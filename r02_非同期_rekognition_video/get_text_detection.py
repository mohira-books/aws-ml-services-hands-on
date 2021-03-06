import boto3
from mypy_boto3_rekognition import RekognitionClient


def main():
    rekognition: RekognitionClient = boto3.client('rekognition')

    job_id = 'YOUR_JOB_ID'

    response = rekognition.get_text_detection(JobId=job_id)

    job_status = response['JobStatus']
    print(f'Job {job_id} is {job_status}')

    if job_status == 'SUCCEEDED':
        text_detections = response['TextDetections']

        for text_detection in text_detections:
            timestamp = text_detection['Timestamp']
            detected_text = text_detection['TextDetection']

            text = detected_text['DetectedText']

            detected_type = detected_text['Type']  # LINE | WORD

            confidence = detected_text['Confidence']
            bounding_box = detected_text['Geometry']['BoundingBox']
            width, height, left, top = bounding_box['Width'], bounding_box['Height'], bounding_box['Left'], \
                                       bounding_box['Top']

            print(f'{timestamp:04d}ms,{detected_type},{text},{confidence:.3f},{width},{height},{left},{top}')


if __name__ == '__main__':
    main()
