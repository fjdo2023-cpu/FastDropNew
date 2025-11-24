
import boto3, uuid, os
from flask import current_app

def upload_file_s3(file_obj, filename=None):
    bucket = current_app.config.get("AWS_BUCKET_NAME")
    region = current_app.config.get("AWS_REGION")
    folder = current_app.config.get("S3_UPLOAD_FOLDER", "uploads")

    if not filename:
        ext = file_obj.filename.rsplit(".", 1)[-1] if "." in file_obj.filename else "bin"
        filename = f"{uuid.uuid4()}.{ext}"

    key = f"{folder}/{filename}"

    s3 = boto3.client("s3", region_name=region)
    s3.put_object(Bucket=bucket, Key=key, Body=file_obj.read())

    return f"https://{bucket}.s3.{region}.amazonaws.com/{key}"
