
import boto3,uuid,os
def upload_file_s3(file):
    bucket=os.getenv("AWS_BUCKET_NAME")
    region=os.getenv("AWS_REGION")
    s3=boto3.client("s3",region_name=region)
    key=f"uploads/{uuid.uuid4()}"
    s3.put_object(Bucket=bucket,Key=key,Body=file.read())
    return f"https://{bucket}.s3.{region}.amazonaws.com/{key}"
