# Amazon Rekognition Custom Labels の使い方

## この記事はなにか？

- Amazon Rekognition Custom Labels を使って、独自モデルの学習及び推論を行うための手続きを記述したものです
- 使用するサービス
    - `S3`
    - `Amazon Rekognition Custom Labels`
    - `AWS Cloud9`

### 手順概要

1. 事前準備: S3バケットに学習用の画像データをアップロードする
2. 東京リージョンでのカスタムラベルのページを表示する
3. プロジェクトを作成する
4. データセットの作成
5. ラベル付け
6. モデルのトレーニング
7. 学習の結果を確認する
8. モデル使って推論する

## 1. 事前準備: S3バケットに学習用の画像データをアップロードする
Custom Labels を利用する前に、学習データを用意を行います。

本稿の説明では、次のバケットを利用しています。

- バケット名: `2021-02-15-bob-bucket`
- リージョン: 東京リージョン(`ap-northeast-1`)

### 今回利用するダミー画像
利用するデータは画像は下記のような画像を利用します(灰色画像または、灰色画像のどこかにQRコードが含まれる簡素なデータ)。

QRコードの検知を行うことを目標にします。

<img width="360" alt="001.png (1.1 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/82f0f167-1023-4aed-90d3-e6e5efc30724.png">

<img width="360" alt="010.png (1.1 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/186c9173-b5b4-4cd7-8d7b-c3833819c96d.png">

<img width="360" alt="001.png (979 B)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/1cf5bf8c-2167-4731-bebb-aad73258cb67.png">

### S3バケットに画像を配備する
下記のようなフォルダ構造にします。

後ほど学習用の「データセット」をつくるときに、ラベルごとにフォルダ分けをすることでラベリングの負担が減ります。

```
2021-02-15-bob-bucket
└── custom_label
    ├── with_qr ← QRコードが含まれる画像用のフォルダ
    │    ├── 001.png
    │    ├── 002.png
    │    ├── ...
    │    └── 020.png
    └── without_qr ← QRコードが含まれない画像用のフォルダ
        ├── 001.png
        ├── 002.png
        ├── ...
        └── 020.png
```

## 2. 東京リージョンでのカスタムラベルのページを表示する

- Rekognition Custom Labels のページに移動します
    - https://ap-northeast-1.console.aws.amazon.com/rekognition/custom-labels?region=ap-northeast-1#/
- リージョンが東京(`ap-northeast-1`) であることを確認します

## 3. プロジェクトを作成する

- 「Get Started」 を押すと、プロジェクト作成画面に遷移します
- プロジェクト名を入力します
    - 本稿では `2021-02-15-bob-project` というプロジェクト名を利用します
- プロジェクト名を入力したら「プロジェクトを作成」をクリックします

## 4. データセットの作成
つづいて「データセット」を作成します。

「データセット」は学習のために利用するデータです(`Amazon Lookout For Vision`などで利用する「データセット」と同じようなものです)。

画像を登録する方法はいくつかありますが、今回はS3バケットの特定フォルダを指定する方式を採用します。

すこし手順が長いのと、S3との行き来があってややこしいので、ゆっくりやりましょう。

### データセットの詳細を入力する

- データセット名: わかりやすいデータセット名をつけてください
    - 今回は `qrcode-dataset-bob` としています
- 画像の場所: 「Amazon S3 バケットから画像をインポートする」
- S3フォルダの場所: 対象となるフォルダの **S3URI** を入力します
    - :memo: S3URI とは、S3のフォルダ(バケット)やデータ(オブジェクト)を指し示す情報です
    - S3で、対象のフォルダのページを開くと「S3URI」をコピーできます
    - 今回の例では、`s3://2021-02-15-bob-bucket/custom_label/` になります
- 自動ラベル付け: 「画像が保存されているフォルダに基づいて、画像にラベルを自動的にアタッチします。」にチェックを入れる

#### S3URIのコピー方法
<img width="480" alt="image.png (298.1 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/a6895923-b165-4d1e-8c65-726bc2e24078.png">

#### 入力例
<img width="480" alt="image.png (425.0 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/50e3e30f-e163-4703-9385-da7ae59217d7.png">

