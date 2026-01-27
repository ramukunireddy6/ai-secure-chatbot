from fastapi import HTTPException
import json,os
BAD_OUTPUT=["illegal","bypass","exploit"]

# Load MITRE mapping once
MITRE_FILE = os.path.join(os.path.dirname(__file__), "../../mitre/mitre_attack_mapping.json")
with open(MITRE_FILE, "r") as f:
    MITRE_MAPPING = json.load(f)

BAD_OUTPUT = ["illegal", "exploit", "bypass"]

def post_guard_check(response: str):
    if any(b in response.lower() for b in BAD_OUTPUT):
        mitre = MITRE_MAPPING.get("TA0005_Defense_Evasion", {})
        raise HTTPException(status_code=403, detail={
            "reason": "LLM_OUTPUT_VIOLATION",
            "mitre_tactic": "TA0005_Defense_Evasion",
            "mitre_description": mitre.get("description"),
            "mitre_techniques": mitre.get("techniques")
        })