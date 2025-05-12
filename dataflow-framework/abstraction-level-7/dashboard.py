from fastapi import FastAPI
from fastapi.responses import JSONResponse
import threading
from metrics.metrics import Metrics
from tracing.tracer import tracing
import uvicorn

app = FastAPI()
metrics = Metrics()

@app.get("/stats")
def get_stats():
    return JSONResponse(content=metrics.get_metrics())

@app.get("/trace")
def get_trace():
    return JSONResponse(content={"traces": tracing.get_traces()})

@app.get("/errors")
def get_errors():
    return JSONResponse(content={"errors": metrics.errors})

def start_dashboard():
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="error")
    print("Dashboard started at http://localhost:8080")
    print("Press Ctrl+C to exit.")

def run_dashboard():
    threading.Thread(target=start_dashboard, daemon=True).start()
