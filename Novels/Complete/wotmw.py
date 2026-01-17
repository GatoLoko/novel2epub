# Created on 24/01/2017
# Copyright (C) 2017 GatoLoko
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
    "1": Volume("1 - Transmigration", 1, 287),
    "2": Volume("2 - Twilight zone", 288, 391),
    "3": Volume("3 - Morning Star chronicles", 392, 628),
    "4": Volume("4 - Passage of bloodlines", 629, 786),
    "5": Volume("5 - World of gods", 787, 1043),
    "6": Volume("6 - Final war", 1044, 1200),
}

origin = "http://www.wuxiaworld.com/novel/warlock-of-the-magus-world/"
author = "Wen Chao Gong/Plagiarist (文抄公)"
cover_file = "Covers/wotmw.jpg"
title = "Warlock Of The Magus World - Vol"

synopsis_text = """
What happens when a scientist from a futuristic world reincarnates in a
World of Magic and Knights?</p>

<p>An awesome MC — that's what happens!</p>

<p>A scientist's goal is to explore the secrets of the universe, and this is
exactly what Leylin sets out to do when he is reincarnated. Dark, cold and
calculating, he makes use of all his resources as he sets off on his
adventures to meet his goal.</p>

<p>Face? Who needs that… Hmmm… that guy seems too powerful for me to take on
now… I better keep a low profile for now.</p>

<p>You want me to help you? Sure… but what benefit can I get out of it?
Nothing? Bye.</p>

<p>Hmmm… that guy looks like he might cause me problems in the future. Should I
let him off for now and let him grow into someone that can threaten me…
Nahhh. *kill*
"""


def genlist(start, end):
    chapterlist = []
    for i in range(start, end + 1):
        url = f"{origin}wmw-chapter-{i}/"
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
