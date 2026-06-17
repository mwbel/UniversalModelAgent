from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable


def crop_block_image(page_image_path: str | Path, bbox: Iterable[float], padding: int = 8) -> str:
    """Crop bbox from a page image and return the cropped image path."""

    try:
        from PIL import Image
    except ModuleNotFoundError as exc:
        raise RuntimeError("Pillow is required for image cropping. Install it with `pip install Pillow`.") from exc

    image_path = Path(page_image_path)
    coords = [float(v) for v in bbox]
    if len(coords) != 4:
        raise ValueError(f"bbox must have four values, got {bbox}")

    with Image.open(image_path) as image:
        width, height = image.size
        x0, y0, x1, y1 = _scale_bbox_if_normalized(coords, width, height)
        left = max(0, int(round(min(x0, x1))) - padding)
        top = max(0, int(round(min(y0, y1))) - padding)
        right = min(width, int(round(max(x0, x1))) + padding)
        bottom = min(height, int(round(max(y0, y1))) + padding)
        if right <= left or bottom <= top:
            raise ValueError(f"invalid crop region {coords} for image {image_path}")
        cropped = image.crop((left, top, right, bottom))
        output_dir = image_path.parent / "mathpix_crops"
        output_dir.mkdir(parents=True, exist_ok=True)
        digest = hashlib.sha256(f"{image_path}:{left}:{top}:{right}:{bottom}".encode("utf-8")).hexdigest()[:16]
        output_path = output_dir / f"{image_path.stem}_{digest}.png"
        cropped.save(output_path)
        return str(output_path)


def _scale_bbox_if_normalized(coords: list[float], width: int, height: int) -> list[float]:
    if all(0 <= value <= 1 for value in coords):
        x0, y0, x1, y1 = coords
        return [x0 * width, y0 * height, x1 * width, y1 * height]
    if all(0 <= value <= 1000 for value in coords) and (width > 1000 or height > 1000):
        x0, y0, x1, y1 = coords
        return [x0 / 1000 * width, y0 / 1000 * height, x1 / 1000 * width, y1 / 1000 * height]
    return coords
