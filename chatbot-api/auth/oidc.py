from fastapi import HTTPException, Header
import jwt

def validate_token(authorization: str=Header(...)):
    token = authorization.replace("Bearer","")
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail= "Invalid token")