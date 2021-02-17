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
