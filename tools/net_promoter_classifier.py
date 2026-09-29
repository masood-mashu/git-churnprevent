"""
net_promoter_classifier.py - Classifies survey responses into standard NPS categories (Promoter, Passive, Detractor)
"""
import sys
import json


def classify_nps_sentiment(nps_score_json: str):
    import json
    data = json.loads(nps_score_json) if isinstance(nps_score_json, str) else nps_score_json
    score = data.get("nps_score", 9)
    cat = "PROMOTER" if score >= 9 else ("PASSIVE" if score >= 7 else "DETRACTOR")
    return {"category": cat, "score": score, "status": f"{cat}_FLAGGED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "net-promoter-classifier"}))
