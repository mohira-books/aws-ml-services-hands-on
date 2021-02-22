from pathlib import Path

import boto3
from mypy_boto3_s3 import S3ServiceResource
from mypy_boto3_s3.service_resource import Bucket


def upload_png_from_dir(bucket: Bucket, png_files_dir: Path) -> None:
    for p in sorted(png_files_dir.glob('*.png')):
        with p.open(mode='rb') as f:
            bucket.put_object(Key=f'custom_label/{p.parent}/{p.name}', Body=f.read())


def main():
    bucket_name = '2021-02-15-bob-bucket'

    s3: S3ServiceResource = boto3.resource('s3', region_name='ap-northeast-1')
    bucket: Bucket = s3.Bucket(bucket_name)

    project_dir = Path(__file__).parent
    with_qr_dir = project_dir / 'with_qr'
    without_qr_dir = project_dir / 'without_qr'

    upload_png_from_dir(bucket, with_qr_dir)
    upload_png_from_dir(bucket, without_qr_dir)


if __name__ == '__main__':
    main()
