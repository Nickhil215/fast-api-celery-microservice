from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery.result import AsyncResult
from app.tasks import *
from app.app import celery

app = FastAPI()

@app.get("/")
def default():
    return "Welcome to Report Service"

@app.get("/health")
def health():
    return JSONResponse({"state": "healthy"})

@app.post("/report")
def generate_report():
    async_result = report.delay()
    return JSONResponse({"report_id": async_result.id})

@app.get("/report/{report_id}")
def get_report(report_id: str):
    res = AsyncResult(report_id, app=celery)
    return JSONResponse({"id": res.id, "result": res.result})
