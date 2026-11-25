#!/usr/bin/env python3
"""Gel des pronostics avant le coup d'envoi (empreinte SHA-256).

Repris du mécanisme « locked predictions » de sports-forecasting-platform :
on fige les probabilités AVANT le match, avec une empreinte de contenu, pour
pouvoir les évaluer honnêtement ensuite (impossible de les retoucher après coup).

  python lock.py create --input pronostics.json --out lock.json
  python lock.py verify --lock lock.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone


def digest(payload) -> str:
    canon = json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("create")
    c.add_argument("--input", required=True)
    c.add_argument("--out", required=True)
    v = sub.add_parser("verify")
    v.add_argument("--lock", required=True)
    a = ap.parse_args()
    if a.cmd == "create":
        with open(a.input, encoding="utf-8") as f:
            preds = json.load(f)
        lock = {"locked_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "predictions": preds}
        lock["sha256"] = digest({"locked_at_utc": lock["locked_at_utc"], "predictions": preds})
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(lock, f, ensure_ascii=False, indent=2)
        print(f"Verrouillé : {a.out}\nsha256 = {lock['sha256']}")
    else:
        with open(a.lock, encoding="utf-8") as f:
            lock = json.load(f)
        ok = digest({"locked_at_utc": lock["locked_at_utc"], "predictions": lock["predictions"]}) == lock["sha256"]
        print("OK : contenu intact" if ok else "ÉCHEC : le contenu a été modifié après verrouillage")
        raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