### バケットポリシーを設定する

- 「S3 バケットが正しく設定されていることを確認してください」に表示されているコードを、今回利用するS3バケットポリシーとしてコピペします。
    - :memo: バケットポリシー とは S3バケットの権限操作の設定です

<img width="480" alt="image.png (461.4 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/f0d1ffb9-284e-431e-be25-b152430a1aee.png">

#### バケットポリシー編集画面へ移動する方法
対象のS3バケットのページを開く > アクセス許可 > バケットポリシー(画面中部あたり) > 編集


<img width="480" alt="image.png (331.4 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/bab9df9f-439d-4b22-92b2-2ef4a02c0460.png">

#### バケットポリシーの編集画面で先程のコードを貼り付ける

- 貼り付けたら「変更を保存」でOKです
- うまくいくと、画面上部に「バケットポリシーが正常に編集されました。」というメッセージが出ます。

<img width="480" alt="image.png (383.9 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/0cdf92aa-0af5-43e7-ae26-fcdc61ef0954.png">

### カスタムラベルのページに戻り、提出(Submit)をクリックする

- 「提出」をクリックすると、**画面上部に「Access Denied.」と表示されますが、問題ありません**
- データセットのページに移動すると、無事、`qrcode-dataset-bob` ができています

<img width="480" alt="image.png (55.8 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/6adc61bd-527c-4437-b8ab-5cc9093ae6a9.png">

## 5. ラベル付け
### まずはデータセットを確認する

- 今回は、S3バケットでの自動ラベリングをつかったので  `with_qr` と `without_qr` のラベルがすでについています

<img width="480" alt="image.png (389.7 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/3e92e5de-ab3c-4e1e-b68e-ffade3458926.png">

### バウンディングボックスをつける

- 物体検知をする場合はアノテーションが必要です
    - **物体検知ではなく、カスタムラベルでの分類が目的の場合は、バウンディングボックスの描画は不要です。**
- データセット詳細画面で「ラベル付けを開始」をクリックします
- 画像を選択します
- 「Draw bounding box」をクリックします

<img width="480" alt="image.png (385.4 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/354eb78a-b314-45de-a517-a782c9a641b8.png">

### バウンディングボックスを描く

1. 右側からラベルを選択します。ショートカットとして「1」を押すと、`with_qr`が選択できます
2. マウスでバウンディングボックスを描きます
3. バウンディングボックスが描けたら、Doneをクリック(または、 Shift + D)します
4. 1~3をすべての画像で繰り返します
5. すべてが終わったら、データセットのページに戻るので、「Save Changes」をクリックします
6. 「終了」をクリックする

<img width="480" alt="image.png (208.4 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/58824dbd-dd0f-472f-87cb-cb1ee21b1175.png">

<img width="480" alt="image.png (377.8 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/7e01bd53-6644-4b8f-9910-2082ab78f7c1.png">

## 6. モデルのトレーニング
すべてのアノテーションが完了したら、「モデルのトレーニング」をクリックします

<img width="480" alt="image.png (389.0 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/756d0965-cd95-4172-90c1-1480f7ce291b.png">

#### トレーニングの詳細を記入する

- プロジェクトを選択: プロジェクト名を入力します
- トレーニングデータセットを選択: アノテーションが完了しているデータセットを選択します
- テストセットを作成: テストに使うためのデータを選択します。いくつか方法があります。
    - 今回は、「トレーニングデータセットを分割」を採用します
    - すでに、テスト用のデータセットがあればそれを使いましょう
      <img width="480" alt="image.png (357.3 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/039f81a8-c76d-4fa8-84d8-5e743c6cf4e9.png">

#### トレーニングを開始する

- 「トレーニング」をクリックする
- しばらく待ちます。40枚のデータで、約1時間くらいはかかります。

<img width="480" alt="image.png (351.6 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/50144685-0364-4cd2-aa24-c0f031475c9b.png">

## 7. 学習の結果を確認する

- **今回はカスタムラベルの使い方が主眼であり、データセットが現実に即していません。そのため、異様に高い精度がでていることに注意してください**

## 8. モデル使って推論する

