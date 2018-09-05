#!/usr/bin/env python3

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

"""
Created on 24/01/17

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1 - Rise of the Cloud', 0, 90),
           '2': Volume('2 - Wandering the Beiyan province', 91, 180),
           '3': Volume('3 - The Crafting School', 181, 361),
           '4': Volume('4 - Soulbeast forest', 362, 510),
           '5': Volume('5 - Turmoil in the Capital', 511, 700),
           '6': Volume('6 - Pill Royale', 701, 722),
           '7': Volume('7 - ', 841, 841),
           '8': Volume('8 - ', 1001, 1001),
           '9': Volume('9 - ', 1051, 1051),
           '10': Volume('10 - ', 1161, 1161),
           '11': Volume('11 - ', 1291, 1356)
           }

origin = 'http://www.wuxiaworld.com/novel/upgrade-specialist-in-another-world/'
author = 'Endless Sea Of Clouds (茫茫云海)'
cover_file = 'Covers/usaw.jpg'
title = 'Upgrade Specialist in Another World - Book '

synopsis_text = """Just as a gamer found an overpowered skill book called ‘Item
Upgrade’ in the hottest virtual reality role-playing game on Earth, something
happened to the game’s system, causing his soul to leave his body and go to
another dimension. Common sense dictates that he would be born anew then become
the greatest overlord of this world by making use of his advanced knowledge.
Not in this case! He was already dead. Only some fragments of his soul and that
skill book managed to get into that dimension and merge with an ordinary common
youngster called Bai Yunfei.</p>

<p>This was the enormous Tianhun continent, where humans could be said to have
no limits. There was a group of humans here who could cultivate the power of
their own souls then control their bodies, the natural elements and even other
people’s souls with that power! These special beings were called — soul
cultivators. Come witness how the several fragments of the dead
inter-dimensional traveler’s soul and that skill book, which was not governed
by the laws of this plane, were going to help Bai Yunfei become a legendary
soul cultivator and craftsman!
"""


def genlist(start, end):
    global origin
    chapterlist = []
    currentvol = ''
    for key, value in volumes.items():
        if value.first is start:
            currentvol = key
    for i in range(start, end+1):
        url = origin + 'usaw-book-' + str(currentvol) + '-chapter-' + str(i)
        if i == 0:
            url = origin + 'usaw-chapter-0'
        if i == 546:
            url = origin + 'usaw-book-5chapter-546'
        if i == 573:
            url = origin + 'usaw-book-5-chapter-5-573'
        if i == 638:
            url = origin + 'usaw-chapter-638'
        chapterlist.append(url)
    return chapterlist
