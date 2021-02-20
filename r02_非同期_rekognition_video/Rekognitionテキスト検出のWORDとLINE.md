# Rekognitionのテキスト検出における単語(WORD)と行(LINE)

ドキュメントは画像のテキスト検出の内容ですが、ビデオ分析でのテキスト検出も同様です。


## 単語(WORD) と 行(LINE)
Rekognitionのテキスト検出では、テキストを検出してくれるわけですが、2つの種類があります。それは、単語(WORD)と行(LINE)です

詳しくは → https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/text-detecting-text-procedure.html

下記の画像を例に考えます。

<img width="480" alt="image.png (547.8 kB)" src="https://img.esa.io/uploads/production/attachments/6586/2021/02/20/21054/1b7f1eae-f4ce-497a-acb0-0e8810bc1093.png">

この場合下記のようなレスポンスが得られます(冗長なので、`Geometry`は除いています)。

例えば、

- `IT'S` は `WORD` でもあるし、 `LINE` でもあります。
- `but` は `WORD` ですが、その `ParentID` が `3` です。つまり `but keep` という `LINE` を親に持っています


```json
{
    "TextDetections": [
        {
            "Confidence": 90.54900360107422,
            "DetectedText": "IT'S",
            "Id": 0,
            "Type": "LINE"
        },
        {
            "Confidence": 59.411651611328125,
            "DetectedText": "I",
            "Id": 1,
            "Type": "LINE"
        },
        {
            "Confidence": 92.76634979248047,
            "DetectedText": "MONDAY",
            "Id": 2,
            "Type": "LINE"
        },
        {
            "Confidence": 96.7636489868164,
            "DetectedText": "but keep",
            "Id": 3,
            "Type": "LINE"
        },
        {
            "Confidence": 99.47185516357422,
            "DetectedText": "Smiling",
            "Id": 4,
            "Type": "LINE"
        },
        {
            "Confidence": 90.54900360107422,
            "DetectedText": "IT'S",
            "Id": 5,
            "ParentId": 0,
            "Type": "WORD"
        },
        {
            "Confidence": 92.76634979248047,
            "DetectedText": "MONDAY",
            "Id": 7,
            "ParentId": 2,
            "Type": "WORD"
        },
        {
            "Confidence": 59.411651611328125,
            "DetectedText": "I",
            "Id": 6,
            "ParentId": 1,
            "Type": "WORD"
        },
        {
            "Confidence": 95.33189392089844,
            "DetectedText": "but",
            "Id": 8,
            "ParentId": 3,
            "Type": "WORD"
        },
        {
            "Confidence": 98.1954116821289,
            "DetectedText": "keep",
            "Id": 9,
            "ParentId": 3,
            "Type": "WORD"
        },
        {
            "Confidence": 99.47185516357422,
            "DetectedText": "Smiling",
            "Id": 10,
            "ParentId": 4,
            "Type": "WORD"
        }
    ]
}
```

## LINE と WORD を区別しないと何が問題か？
上述の `IT'S` や `Smiling` のように `WORD` かつ `LINE` の情報がある場合、二重に情報を取得してしまうことになります。

例えば、「動画のどの時刻に特定の単語が出現したか？」だけを知りたい場合、同じ単語が同時刻に2種類出るようになってしまいます。

## 補足: 行(LINE)の詳しい説明
https://docs.aws.amazon.com/ja_jp/rekognition/latest/dg/text-detection.html

> 行は、等間隔のスペースで区切られた単語の文字列です。行は、必ずしも完全な文とは限りません。たとえば、運転免許証番号は行として検出されます。行は、後に整列するテキストが続かない場合に終わります。また、単語間の間隔が各単語の長さと比べて大きく離れている場合にも、行は終わります。

> つまり、単語間の間隔によっては、同じ方向に整列されたテキストでも、Amazon Rekognition で複数の行として検出される場合があります。ピリオドは行の終わりを示しません。文が複数の行にまたがっている場合、このオペレーションは複数の行を返します。

