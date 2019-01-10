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

volumes = {'1': Volume('1 - Battle of dignity',
                       1, 264),
           '2': Volume('2 - Sweeping through the Nine Provinces',
                       265, 548),
           '3': Volume('3 - Eastern Sea region',
                       549, 1004),
           '4': Volume('4 - A new journey',
                       1005, 1558),
           '5': Volume('5 - Battle for Overlord',
                       1559, 2148),
           '6': Volume('6 - Hundred refining ordinary realm',
                       2149, 2672),
           '7': Volume('7 - Return of the discarded child',
                       2673, 3108),
           '8': Volume('8 - Battle of prophecy',
                       3109, 3183),
           'X': Volume('X - ',
                       9999, 9999)
           }

origin = 'http://www.wuxiaworld.com/novel/martial-god-asura/'
author = 'Kindhearted Bee (善良的蜜蜂 / Shan Liang de Mi Feng)'
cover_file = 'Covers/mga.jpg'
title = 'Martial God Asura - Vol'

synopsis_text = """
Regarding potential—even if you are not considered a genius, you can still
learn Mysterious Techniques and martial skills. Anyone can be enlightened
without a master.</p>

<p>Regarding strength—despite having a myriad of artifacts, you may not defeat
my army of World Spirits.</p>

<p>Who am I? All of the world’s living perceives me as Asura, but I was
ignorant to such a thing. I thus ascend to be the Martial God as Asura.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i == 1632:
            # Author misnumbered chapter 1633 as 1632 and continued from there,
            # causing this number to be duplicated
            url = origin + 'mga-chapter-1632-01'
            chapterlist.append(url)
            url = origin + 'mga-chapter-1632-02'
            chapterlist.append(url)
        else:
            url = origin + 'mga-chapter-' + str(i)
            chapterlist.append(url)
    return chapterlist
