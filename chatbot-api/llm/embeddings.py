from bedrock import bedrock_embed
from openai_client import openai_embed

def embed(text: str):
    """Unified embedding interface with fallback"""
    try:
        return bedrock_embed(text)
    except Exception:
        return openai_embed(text)