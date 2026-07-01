from fastapi import FastAPI, HTTPException
from core.engine_manager import engine_manager
from engines.voice_cleaner.engine import VoiceCleanerEngine

app = FastAPI(
    title="SADAM VOX API",
    version="1.0.0",
    description="Professional AI Music Studio Backend"
)

# تسجيل المحركات مرة واحدة عند بدء التشغيل
if not engine_manager.exists("voice_cleaner"):
    engine_manager.register(
        "voice_cleaner",
        VoiceCleanerEngine()
    )


@app.get("/")
def home():
    return {
        "name": "SADAM VOX",
        "status": "online",
        "version": "1.0.0"
    }


@app.get("/engines")
def list_engines():
    return {
        "engines": engine_manager.list_engines()
    }


@app.post("/run/{engine_name}")
def run_engine(engine_name: str, payload: dict):

    engine = engine_manager.get(engine_name)

    if engine is None:
        raise HTTPException(
            status_code=404,
            detail=f"Engine '{engine_name}' not found."
        )

    return engine.process(payload)
