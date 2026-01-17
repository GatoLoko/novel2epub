# Created on 29/06/2019
# Copyright (C) 2019 GatoLoko
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import re

from libs import common

Volume = common.Volume

volumes = {
    "1": Volume("1", 1, 100),
    "2": Volume("2", 101, 200),
    "3": Volume("3", 201, 300),
    "4": Volume("4", 301, 400),
    "5": Volume("5", 401, 500),
    "6": Volume("6", 501, 600),
    "7": Volume("7", 601, 700),
    "8": Volume("8", 701, 800),
    "9": Volume("9", 801, 900),
    "10": Volume("10", 901, 1000),
    "11": Volume("11", 1001, 1100),
    "12": Volume("12", 1101, 1200),
    "13": Volume("13", 1201, 1300),
    "14": Volume("14", 1301, 1400),
    "15": Volume("15", 1401, 1500),
    "16": Volume("16", 1501, 1600),
    "17": Volume("17", 1601, 1700),
    "18": Volume("18", 1701, 1800),
    "19": Volume("19", 1801, 1900),
    "20": Volume("20", 1901, 2000),
    "21": Volume("21", 2001, 2100),
    "22": Volume("22", 2101, 2200),
    "23": Volume("23", 2201, 2300),
    "24": Volume("24", 2301, 2400),
    "25": Volume("25", 2401, 2500),
}

origin = "http://www.wuxiaworld.co/Peerless-Martial-God/"
author = "Jing Wu Hen (净无痕)"
cover_file = "Covers/pmg.jpg"
title = "Peerless martial God - Vol"

synopsis_text = """
Lin Feng tried to be the diligent and hard-working good guy. He studied hard,
did his best to make his family proud and not get into trouble, but when he saw
a girl being taken advantage of, he had to intervene. He had been tricked,
sentenced to 10 years in jail and framed for a crime he never committed, all
was lost. If his life was over he would take those who ruined his life with
him.</p>

<p>Suddenly he opens his eyes again. He is not dead, but alive in the body of
the Lin Feng of a different world. This Lin Feng had been killed as trash of
cultivation. This world where the strong had no regard for human life and would
kill freely if they had the strength. Called “trash” and thrown away, with
vengeance in his heart he will rise to new heights opposing the will of heaven
and earth.</p>

<p>“Do not judge others in ignorance within my presence.</p>

<p>Those who think to harm someone should be ready to be harmed.</p>

<p>Those who are open and respectful shall receive my kindness and respect.</p>

<p>Those who plot against me are seeking their own death.</p>

<p>This is true, for I am death… I am Lin Feng”
"""


def genlist(start, end):
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end + 1):
        # print(i)
        if (
            i in range(1051, 1056 + 1)
            or i in [1441, 1537, 1883, 2450]
            or i in range(2481, 2485 + 1)
        ):
            text = f"Chapter {i}"
        elif i == 1124:
            text = "Chapter 1124: Soon Getting Nature pills"
        elif i == 1224:
            text = "Chapter 1124: Qiu Yue Xin"
        elif i == 1936:
            text = f"Chaoter {i}:"
        elif i == 2024:
            text = "Chapter 2024: Collapsing Sky"
        elif i == 2124:
            text = "Chapter 2024: Deployment"
        elif i == 2237:
            text = "Chapter 2237: Fighting"
        elif i == 2337:
            text = "Chapter 2237: Sky Palace"
        elif i == 2243:
            text = "Chapter 2243: Name List"
        elif i == 2343:
            text = "Chapter 2243: Devouring"
        elif i in range(2476, 2480 + 1):
            text = f"Chapters {i}"
        else:
            text = f"^Chapter {i}:"
        link = list_page.find("a", text=re.compile(text))
        url = f"{origin}{link["href"].split("/")[-1]}"
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