- `Lookout for Vision` などと違って、**コンソール上から推論は利用できません**
    - 必ず、APIを利用して、プログラムから実行する必要があります
    - 今回は Cloud9 の環境でPythonプログラムを実行します
- 利用するPythonコードは、学習したモデル詳細ページ下部の「モデルを使用する」> 「APIコード」にあります
    - 一部修正が必要ですが、ゼロから書くことはありません

<img width="480" alt="image.png (381.7 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/5f2fd6d5-8159-4675-9720-558627e43ac9.png">

### Cloud9環境の準備

- Cloud9環境を起動します
- 下記のコードを画面下部(ターミナルといいます)に貼り付けてEnterを押します
    - モデルの推論に必要なものをインストールする手続きを行っています

```
sudo pip3 install boto3 pillow
```

<img width="480" alt="image.png (317.8 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/88104361-812b-48a4-a6e0-60f019ed7efd.png">

### モデルの起動

- プログラムをつかってモデルを起動します(エンドポイントの作成)
    - モデルの起動をしていないと推論できない
    - モデルの起動は数分かかる場合があります
- 手順
    - `start_model.py` というファイルを作ります
    - `start_model.py` に「モデルを開始する」にあるPythonコードを貼り付けて、保存します
    - 画面上部の「Run」をクリックするとプログラムが動作します
    - 画面に Done. とでるまで、しばらく待機しましょう
- 今回のプロジェクトの場合のソースコード例を記述します

正しく起動された場合は次のような出力が得られます。

```
Starting model: arn:aws:rekognition:ap-northeast-1:293714825488:project/2021-02-15-bob-project/version/2021-02-15-bob-project.2021-02-15T14.19.24/1613366364610
Status: RUNNING
Message: The model is running.
Done...
```

また、コンソールは次のような表示になります。

<img width="720" alt="image.png (237.2 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/5e6e4fd7-b550-4c10-9e82-e200a86a8bc1.png">

```python
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3


def start_model(project_arn, model_arn, version_name, min_inference_units):
    client = boto3.client('rekognition')

    try:
        # Start the model
        print('Starting model: ' + model_arn)
        response = client.start_project_version(ProjectVersionArn=model_arn,
                                                MinInferenceUnits=min_inference_units)
        # Wait for the model to be in the running state
        project_version_running_waiter = client.get_waiter(
            'project_version_running')
        project_version_running_waiter.wait(ProjectArn=project_arn,
                                            VersionNames=[version_name])

        # Get the running status
        describe_response = client.describe_project_versions(
            ProjectArn=project_arn,
            VersionNames=[version_name])
        for model in describe_response['ProjectVersionDescriptions']:
            print("Status: " + model['Status'])
            print("Message: " + model['StatusMessage'])
    except Exception as e:
        print(e)

    print('Done...')


def main():
    project_arn = 'arn:aws:rekognition:ap-northeast-1:293714825488:project/2021-02-15-bob-project/1613363483971'
    model_arn = 'arn:aws:rekognition:ap-northeast-1:293714825488:project/2021-02-15-bob-project/version/2021-02-15-bob-project.2021-02-15T14.19.24/1613366364610'
    min_inference_units = 1
    version_name = '2021-02-15-bob-project.2021-02-15T14.19.24'
    start_model(project_arn, model_arn, version_name, min_inference_units)


if __name__ == "__main__":
    main()
```

### 推論

- 推論を行う場合には、推論したい対象をS3バケットに事前に配備する必要があります
- 手順
    - `analyze.py` というファイルを作ります
    - `analyze.py` に「画像を分析する 」にあるPythonコードを貼り付けて、保存します
    - ソースコードを編集します
        - `MY_BUCKET` を、対象画像が保存されているバケット名にします
            - ex: `2021-02-15-bob-bucket`
        - `MY_IMAGE_KEY` を、対象画像の「キー」にします
            - ex: `sample_images/test001.png`
        - 変更が終わったらファイルを保存します
    - 画面上部の「Run」をクリックするとプログラムが動作します
    - 画面に Done. とでるまで、しばらく待機しましょう
