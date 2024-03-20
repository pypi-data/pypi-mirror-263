# Copyright (c) FULIUCANSHENG.
# Licensed under the MIT License.

import json
import torch
import torch.nn.functional as F
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
import diffusers.schedulers as schedulers
from transformers import CLIPTextConfig, CLIPTextModel
from diffusers.schedulers import SchedulerMixin
from diffusers.models.attention_processor import (
    AttnAddedKVProcessor,
    AttnAddedKVProcessor2_0,
    LoRAAttnAddedKVProcessor,
    LoRAAttnProcessor,
    LoRAAttnProcessor2_0,
    SlicedAttnAddedKVProcessor,
)
from diffusers.models import (
    ControlNetModel,
    UNet2DModel,
    UNet2DConditionModel,
    AutoencoderKL,
)
from diffusers.pipelines import (
    StableDiffusionPipeline,
    StableDiffusionControlNetPipeline,
)
from diffusers.pipelines.blip_diffusion.modeling_blip2 import (
    Blip2Config,
    Blip2QFormerModel,
    BaseModelOutputWithPoolingAndCrossAttentions,
)
from diffusers.pipelines.blip_diffusion.modeling_ctx_clip import ContextCLIPTextModel
from unitorch.models import (
    GenericModel,
    GenericOutputs,
    QuantizationConfig,
    QuantizationMixin,
)
from unitorch.models.diffusers.modeling_stable import compute_snr


class Blip2QFormerModelV2(Blip2QFormerModel):
    def forward(
        self,
        input_ids,
        attention_mask,
        pixel_values,
        head_mask=None,
        encoder_hidden_states=None,
        encoder_attention_mask=None,
        past_key_values=None,
        use_cache=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
    ):
        batch_size = input_ids.shape[0]
        query_atts = torch.ones(
            (batch_size, self.query_tokens.size()[1]), dtype=torch.long
        ).to(self.device)
        attention_mask = torch.cat([query_atts, attention_mask], dim=1)

        output_attentions = (
            output_attentions
            if output_attentions is not None
            else self.config.output_attentions
        )
        output_hidden_states = (
            output_hidden_states
            if output_hidden_states is not None
            else self.config.output_hidden_states
        )
        return_dict = (
            return_dict if return_dict is not None else self.config.use_return_dict
        )

        # past_key_values_length
        past_key_values_length = (
            past_key_values[0][0].shape[2] - self.config.query_length
            if past_key_values is not None
            else 0
        )

        query_length = self.query_tokens.shape[1]

        embedding_output = self.embeddings(
            input_ids=input_ids,
            query_embeds=self.query_tokens,
            past_key_values_length=past_key_values_length,
        )

        # embedding_output = self.layernorm(query_embeds)
        # embedding_output = self.dropout(embedding_output)

        input_shape = embedding_output.size()[:-1]
        batch_size, seq_length = input_shape
        device = embedding_output.device

        image_embeds_frozen = self.visual_encoder(pixel_values).last_hidden_state
        # image_embeds_frozen = torch.ones_like(image_embeds_frozen)
        encoder_hidden_states = image_embeds_frozen

        if attention_mask is None:
            attention_mask = torch.ones(
                ((batch_size, seq_length + past_key_values_length)), device=device
            )

        # We can provide a self-attention mask of dimensions [batch_size, from_seq_length, to_seq_length]
        # ourselves in which case we just need to make it broadcastable to all heads.
        extended_attention_mask = self.get_extended_attention_mask(
            attention_mask, input_shape, device
        )

        # If a 2D or 3D attention mask is provided for the cross-attention
        # we need to make broadcastable to [batch_size, num_heads, seq_length, seq_length]
        if encoder_hidden_states is not None:
            if isinstance(encoder_hidden_states, list):
                encoder_batch_size, encoder_sequence_length, _ = encoder_hidden_states[
                    0
                ].size()
            else:
                (
                    encoder_batch_size,
                    encoder_sequence_length,
                    _,
                ) = encoder_hidden_states.size()
            encoder_hidden_shape = (encoder_batch_size, encoder_sequence_length)

            if isinstance(encoder_attention_mask, list):
                encoder_extended_attention_mask = [
                    self.invert_attention_mask(mask) for mask in encoder_attention_mask
                ]
            elif encoder_attention_mask is None:
                encoder_attention_mask = torch.ones(encoder_hidden_shape, device=device)
                encoder_extended_attention_mask = self.invert_attention_mask(
                    encoder_attention_mask
                )
            else:
                encoder_extended_attention_mask = self.invert_attention_mask(
                    encoder_attention_mask
                )
        else:
            encoder_extended_attention_mask = None

        # Prepare head mask if needed
        # 1.0 in head_mask indicate we keep the head
        # attention_probs has shape bsz x n_heads x N x N
        # input head_mask has shape [num_heads] or [num_hidden_layers x num_heads]
        # and head_mask is converted to shape [num_hidden_layers x batch x num_heads x seq_length x seq_length]
        head_mask = self.get_head_mask(
            head_mask, self.config.qformer_config.num_hidden_layers
        )

        encoder_outputs = self.encoder(
            embedding_output,
            attention_mask=extended_attention_mask,
            head_mask=head_mask,
            encoder_hidden_states=encoder_hidden_states,
            encoder_attention_mask=encoder_extended_attention_mask,
            past_key_values=past_key_values,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
            query_length=query_length,
        )
        sequence_output = encoder_outputs[0]
        pooled_output = sequence_output[:, 0, :]

        if not return_dict:
            return self.proj_layer(sequence_output[:, :query_length, :])

        return BaseModelOutputWithPoolingAndCrossAttentions(
            last_hidden_state=sequence_output,
            pooler_output=pooled_output,
            past_key_values=encoder_outputs.past_key_values,
            hidden_states=encoder_outputs.hidden_states,
            attentions=encoder_outputs.attentions,
            cross_attentions=encoder_outputs.cross_attentions,
        )


