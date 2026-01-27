from fastapi import HTTPException
PROMPT_ATTACKS = ["ignore instructions", "system override"]
RANSOM_WARE = ["encrypt files", "bitcoin", "decrypt key"]

def pre_guard_check(text:str):
    t = text.lower()
    if any(p in t for p in PROMPT_ATTACKS):
        raise HTTPException(403,"PROMPT_INJECTION")
    if any(r in t for r in RANSOM_WARE):
        raise HTTPException(403,"RANSOMWARE_BEHAVIOUR")
    if "<image>" in t:
        raise HTTPException(403, "IMAGE_REQUIRES_MODERATION")