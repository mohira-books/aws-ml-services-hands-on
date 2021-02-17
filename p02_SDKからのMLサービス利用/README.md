# プログラムからMLサービス利用する

## マネジメントコンソールとプログラムからの利用
AWSのサービスの多くは、マネジメントコンソールから利用できます。

マネジメントコンソールでは、特にプログラミングを知らなくても操作できる上に、結果を見やすく表示したりしてくれるので非常に便利です。

しかし、大量のデータの処理となってくると途端に厳しくなります。

そこで、プログラムからAWSのサービスを操作する方法の概論を説明します。

まず、マネジメントコンソールと、プログラムからの利用の違いを簡単にまとめます。

|  | マネジメントコンソール | APIからの利用 |
| --- | --- | --- |
| 処理方法 | 同期処理が中心 | 非同期処理が中心 |
| 結果の表示 | Viewerでカンタンに確認できる | 取得したい情報を自力で処理する必要がある |
| 取得できる情報 | Viewerで表示される情報のみ | すべての情報が取得できる |
| 操作方法 | ブラウザ上での操作 | プログラムからの操作 |
| 向き不向き | 簡易実験なら便利。大量処理は厳しい | 大量にさばける。実装が負担 |

## ポイント1: 同期処理と非同期処理
MLサービスでは即座に結果を返してくるもの(同期処理)と、「ジョブ」というかたちでAWS側にしばらく処理を任せるもの(非同期処理)の2種類があります。

- 同期処理の例
    - Rekognition の オブジェクトとシーンの検出
    - Comprehend の 感情分析
- 非同期処理の例
    - Rekognition の ビデオ分析でのテキスト検出
    - Transcribe の テキスト変換

## ポイント2: S3との連携が多い
MLサービスに限った話ではないですが、AWSのサービスの多くはS3(Amazon Simple Storage Service)との連携が多いです。

例えば、なにかの動画データをRekognitionで分析する場合を考えます。 このとき、動画データを直接送るのではなく、S3にある動画データの場所(
オブジェクトのURI)を指定するかたちでプログラムに依頼します。

### S3(Amazon Simple Storage Service)

- **S**imple **S***torage **S**ervice と Sが3つあるので、S3と呼ぶ
- クラウドストレージサービス(GoogleDriveやDropboxなどと同じタイプのサービス)
- バケット(Bucket)という単位で管理する
- 各バケットに格納するデータは、オブジェクトと呼ぶ
- S3URI: S3のバケットやオブジェクトの場所を表す情報

## ポイント3: JSONの理解
APIからサービスを呼び出した場合、多くは**JSON**という形式のテキスト情報が手に入ります。
(画像データや音声データが直接返ってくるわけではありません)

### JSON(JavaScript Object Notation)

- テキストファイルのデータフォーマットの1つ → **ただのテキストファイル**なので、どんなプログラムからでも扱える！
    - テキストファイルのフォーマットの仲間としては、csvやtsvなどがある
    - しっかり説明
      → [JSON データの操作 - ウェブ開発を学ぶ | MDN](https://developer.mozilla.org/ja/docs/Learn/JavaScript/Objects/JSON)
    - 簡易な説明
      → [【超ざっくり解説シリーズ４】 データフォーマットとは？XML、JSON、CSVの違いや特徴についてわかりやすく解説するよ｜とよもも｜note](https://note.com/toyomomo/n/nc4ad516aa32c)\
- JSONは機械可読しやすい == ルールが決まっているのでプログラムで解釈しやすい！
- WebAPIのやりとりでは最も利用されているフォーマット

#### JSONの例その1

かんたんなJSON例を示します。

```json
{
  "name": "John Smith",
  "age": 33
}
```

#### JSONの例その2
もう少し複雑なJSONの例を示します

- 階層構造も表現できる
- **CSVやExcelなどは階層構造を表現しにくい**

```json
{
  "teamName": "Powers",
  "members": [
    {
      "name": "Bob",
      "age": 29,
      "skills": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Tom",
      "age": 39,
      "skills": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Ken",
      "age": 1000000,
      "skills": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

### Rekognitionを利用したときのJSONレスポンス
マネジメントコンソール上で、 「オブジェクトとシーンの検出」を行うと、次のような結果が得られます。

<img width="720" alt="image.png (1.4 MB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/17/21054/ed87bfe0-cfb8-476d-806c-5f0956f3929f.png">


同じことをプログラムから試すと、次のようなJSONが返ってきます。
(しつこいですが、JSONは単なるテキストです)

JSONは長くて人間には見づらい部分がありますが、同じ情報を持っていることがわかるでしょうか？

プログラムから扱う場合は、このJSONから必要となる情報を自力で取得して、求めるかたちに加工する必要があります(慣れは必要ですが、実はそこまで難しくはないです)
。

```json
{
  "LabelModelVersion": "2.0",
  "Labels": [
    {
      "Confidence": 97.14922332763672,
      "Instances": [
        {
          "BoundingBox": {
            "Height": 0.8138601779937744,
            "Left": 0.13302530348300934,
            "Top": 0.18296340107917786,
            "Width": 0.8167757391929626
          },
          "Confidence": 97.14922332763672
        }
      ],
      "Name": "Dog",
      "Parents": [
        {
          "Name": "Pet"
        },
        {
          "Name": "Canine"
        },
        {
          "Name": "Animal"
        },
        {
          "Name": "Mammal"
        }
      ]
    },
    {
      "Confidence": 97.14922332763672,
      "Instances": [],
      "Name": "Canine",
      "Parents": [
        {
          "Name": "Mammal"
        },
        {
          "Name": "Animal"
        }
      ]
    },
    {
      "Confidence": 97.14922332763672,
      "Instances": [],
      "Name": "Pet",
      "Parents": [
        {
          "Name": "Animal"
        }
      ]
    },
    {
      "Confidence": 97.14922332763672,
      "Instances": [],
      "Name": "Mammal",
      "Parents": [
        {
          "Name": "Animal"
        }
      ]
    },
    {
      "Confidence": 97.14922332763672,
      "Instances": [],
      "Name": "Animal",
      "Parents": []
    },
    {
      "Confidence": 96.78888702392578,
      "Instances": [],
      "Name": "Poodle",
      "Parents": [
        {
          "Name": "Dog"
        },
        {
          "Name": "Pet"
        },
        {
          "Name": "Canine"
        },
        {
          "Name": "Animal"
        },
        {
          "Name": "Mammal"
        }
      ]
    }
  ],
  "ResponseMetadata": {
    "HTTPHeaders": {
      "connection": "keep-alive",
      "content-length": "870",
      "content-type": "application/x-amz-json-1.1",
      "date": "Wed, 03 Feb 2021 02:21:57 GMT",
      "x-amzn-requestid": "9a5cdb3d-5f4b-4db3-8221-0302e24c13f5"
    },
    "HTTPStatusCode": 200,
    "RequestId": "9a5cdb3d-5f4b-4db3-8221-0302e24c13f5",
    "RetryAttempts": 0
  }
}
```

## ポイント4: SDKの存在
プログラムからAWSのサービスを呼び出すという説明をしていますが、実際にそのプログラムをゼロから書くのは大変です。

そこで、AWSのSDKを使いましょう。を公開しています。 SDK(Software Development Kit)
とは、開発用の便利ツールのことで、ざっくりいえば、ラクにAWSのサービスを利用できるライブラリです。

各種プログラミング言語用のSDKがあり、Pythonでは `boto3` というSDKが公開されています。
