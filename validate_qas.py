import json
import sys
import re

SOURCE_RE = re.compile(r'^[^:]+\.pdf:\d+$|^[^:]+\.pdf:chunk_\d+$', re.IGNORECASE)

def validate_line(obj, lineno):
    errors = []
    if "id" not in obj or not isinstance(obj["id"], str) or not obj["id"].strip():
        errors.append("missing or invalid 'id'")
    if "question" not in obj or not isinstance(obj["question"], str) or not obj["question"].strip():
        errors.append("missing or invalid 'question'")
    if "answer" not in obj or not isinstance(obj["answer"], str) or not obj["answer"].strip():
        errors.append("missing or invalid 'answer'")
    if "sources" in obj:
        if not isinstance(obj["sources"], list):
            errors.append("'sources' must be a list")
        else:
            for s in obj["sources"]:
                if not isinstance(s, str) or not s.strip():
                    errors.append(f"empty/invalid source entry: {s}")
                elif not SOURCE_RE.match(s):
                    errors.append(f"source has unexpected format (expected filename.pdf:page or filename.pdf:chunk_id): {s}")
    if "type" in obj:
        if obj["type"] not in ("question", "operation", "enquiry"):
            errors.append(f"invalid type (must be 'question' or 'operation'): {obj['type']}")
    return errors

def main(path):
    ok = True
    with open(path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            line=line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[LINE {i}] JSON error: {e}")
                ok = False
                continue
            errs = validate_line(obj, i)
            if errs:
                ok = False
                print(f"[LINE {i}] {obj.get('id','<no-id>')} errors:")
                for e in errs:
                    print(f"   - {e}")
    if ok:
        print("Validation OK: all lines passed basic schema checks.")
    else:
        print("Validation FAILED: fix listed issues above.")
        sys.exit(2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_qas.py path/to/qas.jsonl")
        sys.exit(1)
    main(sys.argv[1])