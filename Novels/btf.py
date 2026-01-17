# Created on 19/02/2019
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
from libs.common import Volume

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
    "18": Volume("18", 1701, 1700),
    "19": Volume("19", 1801, 1900),
    "20": Volume("20", 2001, 2100),
    "21": Volume("21", 2101, 2200),
    "22": Volume("22", 2201, 2264),
    "23": Volume("23", 2301, 2301),
    "24": Volume("24", 2401, 2401),
    # As of May 2021, there are 10855+ chapters in the original novel.
    # As of Nov 2021, there are 11547+ chapters in the original novel.
    # As of Dec 2025, there are 16628+ chapters in the original novel.
}

origin = "http://m.wuxiaworld.xyz/Bringing-The-Farm-To-Live-In-Another-World/"
author = "Ming Yu (明宇)"
cover_file = "Covers/bringing-the-farm.jpg"
title = "Bringing the farm to live in another world - Vol"

synopsis_text = """
“If he's being badass, I'm gonna plant my own crops. If he messes with me, he
will not live past next year.”</p>

<p>Homebody Zhao Hai brought ‘QQ Farm’ along in his traversal to another world
and resided within the body of a fallen noble. His fief was a black land which
nothing could be planted, and more importantly, he even had a peerlessly
powerful fiancee, who was actually the successor of a duchy and future Grand
Duchess!</p>

<p>Even more importantly, he is a magical and martial cripple who could not
learn magic and martial arts. His crippling was very thorough.</p>

<p>“I can't learn magic, but I have the farm. You dare attack me? I'll release
bugs to eat up your rations and crops, and put pesticides and weed agents into
your water sources to make your lands grow weeds. See if you dare to attack me.
What? You wanna hire killers to assassinate me? Hehehe. I'll hide inside the
little house in my farm and see how you can attack me. When you leave, I'm
gonna terminate your country's crop productions, and then all of your people
will revolt. See if you dare to kill me.”</p>

<p>Watch how this somewhat black hearted hobo uses his QQ Farm in the world of
swords and magic to become a globally known nightmarish existence.
"""


def genlist(start: int, end: int) -> list[str]:
    list_page = common.get_html(origin)
    origin2 = "http://m.wuxiaworld.xyz/"
    chapterlist = []
    for i in range(start, end + 1):
        # print(i)
        text = rf"^Chapter {i} .*"
        if i in range(127, 137):
            text = rf"^Chapter {i}"
        elif i in [149, 861, 1044, 1212]:
            text = rf"^Chapter {i}-.*"
        elif i == 283:
            text = "^Chapter 284 – Special Requests"
        elif i == 284:
            text = "^Chapter 284 – Seeing West Wonder King"
        elif i == 311:
            text = "^Chapter 312 – Playing the Role of A Silkpants"
        elif i == 312:
            text = "^Chapter 312 – Keeping Up Appearances"
        elif i == 1350:
            continue
        link = list_page.find("a", text=re.compile(text))
        url = f"{origin2}{link['href'].split('/')[-1]}"
        chapterlist.append(url)
    return list(dict.fromkeys(chapterlist))


def clean(content):
    credline = re.compile(r"Translator:.*Editor:.*")
    for i in content.find_all(text=credline):
        i.replaceWith("")
    return content
