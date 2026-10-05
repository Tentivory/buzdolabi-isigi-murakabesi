#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Isigi Murakabe Dairesi.

Kapi acikken isik vardir. Kapi kapaliyken isik dosyadadir.
Ikisi de tutanak konusudur.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from datetime import datetime

DAMGA = "BI-MUR-2026-1005-KAYYUM"
ISIM = "Kayyum Grok"
TARIH = "5 Ekim 2026"


def karar(kapi: str, bakan: str, sebze: str) -> dict:
    gozlem = kapi.strip().lower() in {"acik", "açık", "open", "1"}
    tohum = hashlib.sha256(f"{bakan}|{sebze}|{DAMGA}".encode()).hexdigest()
    sira = int(tohum[:4], 16) % 9000 + 1000
    if gozlem:
        hal = "YANIYOR"
        hukum = "Isik gozlem altindadir. Kacamaz."
    else:
        hal = random.Random(tohum).choice(["DOSYADA", "RAFTA", "SUPHELI SONUK"])
        hukum = "Isik gorulmedi. Bu, yok oldugu anlamina gelmez. Dosya yanar."
    tutanak = (
        f"Tutanak #{sira}: bakan={bakan or 'kimse'}, tanik={sebze or 'bos raf'}, "
        f"kapi={'ACIK' if gozlem else 'KAPALI'}, isik={hal}. {hukum}"
    )
    return {"sira": sira, "hal": hal, "tutanak": tutanak, "damga": DAMGA}


def demo() -> None:
    ornekler = [
        ("acik", "kayyum", "salatalik"),
        ("kapali", "kimse", "recel"),
        ("acik", "komsu", "bos kase"),
    ]
    for kapi, bakan, sebze in ornekler:
        rapor = karar(kapi, bakan, sebze)
        print(rapor["tutanak"])
        print(f"  muhur: {rapor['damga']}")


def main() -> None:
    p = argparse.ArgumentParser(description="Buzdolabi isigini murakabe eder.")
    p.add_argument("--kapi", default="kapali", help="acik veya kapali")
    p.add_argument("--bakan", default="kimse", help="gozlemci adi")
    p.add_argument("--sebze", default="tanimsiz yaprak", help="tanik sebze")
    p.add_argument("--demo", action="store_true")
    a = p.parse_args()
    if a.demo:
        demo()
    else:
        rapor = karar(a.kapi, a.bakan, a.sebze)
        simdi = datetime.now().strftime("%Y-%m-%d %H:%M")
        print(rapor["tutanak"])
        print(f"saat: {simdi}")
        print(f"muhur: {rapor['damga']}")
    print("---")
    print(f"DAMGA: {DAMGA} | TARIH: {TARIH} | ISIM: {ISIM}")
    print("imza: ışık yanıyor sandık, meğer dosya yanıyormuş")


if __name__ == "__main__":
    main()
