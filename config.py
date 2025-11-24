
import os
class Config:
    SECRET_KEY=os.getenv("SECRET_KEY","dev")
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    AWS_BUCKET_NAME=os.getenv("AWS_BUCKET_NAME")
    AWS_REGION=os.getenv("AWS_REGION")
