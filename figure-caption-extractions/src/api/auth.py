from fastapi import Header, HTTPException, Depends
from src.config.config_loader import load_config

config = load_config()

def get_api_key(x_api_key: str = Header(...)):
    if x_api_key != config.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key