"""Guard the copied scenarios and repeated-sentence regressions."""

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from noteformats.content_quality import scenario_duplicates, limitation_duplicates, repeated_sentences, content_issues
from build import load_content


class ContentQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = load_content(json.loads((ROOT / "profiles/a5-draft.json").read_text()))

    def test_catalog_has_unique_scenarios_and_no_repeated_sentences(self):
        self.assertEqual(content_issues(self.content), [])

    def test_copied_scenarios_are_detected_even_when_reordered(self):
        content = copy.deepcopy(self.content)
        content["six-cards"]["translations"]["en"]["when"] = list(reversed(content["four-cards"]["translations"]["en"]["when"]))
        self.assertIn(["four-cards", "six-cards"], scenario_duplicates(content)["en"])
        self.assertTrue(any("identical usage scenarios" in issue for issue in content_issues(content)))

    def test_reported_card_counts_and_why_method(self):
        for layout_id, number in (("six-cards", "six"), ("eight-cards", "eight")):
            text = " ".join(self.content[layout_id]["translations"]["en"]["when"]).lower()
            self.assertIn(number, text)
            self.assertNotIn("four workshop questions", text)
        why = self.content["five-why-chain"]["translations"]["en"]
        self.assertIn("why", " ".join(why["when"]).lower())
        self.assertNotIn("borrowing a book", " ".join(why["when"]).lower())
        self.assertEqual(repeated_sentences(why["unsuitable"]), [])
        self.assertTrue(repeated_sentences("Small cells hold short phrases rather than long paragraphs. Small cells hold short phrases rather than long paragraphs."))

    def test_copied_limitations_are_detected(self):
        content = copy.deepcopy(self.content)
        content["causal-chain"]["translations"]["en"]["unsuitable"] = content["frayer"]["translations"]["en"]["unsuitable"]
        self.assertTrue(any(set(ids) == {"causal-chain", "frayer"} for ids in limitation_duplicates(content)["en"]))
        self.assertTrue(any("identical limitations" in issue for issue in content_issues(content)))

    def test_commas_stay_inside_one_numbered_region(self):
        content = copy.deepcopy(self.content)
        example = content["six-cards"]["translations"]["en"]
        self.assertEqual(len(example["example_entries"]), 6)
        self.assertEqual(example["example_entries"][0], "Library, ten seats")
        items = example["example"].split("\n\n", 1)[1].splitlines()
        self.assertEqual(len(items), 6)
        self.assertEqual(items[0], "1. Library, ten seats")
        self.assertTrue(items[-1].startswith("6. "))
        example["example"] = "Entries in region order: " + ", ".join(example["labels"])
        self.assertTrue(any("worked-example entries" in issue for issue in content_issues(content)))


if __name__ == "__main__":
    unittest.main()
