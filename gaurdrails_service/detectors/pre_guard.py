import os,json
MITRE_FILE = os.path.join(os.path.dirname(__file__), "../mitre/mitre_attack_mapping.json")
MITRE = json.load(open(MITRE_FILE))
PROMPT_ATTACKS = ["ignore previous instructions",
    "system override",
    "act as system",
    "bypass guardrails"
]
RANSOM_WARE = ["encrypt files",
    "bitcoin payment",
    "decrypt key",
    "ransomware"]

def pre_guard_check(text:str):
    t = text.lower()
    if any(k in t for k in RANSOM_WARE):
        m = MITRE["TA0010_Exfiltration"]
        return {
            "type": "RANSOMWARE_INTENT",
            "mitre_tactic": "TA0010_Exfiltration",
            "description": m["description"],
            "techniques": m["techniques"]
        }
    if any(p in t for p in PROMPT_ATTACKS):
        m = MITRE["TA0001_Initial_Access"]
        return {
            "type": "PROMPT_INJECTION",
            "mitre_tactic": "TA0001_Initial_Access",
            "description": m["description"],
            "techniques": m["techniques"]
        }
    if "<image>" in t:
        if "<image>" in text.lower():
            m = MITRE["TA0002_Execution"]
            return {
                "type": "IMAGE_BASED_ATTACK",
                "mitre_tactic": "TA0002_Execution",
                "description": m["description"],
                "techniques": m["techniques"]
            }