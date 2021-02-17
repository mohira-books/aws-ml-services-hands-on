from pprint import pprint

import boto3


def main():
    client = boto3.client('comprehend', region_name='ap-northeast-1')

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
