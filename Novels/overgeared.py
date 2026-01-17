# Created on 01/11/2020
# Copyright (C) 2020 GatoLoko
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
    "16": Volume("16", 1501, 1558),
    "17": Volume("17", 1601, 1601),
    "18": Volume("18", 1701, 1701),
    "19": Volume("19", 1801, 1801),
    "20": Volume("20", 1901, 1901),
}

origin = "http://www.wuxiaworld.com/novel/overgeared"
author = "Park Saenal"
cover_file = "Covers/Overgeared.jpg"
title = "Overgeared - Vol"

synopsis_text = """
As Shin Youngwoo had an unfortunate life and is now stuck carrying bricks on
construction sites. He even had to do labor in the VR game, Satisfy!</p>

<p>However, luck would soon enter his hopeless life. His character, ‘Grid’,
would discover the Northern End Cave for a quest, and in that place, he would
find ‘Pagma's Rare Book’ and become a legendary class player…
"""


def genlist(start: int, end: int) -> list[str]:
    chapterlist = []
    for i in range(start, end + 1):
        url = f"{origin}/og-chapter-{i}"
        chapterlist.append(url)
    return list(dict.fromkeys(chapterlist))


def clean(content):
    # credline = re.compile(r'Translator:.*Editor:.*')
    # for i in content.find_all(text=credline):
    #     i.replaceWith('')
    return content
