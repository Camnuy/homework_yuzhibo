from __future__ import annotations

from pathlib import Path

import numpy as np
import torch
from PIL import Image
from transformers import CLIPModel, CLIPProcessor

from .config import EMBEDDING_MODEL_ID, MODEL_ROOT, RUNTIME_MODEL_ROOT


def _normalize(array: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(array, axis=-1, keepdims=True)
    norms = np.clip(norms, 1e-12, None)
    return array / norms


class ClipEmbedder:
    def __init__(self, model_id: str = EMBEDDING_MODEL_ID) -> None:
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        model_source = str(RUNTIME_MODEL_ROOT if RUNTIME_MODEL_ROOT.exists() else MODEL_ROOT) if (RUNTIME_MODEL_ROOT.exists() or MODEL_ROOT.exists()) else model_id
        self.processor = CLIPProcessor.from_pretrained(model_source)
        self.model = CLIPModel.from_pretrained(model_source).to(self.device)
        self.model.eval()

    @torch.inference_mode()
    def encode_image(self, image: Image.Image) -> np.ndarray:
        rgb_image = image.convert("RGB")
        inputs = self.processor(images=rgb_image, return_tensors="pt").to(self.device)
        features = self.model.get_image_features(**inputs)
        if hasattr(features, "image_embeds"):
            features = features.image_embeds
        elif hasattr(features, "pooler_output"):
            features = features.pooler_output
        array = features.detach().cpu().numpy()[0]
        return _normalize(array[None, :])[0]

    @torch.inference_mode()
    def encode_text(self, text: str) -> np.ndarray:
        inputs = self.processor(text=[text], return_tensors="pt", padding=True).to(self.device)
        features = self.model.get_text_features(**inputs)
        if hasattr(features, "text_embeds"):
            features = features.text_embeds
        elif hasattr(features, "pooler_output"):
            features = features.pooler_output
        array = features.detach().cpu().numpy()[0]
        return _normalize(array[None, :])[0]

    def encode_paths(self, paths: list[Path]) -> np.ndarray:
        embeddings: list[np.ndarray] = []
        for path in paths:
            with Image.open(path) as image:
                embeddings.append(self.encode_image(image))
        return np.vstack(embeddings)
