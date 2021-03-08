import os

import cv2
import pyocr
from PIL import Image


def main():
    """
    Cloud9のUbuntu環境で動作するコードです。詳しくは README.md をみてください。
    """
    os.environ['TESSDATA_PREFIX'] = '/usr/local/share/tessdata/tessdata/'

    tools = pyocr.get_available_tools()

    assert len(tools) > 0

    # <module 'pyocr.libtesseract' from '/home/ubuntu/.local/lib/python3.6/site-packages/pyocr/libtesseract/__init__.py'>
    tool = tools[1]

    img_file_path = 'sample.png'
    output_img_file_path = 'sample_output.png'

    img = Image.open(img_file_path)
    response = tool.image_to_string(img,
                                    lang='jpn_vert',  # ここで言語設定を変えられる(言語ごとの `*.traineddata`が必要)
                                    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=6))

    output_img = cv2.imread(img_file_path)

    for r in response:
        print(r.content)
        print(r.position)
        cv2.rectangle(output_img, r.position[0], r.position[1], (0, 0, 255), 2)

    cv2.imwrite(output_img_file_path, output_img)


if __name__ == '__main__':
    main()
