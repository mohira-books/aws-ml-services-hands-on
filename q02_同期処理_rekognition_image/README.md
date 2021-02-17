# [Amazon Rekognition（高精度の画像・動画分析サービス）| AWS](https://aws.amazon.com/jp/rekognition/?blog-cards.sort-by=item.additionalFields.createdDate&blog-cards.sort-order=desc)

## 演習: マネジメントコンソール
### 演習1: オブジェクトとシーンの検出

- ポイント
    - 結果の読み方
    - うまくいくパターン
    - うまくいかないパターンも探してみよう！

### 演習2: イメージ内のテキスト

- ポイント
    - 結果の読み方
    - うまくいくパターン
    - うまくいかないパターンも探してみよう！

## 演習: SDKを利用する
### 演習1: オブジェクトとシーンの検出

```python
from pathlib import Path
from pprint import pprint

import boto3


def main():
  client = boto3.client('rekognition', region_name='ap-northeast-1')

  image_file_path = Path(__file__).parent / 'image01.jpg'

  with image_file_path.open(mode='rb') as f:
    bytes_data = f.read()
        response = client.detect_labels(Image={'Bytes': bytes_data})

    pprint(response)

    label_names = [label['Name'] for label in response['Labels']]
    print(f'Label: {label_names}')


if __name__ == '__main__':
    main()
```

### 演習2: イメージ内のテキスト

- [Amazon Textract](https://aws.amazon.com/jp/textract/) もぜひ試してほしい
- ポイント
    - うまくいくパターン
    - うまくいかないパターンも探してみよう！

```python
from pathlib import Path
from pprint import pprint

import boto3


def main():
  client = boto3.client('rekognition', region_name='ap-northeast-1')

  image_file_path = Path(__file__).parent / 'credit_card.png'

  with image_file_path.open(mode='rb') as f:
    bytes_data = f.read()
        response = client.detect_text(Image={'Bytes': bytes_data})

    pprint(response)

    print('===== DetectedText ====')
    for x in response['TextDetections']:
        print(x['DetectedText'])


if __name__ == '__main__':
    main()
```

