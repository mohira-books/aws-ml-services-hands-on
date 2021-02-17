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

    transcribe_job_response = client.get_transcription_job(TranscriptionJobName=job_name)
    transcription_job_status = transcribe_job_response['TranscriptionJob']['TranscriptionJobStatus']

    if transcription_job_status == 'COMPLETED':
        display_transcript(transcribe_job_response)
    else:
        print(transcribe_job_response)


if __name__ == '__main__':
    main()
