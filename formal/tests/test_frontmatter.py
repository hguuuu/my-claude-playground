"""Frontmatter validator — the mechanical half of the study/RULES constitution.

v1 scope (stub grows with the corpus):
  1. Every YAML frontmatter `id:` in the repo is unique.
  2. Study notes of registered types carry their required fields.
  3. Controlled vocabularies are respected where present.
Deferred (TODO as records accumulate): two-way link resolution
(study→corpus citation targets exist; corpus id stability), basis-tag
presence on tradition-claims, derived-field ban.

No external deps: frontmatter is parsed line-wise for top-level scalar
keys only, which is all v1 checks need.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", ".obsidian", "views", "node_modules"}
TEMPLATE_DIRS = {"templates"}  # templates carry placeholder ids on purpose

REQUIRED_FIELDS = {
    "daily-draw": {"date", "system"},
    "prediction": {"made", "resolve_by", "claim", "status"},
    "case": {"case_type", "systems"},
}
VOCAB = {
    "status": {  # prediction status only; matched per-type below
        "prediction": {"open", "verified-correct", "verified-wrong", "void"},
    },
    "case_type": {"命例", "historical-event", "fiction", "friend-reading", "own-question"},
}


def iter_notes():
    for path in ROOT.rglob("*.md"):
        parts = set(path.relative_to(ROOT).parts)
        if parts & SKIP_DIRS or parts & TEMPLATE_DIRS:
            continue
        yield path


def frontmatter(path):
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    fields = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z_一-鿿][\w一-鿿-]*):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip("\"'")
    return fields


class TestFrontmatter(unittest.TestCase):
    def setUp(self):
        self.notes = {p: frontmatter(p) for p in iter_notes()}

    def test_ids_unique(self):
        seen = {}
        for path, fm in self.notes.items():
            note_id = fm.get("id")
            if not note_id:
                continue
            self.assertNotIn(
                note_id, seen,
                f"duplicate id '{note_id}': {path} and {seen.get(note_id)}")
            seen[note_id] = path

    def test_required_fields(self):
        for path, fm in self.notes.items():
            required = REQUIRED_FIELDS.get(fm.get("type", ""))
            if not required:
                continue
            missing = required - fm.keys()
            self.assertFalse(missing, f"{path}: type {fm['type']} missing {sorted(missing)}")

    def test_controlled_vocab(self):
        for path, fm in self.notes.items():
            if fm.get("type") == "prediction" and "status" in fm:
                self.assertIn(fm["status"], VOCAB["status"]["prediction"],
                              f"{path}: bad prediction status '{fm['status']}'")
            if "case_type" in fm:
                self.assertIn(fm["case_type"], VOCAB["case_type"],
                              f"{path}: bad case_type '{fm['case_type']}'")


if __name__ == "__main__":
    unittest.main()
