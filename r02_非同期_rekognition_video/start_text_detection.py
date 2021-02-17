from pathlib import Path

import boto3


def main():
    rekognition = boto3.client('rekognition')

    bucket_name = 'YOUR_JOB_BUCKET_NAME'
    movie_file = 'YOUR_OBJECT_KEY'  # オブジェクトのキー名

    # 動画のテキスト検出を開始する
    response = rekognition.start_text_detection(Video={'S3Object': {'Bucket': bucket_name,
                                                                    'Name': movie_file}})
    # あとで利用するので動画ファイル名とジョブIDを記録する
    log_file_path = Path(__file__).parent / 'text_detection_log.txt'

    with log_file_path.open(mode='a') as f:
        line = f"{movie_file},{response['JobId']}\n"
        f.write(line)


if __name__ == '__main__':
    main()
