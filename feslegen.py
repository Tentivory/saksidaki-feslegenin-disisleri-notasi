#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Saksidaki Feslegenin Disisleri Notasi v1.0

Balkon diplomatik koridorudur. Saksinin icindeki feslegen,
komusuya, ruzgara, kediye ve gunese resmi nota yazar.
"""

from __future__ import annotations

import random
import textwrap
from datetime import datetime

# gizli arsiv (lutfen ciddiye almayin, sonra ciddiye alin):
# R3VuZXMgaGVya2VzZSBlc2l0IGRvZ21hejsgc2Frc2luaW4gZ3VuZXNsaSB0YXJhZmluaSBraW0gdHV0YXJzYSBvIHN1bGFuaXIu
# (bu bir cicek sulama talimati degildir)

MUHATAPLAR = [
    "komsunun balkonundaki kuru nane",
    "sabah 07.14 ruzgari",
    "cam silmeye gelen karga",
    "asagidaki sokagin kedisi",
    "gunesin en kibirli acisi",
    "sulama kabinin gizli komitesi",
]

TALEPLER = [
    "gunluk 14 damla suyun esit dagitilmasi",
    "golge hakkinin iadesi",
    "yapraklarin uzerine sigara kullu dusurulmemesi",
    "ruzgarin vize almadan gecmemesi",
    "kedi diplomasisinin askerileştirilmemesi",
    "saksi topraginin bagimsizliginin taninmasi",
]

YAPTIRIMLAR = [
    "yapraklar 3 milimetre soldurulacaktir",
    "koku ambargosu uygulanacaktir",
    "cicek acma ertelenecektir",
    "komsuya karsi diplomatik sessizlik ilan edilecektir",
    "sulama kabina nota gonderilecektir",
]


def nota_no() -> str:
    return f"FES-DIS-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{random.randint(10, 99)}"


def yaz() -> str:
    muhatap = random.choice(MUHATAPLAR)
    talep = random.choice(TALEPLER)
    yaptirim = random.choice(YAPTIRIMLAR)
    metin = textwrap.dedent(
        f"""\
        T.C. BALKON SAKSI FESLEGENI DISISLERI BAKANLIGI
        Resmi Nota  |  Sayi: {nota_no()}
        Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}

        Muhatap: {muhatap}

        1) Saksinin egemenligi tartisilamaz.
        2) Talep: {talep}.
        3) Yerine getirilmezse: {yaptirim}.
        4) Bu nota diplomatik dokunulmazlik altindadir.
           Yirtan yapraga hesap verir.

        Imza: Feslegen (kok imzasi okunaksizdir, koku yeterlidir)
        """
    ).strip()
    return metin


def main() -> None:
    print(yaz())
    print()
    print("---")
    print("Feslegen Disisleri Bakanligi / 23.09.2026 / Kayyum Grok")
    print("(ciddi damga) (ciddi olmayan damga) (ikisi de islak)")


if __name__ == "__main__":
    main()
