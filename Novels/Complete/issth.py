# Created on 18/12/2018
# Copyright (C) 2018 GatoLoko
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

from libs.common import Volume

volumes = {
    "1": Volume("1 - Patriarch Reliance", 1, 95),
    "2": Volume("2 - Cutting into the Southern Domain", 96, 204),
    "3": Volume("3 - The honor of Violet Fate", 205, 313),
    "4": Volume("4 - Five color Paragon", 314, 628),
    "5": Volume("5 - Nirvanic Rebirth. Blood everywhere!", 629, 800),
    "6": Volume(
        "6 - Fame that rocks the Ninth Mountain; the path to True Immortality",
        801,
        1004,
    ),
    "7": Volume(
        "7 - Immortal Ancient builds a bridge leaving the" + " Ninth Mountain",
        1005,
        1211,
    ),
    "8": Volume("8 - My Mountain and Sea realm", 1212, 1409),
    "9": Volume(
        "9 - The demon sovereign returns; the peak of the" + " vast expanse!",
        1410,
        1557,
    ),
    "10": Volume("10 - I watch blue seas become lush fields", 1558, 1614),
}

origin = "http://www.wuxiaworld.com/novel/i-shall-seal-the-heavens/"
author = "Er Gen (耳根)"
cover_file = "Covers/issth.jpg"
title = "I shall seal the heavens - Vol"

synopsis_text = """
“What I want, the Heavens shall not lack!”</p>

<p>“What I don’t want, had better not exist in the Heavens!”</p>

<p>This is a story which originates between the Eighth and Ninth Mountains, the
world in which the strong prey upon the weak.</p>

<p>“My Name is Meng Hao! The Ninth Generation Demon Sealer, I shall seal the
Heavens!“
"""


def genlist(start, end):
    chapterlist = []
    currentvol = ""
    for key, value in volumes.items():
        if value.first is start:
            currentvol = key
    for i in range(start, end + 1):
        # Chapter 583 is merged into 582. Chapter 1377 is missing entirelly.
        if i in [583, 1377]:
            continue
        url = f"{origin}issth-book-{currentvol}-chapter-{i}"
        if i == 582:
            url = f"{url}-0583"
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
