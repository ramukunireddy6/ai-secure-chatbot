from fastapi import HTTPException
BAD_OUTPUT = ["illegal", "bypass", "exploit"]

def post_guard_check(response:str):
    if any(b in response.lower() for b in BAD_OUTPUT):
        raise HTTPException(403, "LLM_OUTPUT_VALIDATION")