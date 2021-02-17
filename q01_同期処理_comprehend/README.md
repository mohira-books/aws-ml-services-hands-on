# [Amazon Comprehend（テキストのインサイトや関係性を検出）| AWS](https://aws.amazon.com/jp/comprehend/?c=ml&sec=srv)

## 演習: マネジメントコンソール

- 他の機能はいずれ
- 重要なのは、「すぐに試せること」

### 演習1: 言語の判定 & 感情分析

```text
大人になって、新しいことをしっかり学ぶ機会を作ることはなかなか難しいことだと考えております。
せっかくの機会ですので、是非、学びを進めるにあたっては「こんなことができればいいなーっ」というワクワク感や、「将来的にこういう風になりたいな」っていう目的や気持ちを持ちながら、楽しく受講をいただければと思っております。
```

```text
Get better answers from your text
Amazon Comprehend can discover the meaning and relationships in text from customer support incidents, product reviews, social media feeds, news articles, documents, and other sources. For example, you can identify the feature that’s most often mentioned when customers are happy or unhappy about your product.
```

### 演習2: 好きな文章で試してみる

- 自由にやってみよう

## 演習: SDKを利用する
### 演習1: 言語の判定

```python
from pprint import pprint

import boto3


def main():
    client = boto3.client('q01_同期処理_comprehend', region_name='ap-northeast-1')

    text = """
            Get better answers from your text
            Amazon Comprehend can discover the meaning and relationships in text from customer support incidents, product reviews, social media feeds, news articles, documents, and other sources. For example, you can identify the feature that’s most often mentioned when customers are happy or unhappy about your product.
    """

    response = client.detect_dominant_language(Text=text)

    pprint(response)


if __name__ == '__main__':
    main()
```

### 演習2: 感情分析

```python
from pprint import pprint

import boto3


def main():
    client = boto3.client('q01_同期処理_comprehend', region_name='ap-northeast-1')

    text = """
        大人になって、新しいことをしっかり学ぶ機会を作ることはなかなか難しいことだと考えております。
        せっかくの機会ですので、是非、学びを進めるにあたっては「こんなことができればいいなーっ」というワクワク感や、「将来的にこういう風になりたいな」っていう目的や気持ちを持ちながら、楽しく受講をいただければと思っております。
    """

    response = client.detect_sentiment(
        Text=text,
        LanguageCode='ja'
    )
    pprint(response)


if __name__ == '__main__':
    main()
```




