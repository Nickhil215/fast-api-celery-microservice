
from fastapi import FastAPI
from celery import Celery
import os

app = FastAPI()

app.celery_broker_url = os.getenv("CELERY_BROKER_URL")
app.celery_result_backend = os.getenv("CELERY_RESULT_BACKEND")
app.secret_key = os.getenv("SECRET_KEY")

celery = Celery(
    __name__,
    backend=app.celery_result_backend,
    broker=app.celery_broker_url
)

celery.conf.update({
    "CELERY_BROKER_URL": app.celery_broker_url,
    "RESULT_BACKEND": app.celery_result_backend,
    "SECRET_KEY": app.secret_key
})
