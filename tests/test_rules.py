import unittest
from src.rules import fingerprint, prepare_draft, priority, validate_proposal


class RuleTests(unittest.TestCase):
    def test_priority_bands(self):
        self.assertEqual(priority(0, 0), "Low")
        self.assertEqual(priority(1, 1), "Normal")
        self.assertEqual(priority(3, 1), "High")
        self.assertEqual(priority(3, 3), "Urgent")

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            priority(4, 2)
        with self.assertRaises(ValueError):
            priority(True, 2)

    def test_fingerprint_is_repeatable(self):
        self.assertEqual(fingerprint("email", "123", "Follow up"), fingerprint(" EMAIL ", "123", "follow up"))
        self.assertNotEqual(fingerprint("email", "123", "Follow up"), fingerprint("email", "124", "Follow up"))

    def test_prepare_draft_requires_review(self):
        source = {"type": "meeting", "id": "demo-123"}
        task = {"proposal_id": "p1", "title": "Send meeting recap", "urgency": 1, "impact": 2}
        draft = prepare_draft(task, source)
        self.assertEqual(draft["priority"], "Normal")
        self.assertEqual(draft["status"], "pending_review")
        self.assertTrue(draft["review_required"])
        self.assertIsNone(draft["assignee_gid"])

    def test_invalid_status(self):
        draft = prepare_draft({"proposal_id":"a","title":"Send recap","urgency":2,"impact":1}, {"type":"manual","id":"source-a"})
        draft["status"] = "published"
        with self.assertRaises(ValueError):
            validate_proposal(draft)

if __name__ == "__main__":
    unittest.main()
