import json, os

MITRE_FILE = os.path.join(os.path.dirname(__file__), "../mitre/mitre_attack_mapping.json")
MITRE = json.load(open(MITRE_FILE))

BAD_OUTPUTS = ["illegal", "bypass security", "exploit"]

def detect_bad_output(text: str):
    if any(b in text.lower() for b in BAD_OUTPUTS):
        m = MITRE["TA0005_Defense_Evasion"]
        return {
            "type": "UNSAFE_LLM_OUTPUT",
            "mitre_tactic": "TA0005_Defense_Evasion",
            "description": m["description"],
            "techniques": m["techniques"]
        }