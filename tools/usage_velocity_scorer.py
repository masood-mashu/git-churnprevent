"""
usage_velocity_scorer.py - Computes rolling 14-day user active session velocity compared to previous period
"""
import sys
import json


def score_usage_velocity(velocity_json: str):
    import json
    data = json.loads(velocity_json) if isinstance(velocity_json, str) else velocity_json
    curr = data.get("current_wau", 100)
    prev = data.get("previous_wau", 100)
    pct_change = round(((curr - prev) / max(prev, 1)) * 100, 1)
    is_risk = pct_change < -30.0
    return {"pct_change": pct_change, "churn_risk": is_risk, "status": "CHURN_RISK_HIGH" if is_risk else "CHURN_RISK_LOW"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "usage-velocity-scorer"}))