class Blip2ForText2ImageGeneration(GenericModel, QuantizationMixin):
    """
    Blip2ForText2ImageGeneration is a class that represents a model for text-to-image generation using the Blip2 architecture.

    Args:
        config_path (str): The path to the configuration file for the Blip2 model.
        text_config_path (str): The path to the configuration file for the text model.
        qformer_config_path (str): The path to the configuration file for the qformer model.
        vae_config_path (str): The path to the configuration file for the VAE model.
        scheduler_config_path (str): The path to the configuration file for the scheduler.
        quant_config_path (Optional[str]): The path to the configuration file for quantization (default: None).
        image_size (Optional[int]): The size of the input image (default: None).
        in_channels (Optional[int]): The number of input channels (default: None).
        out_channels (Optional[int]): The number of output channels (default: None).
        num_train_timesteps (Optional[int]): The number of training timesteps (default: 1000).
        num_infer_timesteps (Optional[int]): The number of inference timesteps (default: 50).
        freeze_vae_encoder (Optional[bool]): Whether to freeze the VAE encoder (default: True).
        freeze_text_encoder (Optional[bool]): Whether to freeze the text encoder (default: True).
        snr_gamma (Optional[float]): The SNR gamma value (default: 5.0).
        prior_loss_weight (Optional[float]): The weight for the prior loss (default: 1.0).
        lora_r (Optional[int]): The value of lora_r (default: None).
        seed (Optional[int]): The random seed (default: 1123).

    Attributes:
        unet (UNet2DConditionModel): The UNet model.
        text (ContextCLIPTextModel): The text model.
        qformer (Blip2QFormerModelV2): The qformer model.
        vae (AutoencoderKL): The VAE model.
        scheduler (SchedulerMixin): The scheduler.
        vae_scale_factor (int): The scale factor for the VAE.
        quant_config (QuantizationConfig): The quantization configuration.
        pipeline (StableDiffusionPipeline): The diffusion pipeline.

    Methods:
        enable_lora: Enables LoRA attention.
        forward: Performs forward pass (not implemented).
        generate: Generates images based on input prompts.

    """

    prefix_keys_in_state_dict = {
        # unet weights
        "^conv_in.*": "unet.",
        "^conv_norm_out.*": "unet.",
        "^conv_out.*": "unet.",
        "^time_embedding.*": "unet.",
        "^up_blocks.*": "unet.",
        "^mid_block.*": "unet.",
        "^down_blocks.*": "unet.",
        # text weights
        "^text_model.*": "text.",
        # vae weights
        "^encoder.*": "vae.",
        "^decoder.*": "vae.",
        "^post_quant_conv.*": "vae.",
        "^quant_conv.*": "vae.",
    }

    # replace_keys_in_state_dict = {
    #     "\.query\.": ".to_q.",
    #     "\.key\.": ".to_k.",
    #     "\.value\.": ".to_v.",
    #     "\.proj_attn\.": ".to_out.0.",
    # }

    def __init__(
        self,
        config_path: str,
        text_config_path: str,
        qformer_config_path: str,
        vae_config_path: str,
        scheduler_config_path: str,
        quant_config_path: Optional[str] = None,
        image_size: Optional[int] = None,
        in_channels: Optional[int] = None,
        out_channels: Optional[int] = None,
        num_train_timesteps: Optional[int] = 1000,
        num_infer_timesteps: Optional[int] = 50,
        freeze_vae_encoder: Optional[bool] = True,
        freeze_text_encoder: Optional[bool] = True,
        snr_gamma: Optional[float] = 5.0,
        prior_loss_weight: Optional[float] = 1.0,
        lora_r: Optional[int] = None,
        seed: Optional[int] = 1123,
    ):
        super().__init__()
        self.seed = seed
        self.num_train_timesteps = num_train_timesteps
        self.num_infer_timesteps = num_infer_timesteps
        self.image_size = image_size
        self.snr_gamma = snr_gamma
        self.prior_loss_weight = prior_loss_weight

        config_dict = json.load(open(config_path))
        if image_size is not None:
            config_dict.update({"sample_size": image_size})
        if in_channels is not None:
            config_dict.update({"in_channels": in_channels})
        if out_channels is not None:
            config_dict.update({"out_channels": out_channels})
        self.unet = UNet2DConditionModel.from_config(config_dict)

        text_config = CLIPTextConfig.from_json_file(text_config_path)
        self.text = ContextCLIPTextModel(text_config)

        qformer_config = Blip2Config.from_json_file(qformer_config_path)
        self.qformer = Blip2QFormerModelV2(qformer_config)

        vae_config_dict = json.load(open(vae_config_path))
        self.vae = AutoencoderKL.from_config(vae_config_dict)

        scheduler_config_dict = json.load(open(scheduler_config_path))
        scheduler_class_name = scheduler_config_dict.get("_class_name", "DDPMScheduler")
        assert hasattr(schedulers, scheduler_class_name)
        scheduler_class = getattr(schedulers, scheduler_class_name)
        assert issubclass(scheduler_class, SchedulerMixin)
        scheduler_config_dict["num_train_timesteps"] = num_train_timesteps
        self.scheduler = scheduler_class.from_config(scheduler_config_dict)

        self.vae_scale_factor = 2 ** (len(self.vae.config.block_out_channels) - 1)

        if freeze_vae_encoder:
            for param in self.vae.parameters():
                param.requires_grad = False

        if freeze_text_encoder:
            for param in self.text.parameters():
                param.requires_grad = False

        if quant_config_path is not None:
            self.quant_config = QuantizationConfig.from_json_file(quant_config_path)
            self.quantize(self.quant_config, ignore_modules=["lm_head", "unet", "vae"])

        if lora_r is not None:
            for param in self.unet.parameters():
                param.requires_grad = False
            self.enable_lora(lora_r=lora_r)

        self.scheduler.set_timesteps(num_inference_steps=self.num_infer_timesteps)
        self.pipeline = StableDiffusionPipeline(
            vae=self.vae,
            text_encoder=self.text,
            unet=self.unet,
            scheduler=self.scheduler,
            tokenizer=None,
            safety_checker=None,
            feature_extractor=None,
        )
        self.pipeline.set_progress_bar_config(disable=True)

    def enable_lora(self, lora_r: Optional[int] = 4):
        """
        Enables LoRA attention in the UNet model.

        Args:
            lora_r (Optional[int]): The value of lora_r (default: 4).

        """
        lora_attn_procs = {}
        for name, attn_processor in self.unet.attn_processors.items():
            cross_attention_dim = (
                None
                if name.endswith("attn1.processor")
                else self.unet.config.cross_attention_dim
            )
            if name.startswith("mid_block"):
                hidden_size = self.unet.config.block_out_channels[-1]
            elif name.startswith("up_blocks"):
                block_id = int(name[len("up_blocks.")])
                hidden_size = list(reversed(self.unet.config.block_out_channels))[
                    block_id
                ]
            elif name.startswith("down_blocks"):
                block_id = int(name[len("down_blocks.")])
                hidden_size = self.unet.config.block_out_channels[block_id]

            if isinstance(
                attn_processor,
                (
                    AttnAddedKVProcessor,
                    SlicedAttnAddedKVProcessor,
                    AttnAddedKVProcessor2_0,
                ),
            ):
                lora_attn_processor_class = LoRAAttnAddedKVProcessor
            else:
                lora_attn_processor_class = (
                    LoRAAttnProcessor2_0
                    if hasattr(F, "scaled_dot_product_attention")
                    else LoRAAttnProcessor
                )

            module = lora_attn_processor_class(
                hidden_size=hidden_size,
                cross_attention_dim=cross_attention_dim,
                rank=lora_r,
            )

            lora_attn_procs[name] = module

        self.unet.set_attn_processor(lora_attn_procs)

    def forward(
        self,
    ):
        """
        Performs a forward pass through the model.

        Raises:
            NotImplementedError: This method is not implemented.

        """
        raise NotImplementedError

    def generate(
        self,
        input_ids: torch.Tensor,
        negative_input_ids: torch.Tensor,
        refer_input_ids: torch.Tensor,
        refer_pixel_values: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        negative_attention_mask: Optional[torch.Tensor] = None,
        refer_attention_mask: Optional[torch.Tensor] = None,
        height: Optional[int] = 512,
        width: Optional[int] = 512,
        ctx_begin_pos: Optional[int] = 2,
        guidance_scale: Optional[float] = 7.5,
    ):
        """
        Generates images based on input prompts.

        Args:
            input_ids (torch.Tensor): The input IDs.
            negative_input_ids (torch.Tensor): The negative input IDs.
            refer_input_ids (torch.Tensor): The reference input IDs.
            refer_pixel_values (torch.Tensor): The reference pixel values.
            attention_mask (Optional[torch.Tensor]): The attention mask (default: None).
            negative_attention_mask (Optional[torch.Tensor]): The negative attention mask (default: None).
            refer_attention_mask (Optional[torch.Tensor]): The reference attention mask (default: None).
            height (Optional[int]): The height of the generated images (default: 512).
            width (Optional[int]): The width of the generated images (default: 512).
            ctx_begin_pos (Optional[int]): The context begin position (default: 2).
            guidance_scale (Optional[float]): The guidance scale (default: 7.5).

        Returns:
            GenericOutputs: The generated images.

        """
        batch_size = input_ids.shape[0]
        qformer_embeds = self.qformer(
            refer_input_ids,
            refer_attention_mask,
            refer_pixel_values,
            return_dict=False,
        )
        prompt_embeds = self.text(
            input_ids=input_ids,
            # attention_mask,
            ctx_embeddings=qformer_embeds,
            ctx_begin_pos=[ctx_begin_pos] * batch_size,
        )[0]
        negative_prompt_embeds = self.text(
            input_ids=negative_input_ids,
            # negative_attention_mask,
        )[0]

        images = self.pipeline(
            prompt_embeds=prompt_embeds,
            negative_prompt_embeds=negative_prompt_embeds,
            generator=torch.Generator(device=self.pipeline.device).manual_seed(
                self.seed
            ),
            height=height,
            width=width,
            guidance_scale=guidance_scale,
            output_type="np.array",
        ).images

        return GenericOutputs(images=torch.from_numpy(images))


