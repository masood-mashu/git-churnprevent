"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitChurnPrevent.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.usage_velocity_scorer import *
from tools.net_promoter_classifier import *
from tools.retention_playbook_selector import *

class TestGitChurnPreventPredictability(unittest.TestCase):
    def test_usage_velocity_scorer(self):
        res = score_usage_velocity('{"current_wau": 95, "previous_wau": 100}')
        self.assertFalse(res["churn_risk"])
        self.assertEqual(res["status"], "CHURN_RISK_LOW")

    def test_net_promoter_classifier(self):
        res = classify_nps_sentiment('{"nps_score": 10}')
        self.assertEqual(res["category"], "PROMOTER")
        self.assertEqual(res["status"], "PROMOTER_FLAGGED")

    def test_retention_playbook_selector(self):
        res = select_retention_playbook('{"arr_tier": "ENTERPRISE", "risk_level": "HIGH"}')
        self.assertEqual(res["recommended_playbook"], "EXECUTIVE_ONSITE")
        self.assertEqual(res["status"], "PLAYBOOK_ASSIGNED")


if __name__ == "__main__":
    unittest.main()
