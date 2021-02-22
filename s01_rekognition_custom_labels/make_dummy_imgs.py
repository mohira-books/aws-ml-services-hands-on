import random
from pathlib import Path

import cv2
import numpy as np
import qrcode
from PIL import Image
from PIL.PngImagePlugin import PngImageFile
from qrcode.image.pil import PilImage


def make_blank_image(save_file_name: Path, width: int, height: int) -> None:
    blank = np.zeros((height, width, 3))
    blank += 122
    cv2.imwrite(str(save_file_name), blank)


def make_qr_code() -> PilImage:
    qr = qrcode.QRCode(box_size=2)
    qr.make()

    return qr.make_image()


def make_overlay_qrcode(file_path: Path) -> PngImageFile:
    img_bg = Image.open(file_path)
    width = img_bg.size[0]
    height = img_bg.size[1]

    position = (random.randint(0, width - 60), random.randint(0, height - 60))
    img_bg.paste(make_qr_code(), position)

    return img_bg


def main():
    project_dir = Path(__file__).parent
    with_qr_dir = project_dir / 'with_qr'
    without_qr_dir = project_dir / 'without_qr'

    with_qr_dir.mkdir(exist_ok=True)
    without_qr_dir.mkdir(exist_ok=True)

    blank_img_path = project_dir / 'blank360x240.png'

    for i in range(1, 20 + 1):
        img_bg = make_overlay_qrcode(blank_img_path)
        img_bg.save(with_qr_dir / f'{i:03d}.png')

        make_blank_image(without_qr_dir / f'{i:03d}.png', img_bg.size[0], img_bg.size[1])


if __name__ == '__main__':
    main()