class Blip2ControlNetForText2ImageGeneration(GenericModel, QuantizationMixin):
    """
    Blip2ControlNetForText2ImageGeneration is a class that represents a control network for text-to-image generation using the Blip2 model.

    Args:
        config_path (str): The path to the configuration file for the Blip2 model.
        text_config_path (str): The path to the configuration file for the text model.
        qformer_config_path (str): The path to the configuration file for the qformer model.
        vae_config_path (str): The path to the configuration file for the VAE model.
        controlnet_config_path (str): The path to the configuration file for the control network model.
        scheduler_config_path (str): The path to the configuration file for the scheduler model.
        quant_config_path (Optional[str]): The path to the configuration file for quantization (default: None).
        image_size (Optional[int]): The size of the input image (default: None).
        in_channels (Optional[int]): The number of input channels (default: None).
        out_channels (Optional[int]): The number of output channels (default: None).
        num_train_timesteps (Optional[int]): The number of training timesteps (default: 1000).
        num_infer_timesteps (Optional[int]): The number of inference timesteps (default: 50).
        freeze_vae_encoder (Optional[bool]): Whether to freeze the VAE encoder (default: True).
        freeze_text_encoder (Optional[bool]): Whether to freeze the text encoder (default: True).
        snr_gamma (Optional[float]): The SNR gamma value (default: 5.0).
        prior_loss_weight (Optional[float]): The weight for the prior loss (default: 1.0).
        lora_r (Optional[int]): The LORA rank (default: None).
        seed (Optional[int]): The random seed (default: 1123).

    Attributes:
        unet (UNet2DConditionModel): The UNet model.
        text (ContextCLIPTextModel): The text model.
        qformer (Blip2QFormerModelV2): The qformer model.
        vae (AutoencoderKL): The VAE model.
        controlnet (ControlNetModel): The control network model.
        scheduler (SchedulerMixin): The scheduler model.
        vae_scale_factor (int): The scale factor for the VAE.

    Methods:
        enable_lora(lora_r: Optional[int] = 4): Enables LoRA attention for the UNet model.
        forward(): Performs the forward pass of the model.
        generate(input_ids: torch.Tensor, negative_input_ids: torch.Tensor, refer_input_ids: torch.Tensor, refer_pixel_values: torch.Tensor, condition_pixel_values: torch.Tensor, attention_mask: Optional[torch.Tensor] = None, negative_attention_mask: Optional[torch.Tensor] = None, refer_attention_mask: Optional[torch.Tensor] = None, height: Optional[int] = 512, width: Optional[int] = 512, ctx_begin_pos: Optional[int] = 2, guidance_scale: Optional[float] = 7.5): Generates images based on the input prompts.

    """

    prefix_keys_in_state_dict = {
        # unet weights
        "^conv_in.*": "unet.",
        "^conv_norm_out.*": "unet.",
        "^conv_out.*": "unet.",
        "^time_embedding.*": "unet.",
        "^up_blocks.*": "unet.",
        "^mid_block.*": "unet.",
        "^down_blocks.*": "unet.",
        # text weights
        "^text_model.*": "text.",
        # vae weights
        "^encoder.*": "vae.",
        "^decoder.*": "vae.",
        "^post_quant_conv.*": "vae.",
        "^quant_conv.*": "vae.",
    }

    # replace_keys_in_state_dict = {
    #     "\.query\.": ".to_q.",
    #     "\.key\.": ".to_k.",
    #     "\.value\.": ".to_v.",
    #     "\.proj_attn\.": ".to_out.0.",
    # }

    def __init__(
        self,
        config_path: str,
        text_config_path: str,
        qformer_config_path: str,
        vae_config_path: str,
        controlnet_config_path: str,
        scheduler_config_path: str,
        quant_config_path: Optional[str] = None,
        image_size: Optional[int] = None,
        in_channels: Optional[int] = None,
        out_channels: Optional[int] = None,
        num_train_timesteps: Optional[int] = 1000,
        num_infer_timesteps: Optional[int] = 50,
        freeze_vae_encoder: Optional[bool] = True,
        freeze_text_encoder: Optional[bool] = True,
        snr_gamma: Optional[float] = 5.0,
        prior_loss_weight: Optional[float] = 1.0,
        lora_r: Optional[int] = None,
        seed: Optional[int] = 1123,
    ):
        """
        Initializes the Blip2 model.

        Args:
            config_path (str): The path to the configuration file.
            text_config_path (str): The path to the text configuration file.
            qformer_config_path (str): The path to the qformer configuration file.
            vae_config_path (str): The path to the VAE configuration file.
            controlnet_config_path (str): The path to the controlnet configuration file.
            scheduler_config_path (str): The path to the scheduler configuration file.
            quant_config_path (str, optional): The path to the quantization configuration file. Defaults to None.
            image_size (int, optional): The size of the image. Defaults to None.
            in_channels (int, optional): The number of input channels. Defaults to None.
            out_channels (int, optional): The number of output channels. Defaults to None.
            num_train_timesteps (int, optional): The number of training timesteps. Defaults to 1000.
            num_infer_timesteps (int, optional): The number of inference timesteps. Defaults to 50.
            freeze_vae_encoder (bool, optional): Whether to freeze the VAE encoder. Defaults to True.
            freeze_text_encoder (bool, optional): Whether to freeze the text encoder. Defaults to True.
            snr_gamma (float, optional): The SNR gamma value. Defaults to 5.0.
            prior_loss_weight (float, optional): The weight of the prior loss. Defaults to 1.0.
            lora_r (int, optional): The LORA R value. Defaults to None.
            seed (int, optional): The seed value. Defaults to 1123.
        """
        super().__init__()
        self.seed = seed
        self.num_train_timesteps = num_train_timesteps
        self.num_infer_timesteps = num_infer_timesteps
        self.image_size = image_size
        self.snr_gamma = snr_gamma
        self.prior_loss_weight = prior_loss_weight

        # Load configuration files
        config_dict = json.load(open(config_path))
        if image_size is not None:
            config_dict.update({"sample_size": image_size})
        if in_channels is not None:
            config_dict.update({"in_channels": in_channels})
        if out_channels is not None:
            config_dict.update({"out_channels": out_channels})
        self.unet = UNet2DConditionModel.from_config(config_dict)

        text_config = CLIPTextConfig.from_json_file(text_config_path)
        self.text = ContextCLIPTextModel(text_config)

        qformer_config = Blip2Config.from_json_file(qformer_config_path)
        self.qformer = Blip2QFormerModelV2(qformer_config)

        vae_config_dict = json.load(open(vae_config_path))
        self.vae = AutoencoderKL.from_config(vae_config_dict)

        controlnet_config_dict = json.load(open(controlnet_config_path))
        self.controlnet = ControlNetModel.from_config(controlnet_config_dict)

        scheduler_config_dict = json.load(open(scheduler_config_path))
        scheduler_class_name = scheduler_config_dict.get("_class_name", "DDPMScheduler")
        assert hasattr(schedulers, scheduler_class_name)
        scheduler_class = getattr(schedulers, scheduler_class_name)
        assert issubclass(scheduler_class, SchedulerMixin)
        scheduler_config_dict["num_train_timesteps"] = num_train_timesteps
        self.scheduler = scheduler_class.from_config(scheduler_config_dict)

        self.vae_scale_factor = 2 ** (len(self.vae.config.block_out_channels) - 1)

        # Freeze VAE encoder if specified
        if freeze_vae_encoder:
            for param in self.vae.parameters():
                param.requires_grad = False

        # Freeze text encoder if specified
        if freeze_text_encoder:
            for param in self.text.parameters():
                param.requires_grad = False

        # Load quantization configuration if specified
        if quant_config_path is not None:
            self.quant_config = QuantizationConfig.from_json_file(quant_config_path)
            self.quantize(self.quant_config, ignore_modules=["lm_head", "unet", "vae"])

        # Enable LORA if specified
        if lora_r is not None:
            for param in self.unet.parameters():
                param.requires_grad = False
            self.enable_lora(lora_r=lora_r)

        self.scheduler.set_timesteps(num_inference_steps=self.num_infer_timesteps)
        self.pipeline = StableDiffusionControlNetPipeline(
            vae=self.vae,
            text_encoder=self.text,
            unet=self.unet,
            controlnet=self.controlnet,
            scheduler=self.scheduler,
            tokenizer=None,
            safety_checker=None,
            feature_extractor=None,
        )
        self.pipeline.set_progress_bar_config(disable=True)

    def enable_lora(self, lora_r: Optional[int] = 4):
        """
        Enable LoRA (Local Rank Attention) for the UNet model.

        Args:
            lora_r (Optional[int]): The rank parameter for LoRA. Defaults to 4.

        Returns:
            None
        """
        lora_attn_procs = {}
        for name, attn_processor in self.unet.attn_processors.items():
            cross_attention_dim = (
                None
                if name.endswith("attn1.processor")
                else self.unet.config.cross_attention_dim
            )
            if name.startswith("mid_block"):
                hidden_size = self.unet.config.block_out_channels[-1]
            elif name.startswith("up_blocks"):
                block_id = int(name[len("up_blocks.")])
                hidden_size = list(reversed(self.unet.config.block_out_channels))[
                    block_id
                ]
            elif name.startswith("down_blocks"):
                block_id = int(name[len("down_blocks.")])
                hidden_size = self.unet.config.block_out_channels[block_id]

            if isinstance(
                attn_processor,
                (
                    AttnAddedKVProcessor,
                    SlicedAttnAddedKVProcessor,
                    AttnAddedKVProcessor2_0,
                ),
            ):
                lora_attn_processor_class = LoRAAttnAddedKVProcessor
            else:
                lora_attn_processor_class = (
                    LoRAAttnProcessor2_0
                    if hasattr(F, "scaled_dot_product_attention")
                    else LoRAAttnProcessor
                )

            module = lora_attn_processor_class(
                hidden_size=hidden_size,
                cross_attention_dim=cross_attention_dim,
                rank=lora_r,
            )

            lora_attn_procs[name] = module

        self.unet.set_attn_processor(lora_attn_procs)

    def forward(
        self,
    ):
        """
        Performs the forward pass of the model.

        Raises:
            NotImplementedError: This method should be implemented in a subclass.
        """
        raise NotImplementedError

    def generate(
        self,
        input_ids: torch.Tensor,
        negative_input_ids: torch.Tensor,
        refer_input_ids: torch.Tensor,
        refer_pixel_values: torch.Tensor,
        condition_pixel_values: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        negative_attention_mask: Optional[torch.Tensor] = None,
        refer_attention_mask: Optional[torch.Tensor] = None,
        height: Optional[int] = 512,
        width: Optional[int] = 512,
        ctx_begin_pos: Optional[int] = 2,
        guidance_scale: Optional[float] = 7.5,
        controlnet_conditioning_scale: Optional[float] = 1.0,
    ):
        """
        Generates images based on the given input_ids, negative_input_ids, refer_input_ids,
        refer_pixel_values, condition_pixel_values, and other optional parameters.

        Args:
            input_ids (torch.Tensor): The input tensor representing the prompt.
            negative_input_ids (torch.Tensor): The input tensor representing the negative prompt.
            refer_input_ids (torch.Tensor): The input tensor representing the reference prompt.
            refer_pixel_values (torch.Tensor): The tensor representing the pixel values of the reference image.
            condition_pixel_values (torch.Tensor): The tensor representing the pixel values of the condition image.
            attention_mask (Optional[torch.Tensor], optional): The attention mask tensor. Defaults to None.
            negative_attention_mask (Optional[torch.Tensor], optional): The attention mask tensor for negative_input_ids. Defaults to None.
            refer_attention_mask (Optional[torch.Tensor], optional): The attention mask tensor for refer_input_ids. Defaults to None.
            height (Optional[int], optional): The height of the generated images. Defaults to 512.
            width (Optional[int], optional): The width of the generated images. Defaults to 512.
            ctx_begin_pos (Optional[int], optional): The beginning position of the context embeddings. Defaults to 2.
            guidance_scale (Optional[float], optional): The scale factor for guidance. Defaults to 7.5.

        Returns:
            GenericOutputs: The generated images.
        """
        batch_size = input_ids.shape[0]
        qformer_embeds = self.qformer(
            refer_input_ids,
            refer_attention_mask,
            refer_pixel_values,
            return_dict=False,
        )
        prompt_embeds = self.text(
            input_ids=input_ids,
            # attention_mask,
            ctx_embeddings=qformer_embeds,
            ctx_begin_pos=[ctx_begin_pos] * batch_size,
        )[0]
        negative_prompt_embeds = self.text(
            input_ids=negative_input_ids,
            # negative_attention_mask,
        )[0]

        images = self.pipeline(
            image=condition_pixel_values,
            prompt_embeds=prompt_embeds,
            negative_prompt_embeds=negative_prompt_embeds,
            generator=torch.Generator(device=self.pipeline.device).manual_seed(
                self.seed
            ),
            height=height,
            width=width,
            guidance_scale=guidance_scale,
            controlnet_conditioning_scale=float(controlnet_conditioning_scale),
            output_type="np.array",
        ).images

        return GenericOutputs(images=torch.from_numpy(images))
