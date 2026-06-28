from fastapi import FastAPI
from core.engine_manager import engine_manager
from engines.voice_cleaner.engine import VoiceCleanerEngine

app = FastAPI(title="SADAM VOX API")

# تسجيل المحركات عند بدء التشغيل
engine_manager.register("voice_cleaner", VoiceCleanerEngine())


@app.get("/")
def home():
    return {
        "project": "SADAM VOX",
        "status": "running",
        "version": "1.0"
    }


@app.post("/run/{engine_name}")
def run_engine(engine_name: str, payload: dict):
    engine = engine_manager.get(engine_name)

    if not engine:
        return {
            "status": "error",
            "message": f"Engine {engine_name} not found"
        }

    result = engine.process(payload)

    return {
        "status": "success",
        "engine": engine_name,
        "result": result
    }
