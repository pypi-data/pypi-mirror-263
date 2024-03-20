# Copyright (c) FULIUCANSHENG.
# Licensed under the MIT License.

import os
import torch
import json
import numpy as np
from PIL import Image, ImageFilter
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
from transformers import CLIPTokenizer
from torchvision.transforms import (
    Resize,
    CenterCrop,
    ToTensor,
    Normalize,
    Compose,
    RandomHorizontalFlip,
)
from diffusers.image_processor import VaeImageProcessor
from unitorch.models import HfTextClassificationProcessor, GenericOutputs


class ControlNetProcessor(HfTextClassificationProcessor):
    def __init__(
        self,
        vocab_path: str,
        merge_path: str,
        vae_config_path: str,
        max_seq_length: Optional[int] = 77,
        position_start_id: Optional[int] = 0,
        pad_token: Optional[str] = "<|endoftext|>",
        image_size: Optional[int] = 512,
    ):
        tokenizer = CLIPTokenizer(
            vocab_file=vocab_path,
            merges_file=merge_path,
        )
        tokenizer.cls_token = tokenizer.bos_token
        tokenizer.sep_token = tokenizer.eos_token
        tokenizer.pad_token = pad_token
        super().__init__(
            tokenizer=tokenizer,
            max_seq_length=max_seq_length,
            position_start_id=position_start_id,
        )
        self.vision_processor = Compose(
            [
                Resize(image_size),
                CenterCrop(image_size),
                ToTensor(),
                Normalize([0.5], [0.5]),
            ]
        )
        self.condition_vision_processor = Compose(
            [
                Resize(image_size),
                CenterCrop(image_size),
                ToTensor(),
            ]
        )

        vae_config_dict = json.load(open(vae_config_path))
        vae_scale_factor = 2 ** (len(vae_config_dict.get("block_out_channels", [])) - 1)
        self.vae_image_processor = VaeImageProcessor(
            vae_scale_factor=vae_scale_factor, do_convert_rgb=True
        )
        self.vae_mask_image_processor = VaeImageProcessor(
            vae_scale_factor=vae_scale_factor
        )
        self.vae_condition_image_processor = VaeImageProcessor(
            vae_scale_factor=vae_scale_factor,
            do_convert_rgb=True,
            do_normalize=False,
        )

    def text2image(
        self,
        image: Union[Image.Image, str],
        condition_image: Union[Image.Image, str],
        prompt: str,
        max_seq_length: Optional[int] = None,
    ):
        if isinstance(image, str):
            image = Image.open(image)
        image = image.convert("RGB")
        if isinstance(condition_image, str):
            condition_image = Image.open(condition_image)
        condition_image = condition_image.convert("RGB")

        pixel_values = self.vision_processor(image)
        condition_pixel_values = self.condition_vision_processor(condition_image)

        prompt_outputs = self.classification(prompt, max_seq_length=max_seq_length)

        return GenericOutputs(
            input_ids=prompt_outputs.input_ids,
            attention_mask=prompt_outputs.attention_mask,
            pixel_values=pixel_values,
            condition_pixel_values=condition_pixel_values,
        )

    def text2image_inputs(
        self,
        condition_image: Union[Image.Image, str],
        prompt: str,
        negative_prompt: Optional[str] = "",
        max_seq_length: Optional[int] = None,
    ):
        if isinstance(condition_image, str):
            condition_image = Image.open(condition_image)
        condition_image = condition_image.convert("RGB")

        condition_pixel_values = self.vae_condition_image_processor.preprocess(
            condition_image
        )[0]

        prompt_outputs = self.classification(prompt, max_seq_length=max_seq_length)
        negative_prompt_outputs = self.classification(
            negative_prompt, max_seq_length=max_seq_length
        )

        return GenericOutputs(
            input_ids=prompt_outputs.input_ids,
            attention_mask=prompt_outputs.attention_mask,
            condition_pixel_values=condition_pixel_values,
            negative_input_ids=negative_prompt_outputs.input_ids,
            negative_attention_mask=negative_prompt_outputs.attention_mask,
        )

    def image2image_inputs(
        self,
        image: Union[Image.Image, str],
        condition_image: Union[Image.Image, str],
        prompt: str,
        negative_prompt: Optional[str] = "",
        max_seq_length: Optional[int] = None,
    ):
        if isinstance(image, str):
            image = Image.open(image)
        image = image.convert("RGB")

        pixel_values = self.vae_image_processor.preprocess(image)[0]

        text_inputs = self.text2image_inputs(
            condition_image=condition_image,
            prompt=prompt,
            negative_prompt=negative_prompt,
            max_seq_length=max_seq_length,
        )

        return GenericOutputs(
            pixel_values=pixel_values,
            **text_inputs,
        )

    def inpainting_inputs(
        self,
        image: Union[Image.Image, str],
        mask_image: Union[Image.Image, str],
        condition_image: Union[Image.Image, str],
        prompt: str,
        negative_prompt: Optional[str] = "",
        max_seq_length: Optional[int] = None,
    ):
        if isinstance(image, str):
            image = Image.open(image)
        image = image.convert("RGB")

        if isinstance(mask_image, str):
            mask_image = Image.open(mask_image)
        mask_image = mask_image.convert("L")

        pixel_values = self.vae_image_processor.preprocess(image)[0]
        pixel_masks = self.vae_mask_image_processor.preprocess(mask_image)[0]
        pixel_masks = (pixel_masks + 1) / 2

        text_inputs = self.text2image_inputs(
            condition_image=condition_image,
            prompt=prompt,
            negative_prompt=negative_prompt,
            max_seq_length=max_seq_length,
        )
        return GenericOutputs(
            pixel_values=pixel_values,
            pixel_masks=pixel_masks,
            **text_inputs,
        )
