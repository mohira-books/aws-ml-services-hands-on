# Cloud9のUbuntu環境で pyocr を使ったテキスト検出を実行する

- 参考
    - [Compilation guide for various platforms | tessdoc](https://tesseract-ocr.github.io/tessdoc/Compiling)
    - [Pythonで日本語OCRを行うときのメモ - Qiita](https://qiita.com/bohemian916/items/67f22ee7aeac103dd205)

## 全体の目標
こんな画像があったときに、

<img width="480" alt="sample.png (87.0 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/03/08/21054/588ea814-1a2f-425e-8849-b58ed4ea6d9a.png">

つぎのような結果を取得し、

```
$ python3 text_detection_sample.py
ブラ
((39, 63), (109, 100))
ウザ
((120, 62), (194, 100))
が
((197, 66), (219, 99))
表示
((221, 63), (349, 101))
し
((0, 0), (1490, 452))
て
((355, 69), (387, 98))
いる
((397, 67), (467, 99))
ダイ
((474, 62), (541, 100))
アロ
((551, 68), (621, 99))
グ
((630, 65), (663, 100))
の
((661, 63), (704, 98))
zoom.us
((708, 75), (868, 99))
を
... 省略
```

バウンディングボックスを描画した画像を保存する。

<img width="480" alt="image.png (125.6 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/03/08/21054/8541ab24-ea2d-4934-9397-2b0c5d158a1a.png">

## 1. Cloud9環境つくり
### Platform は Amazon Linux 2 ではなく Ubuntuを選択する

- Ubuntu は 「ウブントゥ」と読みます(「ウブンツ」という人もいます)

<img width="480" alt="image.png (196.7 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/03/08/21054/9b474f4f-48dd-4ca2-8ac2-04ac6e954ed7.png">

### upgrade や update

```
$ sudo pip3 install --upgrade pip
$ hash -r

# 確認
$ pip -V
pip 21.0.1 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```

```
sudo apt update
```

## 2. opencvの準備
### 目標
まずは、次のコードがエラーなく動くことを目指します。

```python
import cv2

print(cv2)
```

### `opencv-python` の install

```
$ pip install opencv-python pillow
```

この時点ではコードを実行すると、次のようなエラーメッセージがでる。

```
python3: Relink `/lib/x86_64-linux-gnu/libsystemd.so.0' with `/lib/x86_64-linux-gnu/librt.so.1' for IFUNC symbol `clock_gettime'
python3: Relink `/lib/x86_64-linux-gnu/libudev.so.1' with `/lib/x86_64-linux-gnu/librt.so.1' for IFUNC symbol `clock_gettime'
bash: line 6:  5586 Segmentation fault      (core dumped) python3 "$file"
```

そこで、次のコマンドを実行すればOK

```
$ sudo apt install -y python3-opencv
```

### 動作確認

```
$ python3 opencv_check.py
<module 'cv2.cv2' from '/home/ubuntu/.local/lib/python3.6/site-packages/cv2/cv2.cpython-36m-x86_64-linux-gnu.so'>
```

## 3. pyocr の install

- [World / OpenPaperwork / pyocr · GitLab](https://gitlab.gnome.org/World/OpenPaperwork/pyocr)
- `pyocr` があると、OCRライブラリをPythonから実行できる(==ラッパーライブラリ)
    - 今回は Tesseract(後述) というOCRライブラリを利用するが、他のOCRツールも対応している

### pip で install

```
$ pip install pyocr
```

## 4. テキスト検出およびbboxの描画
### 目標
次の画像(`sample.png`とします)のテキストを検出し、bboxを描画した画像を保存すること。

<img width="480" alt="sample.png (87.0 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/03/08/21054/588ea814-1a2f-425e-8849-b58ed4ea6d9a.png">

次のコード(`text_detection_sample`とします)が動作すればOK。

```python
import os
import sys

import cv2
import pyocr
from PIL import Image


def main():
    os.environ['TESSDATA_PREFIX'] = '/usr/local/share/tessdata/tessdata/'

    tools = pyocr.get_available_tools()

    assert len(tools) > 0

    tool = tools[
        1]  # <module 'pyocr.libtesseract' from '/home/ubuntu/.local/lib/python3.6/site-packages/pyocr/libtesseract/__init__.py'>

    img_file_path = 'sample.png'
    output_img_file_path = 'sample_output.png'

    img = Image.open(img_file_path)
    response = tool.image_to_string(img,
                                    lang='jpn_vert',
                                    # ここで言語設定を変えられる(`*.trainedata`が必要)
                                    builder=pyocr.builders.WordBoxBuilder(
                                        tesseract_layout=6))

    output_img = cv2.imread(img_file_path)

    for r in response:
        print(r.content)
        print(r.position)
        cv2.rectangle(output_img, r.position[0], r.position[1], (0, 0, 255), 2)

    cv2.imwrite(output_img_file_path, output_img)


if __name__ == '__main__':
    main()

```

### tesseractのinstall

- OCRを行うために、`tesseract` が必要

```
sudo apt install -y tesseract-ocr
```

### Leptonicaのinstall

- 2021/03/08時点だと、1.75.3。Ubuntu18.04でも動作する。
- :memo: Cloud9のUbuntuは 18.04

```
sudo apt install libleptonica-dev
```

### Language Dataの取得と配備

- tesseract を利用する上では学習済みデータ(`traineddata`)が必要
    - テキスト検出を行う際に、言語などを設定できる
    - [tesseract-ocr/tessdata: Trained models with support for legacy and LSTM OCR engine](https://github.com/tesseract-ocr/tessdata)
      から 好きな `*.traineddata` をDownloadすればOK
    - 今回は、 `jpn_vert.traineddata` と `eng.traineddata`

```
$ sudo mkdir -p /usr/local/share/tessdata/tessdata/

$ sudo wget https://github.com/tesseract-ocr/tessdata_best/raw/master/jpn_vert.traineddata --directory-prefix=/usr/local/share/tessdata/tessdata/        

$ sudo wget https://github.com/tesseract-ocr/tessdata_best/raw/master/eng.traineddata --directory-prefix=/usr/local/share/tessdata/tessdata/        


# 確認
$ ls /usr/local/share/tessdata/tessdata/
eng.traineddata  jpn_vert.traineddata
```

### 動作確認
<img width="480" alt="image.png (125.6 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/03/08/21054/8541ab24-ea2d-4934-9397-2b0c5d158a1a.png">

```
$ python3 text_detection_sample.py
ブラ
((39, 63), (109, 100))
ウザ
((120, 62), (194, 100))
が
((197, 66), (219, 99))
表示
((221, 63), (349, 101))
し
((0, 0), (1490, 452))
て
((355, 69), (387, 98))
いる
((397, 67), (467, 99))
ダイ
((474, 62), (541, 100))
アロ
((551, 68), (621, 99))
グ
((630, 65), (663, 100))
の
((661, 63), (704, 98))
zoom.us
((708, 75), (868, 99))
を
((872, 64), (947, 101))
開く
((957, 64), (1025, 101))
を
((0, 0), (1490, 452))
クリ
((1034, 65), (1124, 100))
ッ
((1122, 74), (1142, 100))
ク
((1154, 65), (1183, 100))
し
((1198, 66), (1224, 99))
て
((1231, 69), (1263, 98))
くだ
((1274, 64), (1343, 100))
さい
((1352, 65), (1423, 99))
ダイ
((17, 142), (84, 180))
アロ
((94, 148), (164, 179))
グ
((173, 145), (205, 180))
が
((203, 143), (235, 179))
表示
((236, 143), (328, 181))
され
((335, 145), (408, 180))
な
((412, 145), (447, 179))
い
((455, 149), (470, 177))
場
((475, 144), (582, 181))
合
((584, 146), (607, 179))
は
((611, 170), (622, 181))
、
((0, 0), (1490, 452))
以
((652, 145), (727, 181))
下
((733, 148), (766, 178))
の
((774, 145), (803, 180))
ミ
((0, 0), (1490, 452))
ー
((812, 159), (847, 165))
テ
((852, 147), (887, 180))
ィング
((895, 144), (1004, 181))
を
((1003, 143), (1046, 180))
起動
((1050, 144), (1165, 181))
を
((1174, 145), (1203, 180))
クリ
((1219, 147), (1264, 179))
ッ
((1262, 154), (1282, 180))
ク
((1294, 145), (1323, 180))
し
((1338, 146), (1364, 179))
て
((1371, 149), (1403, 178))
く
((1414, 145), (1435, 180))
だ
((673, 224), (707, 259))
さい
((716, 225), (787, 259))

```

## 5. (おまけ) pyocrのパラメータ調整ポイント
### Builder によって検出結果が異なる

- `TextBuilder`  文字列を認識
- `WordBoxBuilder`  単語単位で文字認識 + BoundingBox   **← 今回はこれ！**
- `LineBoxBuilder`  行単位で文字認識 + BoundingBox
- `DigitBuilder`  数字 / 記号を認識
- `DigitLineBoxBuilder`  数字 / 記号を認識 + BoundingBox

### `tesseract_layout` をいじると変わる

-
参考: [Pythonで文字認識 | inglow：愛知名古屋のマーケティングオートメーション・Webプロモーション](https://inglow.jp/techblog/ocr/)

- `0`: 文字角度の識別と書字系のみの認識(OSD)のみ実施(OCRは実施されない)
- `1`: OSDを利用した自動ページセグメンテーション
- `2`: OSDまたはOCRを利用しない自動セグメンテーション
- `3`: OSDなしの完全自動セグメンテーション（デフォルト）
- `4`: 可変サイズの1列テキストを想定する
- `5`: 縦書きの単一のテキストブロックと想定する
- `6`: **横書きの単一のテキストブロックと想定する ← 今回はこれ！**
- `7`: 画像を1行のテキストと想定する
- `8`: 画像を１つの単語と想定する
- `9`: 円の中に記載された1単語と想定する（①などの丸数字等）
- `10`: 画像を1文字と想定する

以上