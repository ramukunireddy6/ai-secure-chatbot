from fastapi import FastAPI, Depends, HTTPException
from auth.oidc import validate_token
from guardrails.pre_guard import  pre_guard_check
from guardrails.post_guard import post_guard_check
from agents.google_adk_agent import run_agent

app = FastAPI()

@app.post("/chat")
async def chat(request: dict,user = Depends(validate_token)):
    prompt = request["query"]

    response = await run_agent(prompt,user)

    post_guard_check(response)

    return  {"response": response}


