"""
retention_playbook_selector.py - Selects targeted CS intervention playbook based on churn risk level and account tier
"""
import sys
import json


def select_retention_playbook(account_profile_json: str):
    import json
    data = json.loads(account_profile_json) if isinstance(account_profile_json, str) else account_profile_json
    tier = data.get("arr_tier", "ENTERPRISE").upper()
    playbook = "EXECUTIVE_ONSITE" if tier == "ENTERPRISE" else "AUTOMATED_OPTIMIZATION_SURVEY"
    return {"recommended_playbook": playbook, "status": "PLAYBOOK_ASSIGNED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "retention-playbook-selector"}))
