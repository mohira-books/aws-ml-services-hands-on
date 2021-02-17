# [Amazon Transcribe（音声をテキストに変換する機能を簡単に追加）| AWS](https://aws.amazon.com/jp/transcribe/?c=ml&sec=srv)

## 準備

- S3バケットを準備する
- 変換したいファイル(音声や動画)を用意したバケットに保存する
- 重要: S3のオブジェクトURL を取得する
    - ex: `https://your-bucekt-name.s3-ap-northeast-1.amazonaws.com/sample.mp4`

## SDK
### Step1. ジョブの作成

```python
from pprint import pprint

import boto3
from botocore.exceptions import ClientError


def main():
  client = boto3.client('transcribe', region_name='ap-northeast-1')

  job_name = 'YOUR-JOB-NAME'

  # ex: https://your-bucket-name.s3-ap-northeast-1.amazonaws.com/WhatIsTranscribe.mp4
  media_object_uri = 'YOUR-OBJECT_URI'

  try:
    response = client.start_transcription_job(TranscriptionJobName=job_name,
                                              LanguageCode='ja-JP',
                                              MediaFormat='mp4',
                                              Media={
                                                'MediaFileUri': media_object_uri})

    print('Jobの作成に成功しました！')
    pprint(response)

  except ClientError as e:
        print('エラーが起きました！')
        pprint(e.response)
        exit()


if __name__ == '__main__':
    main()

```

### Step2. 変換結果の取得

```python
import textwrap

import boto3
import requests


def display_transcript(transcribe_job_response):
    transcript_file_url = transcribe_job_response['TranscriptionJob']['Transcript']['TranscriptFileUri']

    results = requests.get(transcript_file_url).json()['results']

    transcripts = results['transcripts']

    for transcript in transcripts:
        print(textwrap.fill(transcript['transcript'], 70))


def main():
  client = boto3.client('transcribe', region_name='ap-northeast-1')

  job_name = 'YOUR-JOB-NAME'

  transcribe_job_response = client.get_transcription_job(
    TranscriptionJobName=job_name)
  transcription_job_status = transcribe_job_response['TranscriptionJob'][
    'TranscriptionJobStatus']

  if transcription_job_status == 'COMPLETED':
    display_transcript(transcribe_job_response)
  else:
    print(transcribe_job_response)


if __name__ == '__main__':
  main()

```

## クリーンアップ

- S3バケットの削除
- Transcribeのジョブの削除

### ジョブの一括削除

- AWS CLIが必要

```
$ aws transcribe list-transcription-jobs | jq -r '.TranscriptionJobSummaries[].TranscriptionJobName'  | xargs -I {} aws transcribe delete-transcription-job --transcription-job-name={}
```