from fastapi import FastAPI, Depends, HTTPException
from schema import ChatRequest
from auth.oidc import validate_token


