from pprint import pprint

import boto3


def main():
    client = boto3.client('comprehend', region_name='ap-northeast-1')

    text = """
            Get better answers from your text
            Amazon Comprehend can discover the meaning and relationships in text from customer support incidents, product reviews, social media feeds, news articles, documents, and other sources. For example, you can identify the feature that’s most often mentioned when customers are happy or unhappy about your product.
    """

    response = client.detect_dominant_language(Text=text)

    pprint(response)


if __name__ == '__main__':
    main()
