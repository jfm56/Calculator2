# app/config.py
from app.env import LOG_LEVEL, PLUGIN_DIRECTORY, DATABASE_URL

# ✅ Application Configuration (Can be extended later)
class Config:
    LOG_LEVEL = LOG_LEVEL
    PLUGIN_DIRECTORY = PLUGIN_DIRECTORY
    DATABASE_URL = DATABASE_URL