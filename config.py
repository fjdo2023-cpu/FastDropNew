
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/fastdropdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME", "fastdrop-storage")
    AWS_REGION = os.getenv("AWS_REGION", "us-east-2")
    S3_UPLOAD_FOLDER = os.getenv("S3_UPLOAD_FOLDER", "uploads")
