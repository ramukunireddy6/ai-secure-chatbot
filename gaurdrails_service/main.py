from fastapi import FastAPI,Request
from detectors.pre_guard import pre_guard_check
from metrics.prometheus import init_metrics,record_block

app = FastAPI(title="AI GUARDRAILS SERVICE")

init_metrics()

@app.post("/authorize")
async def authorize(request: Request):
    body = await request.json()
    prompt = body.get("prompt","")

    for detector in pre_guard_check:
        result = detector(prompt)
        if result:
            record_block(result["mitre_tactic"])
            return {
                "allowed": False,
                "reason": result
            }

    return {"allowed":True}