- 今回のプロジェクトの場合のソースコード例を記述します

```
Detected custom labels for sample_images/test001.png
Label with_qr
Confidence 98.26100158691406
Custom labels detected: 1
```

```python
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont


def display_image(bucket, photo, response):
    # Load image from S3 bucket
    s3_connection = boto3.resource('s3')

    s3_object = s3_connection.Object(bucket, photo)
    s3_response = s3_object.get()

    stream = io.BytesIO(s3_response['Body'].read())
    image = Image.open(stream)

    # Ready image to draw bounding boxes on it.
    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)

    # calculate and display bounding boxes for each detected custom label
    print('Detected custom labels for ' + photo)
    for customLabel in response['CustomLabels']:
        print('Label ' + str(customLabel['Name']))
        print('Confidence ' + str(customLabel['Confidence']))
        if 'Geometry' in customLabel:
            box = customLabel['Geometry']['BoundingBox']
            left = imgWidth * box['Left']
            top = imgHeight * box['Top']
            width = imgWidth * box['Width']
            height = imgHeight * box['Height']

            fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 50)
            draw.text((left, top), customLabel['Name'], fill='#00d400',
                      font=fnt)

            print('Left: ' + '{0:.0f}'.format(left))
            print('Top: ' + '{0:.0f}'.format(top))
            print('Label Width: ' + "{0:.0f}".format(width))
            print('Label Height: ' + "{0:.0f}".format(height))

            points = (
                (left, top),
                (left + width, top),
                (left + width, top + height),
                (left, top + height),
                (left, top))
            draw.line(points, fill='#00d400', width=5)

    image.show()


def show_custom_labels(model, bucket, photo, min_confidence):
    client = boto3.client('rekognition')

    # Call DetectCustomLabels
    response = client.detect_custom_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MinConfidence=min_confidence,
        ProjectVersionArn=model)

    # For object detection use case, uncomment below code to display image.
    # display_image(bucket, photo, response)

    return len(response['CustomLabels'])


def main():
    bucket = 'MY_BUCKET'  # <--- MEMO: ここをバケット名に修正する
    photo = 'MY_IMAGE_KEY'  # <--- MEMO: ここを推論したいデータの「キー」に修正する

    model = 'arn:aws:rekognition:ap-northeast-1:293714825488:project/2021-02-15-bob-project/version/2021-02-15-bob-project.2021-02-15T14.19.24/1613366364610'
    min_confidence = 95

    label_count = show_custom_labels(model, bucket, photo, min_confidence)
    print("Custom labels detected: " + str(label_count))


if __name__ == "__main__":
    main()
```

### モデルの停止

- モデルを停止します。**必ず停止してください！**
- 手順
    - `stop_model.py` というファイルを作ります
    - `stop_model.py` に「モデルを停止する」にあるPythonコードを貼り付けて、保存します
    - 画面上部の「Run」をクリックするとプログラムが動作します
    - 画面に Done. とでるまで、しばらく待機しましょう
- 今回のプロジェクトの場合のソースコード例を記述します

ただしく停止した場合は下記のような出力になります。

```
Stopping model:arn:aws:rekognition:ap-northeast-1:293714825488:project/2021-02-15-bob-project/version/2021-02-15-bob-project.2021-02-15T14.19.24/1613366364610
Status: STOPPING
Done...
```

また、コンソールは次のような表示になります。

<img width="720" alt="image.png (113.7 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/15/21054/ba76677c-52f4-46ac-a74b-fd1d92aba7cf.png">

```python
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-custom-labels-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import time


def stop_model(model_arn):
    client = boto3.client('rekognition')

    print('Stopping model:' + model_arn)

    # Stop the model
    try:
        response = client.stop_project_version(ProjectVersionArn=model_arn)
        status = response['Status']
        print('Status: ' + status)
    except Exception as e:
        print(e)

    print('Done...')


def main():
    model_arn = 'arn:aws:rekognition:ap-northeast-1:293714825488:project/2021-02-15-bob-project/version/2021-02-15-bob-project.2021-02-15T14.19.24/1613366364610'
    stop_model(model_arn)


if __name__ == "__main__":
    main()
```

以上