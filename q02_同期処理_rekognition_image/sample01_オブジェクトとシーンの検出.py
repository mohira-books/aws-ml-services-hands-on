from pathlib import Path
from pprint import pprint

import boto3
from mypy_boto3_rekognition import RekognitionClient


def main():
    client: RekognitionClient = boto3.client('rekognition', region_name='ap-northeast-1')

    image_file_path = Path(__file__).parent / 'image01.jpg'

    with image_file_path.open(mode='rb') as f:
        bytes_data = f.read()
        response = client.detect_labels(Image={'Bytes': bytes_data})

    pprint(response)

    label_names = [label['Name'] for label in response['Labels']]
    print(f'Label: {label_names}')


if __name__ == '__main__':
    main()
