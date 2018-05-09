#!/usr/bin/env python3

# -*- coding: utf-8 -*-

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
Created on 09/05/18

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1 - ',
                       1, [1, 7]),
           '2': Volume('2 - ',
                       2, [8, 14]),
           '3': Volume('3 - ',
                       3, [15, 21]),
           '4': Volume('4 - ',
                       4, [22, 24]),
           '5': Volume('5 - ',
                       5, [25, 35]),
           '6': Volume('6 - ',
                       6, [36, 54]),
           '7': Volume('7 - ',
                       7, [55, 61]),
           '8': Volume('8 - ',
                       8, [62, 70]),
           '9': Volume('9 - ',
                       9, [71, 79]),
           '10': Volume('10 - ', 10, [80, 83]),
           '11': Volume('11 - ', 11, [84, 91]),
           '12': Volume('12 - ', 12, [92, 105]),
           '13': Volume('13 - ', 13, [106, 112]),
           '14': Volume('14 - ', 14, [113, 119]),
           '15': Volume('15 - ', 15, [120, 126]),
           '16': Volume('16 - ', 16, [127, 133]),
           '17': Volume('17 - ', 17, [134, 140]),
           '18': Volume('18 - ', 18, [141, 147]),
           '19': Volume('19 - ', 19, [148, 168]),
           '20': Volume('20 - ', 20, [169, 171]),
           '21': Volume('21 - ', 21, [172, 175]),
           '22': Volume('22 - ', 22, [176, 189]),
           '23': Volume('23 - ', 23, [190, 217]),
           '24': Volume('24 - ', 24, [218, 231]),
           '25': Volume('25 - ', 25, [232, 238]),
           '26': Volume('26 - ', 26, [239, 266]),
           '27': Volume('27 - ', 27, [267, 271]),
           '28': Volume('28 - ', 28, [55, 271]),
           }

origin = 'http://www.wuxiaworld.com/novel/heavenly-jewel-change/'
author = 'Tang Jia San Shao (唐家三少)'
cover_file = 'Covers/heavenly-jewel-change.jpg'
title = 'Heavenly Jewel Change - Vol'

synopsis_text = """
[Zen’s Synopsis]</p>

<p>In a world where power means everything, and the strong trample the weak;
there was a boy born from a Heavenly Jewel Master. Born in a small country
which had to struggle to survive, the boy was expected to do great things.
Alas he turned out to have blocked meridians and was unable to cultivate,
ending up the trash of society. His father’s tarnished pride… his fianceé’s
ultimate dishonour…</p>

<p>Being almost accidentally killed and left for the dead, heaven finally
smiles upon him as a miracle descends, awakening his potential as a Heavenly
Jewel Master. Or… is it truly a gift?</p>

<p>Join our dear rascally and shameless MC Zhou Weiqing in his exploits to
reach the peak of the cultivation world, form an army, protect those he loves,
and improve his country!</p>

<p>An all new world, an all new power system, unique weaponry & MC! Come join
me in laughing and crying together with this new masterpiece from Tang Jia San
Shao!</p>

<p>[Translated Synopsis]</p>

<p>Every human has their Personal Jewel of power, when awakened it can either
be an Elemental Jewel or Physical Jewel. They circle the right and left wrists
like bracelets of power.</p>

<p>Heavenly Jewels are like the twins born, meaning when both Elemental and
Physical Jewels are Awakened for the same person, the pair is known as Heavenly
Jewels.</p>

<p>Those who have the Physical Jewels are known as Physical Jewel Masters,
those with Elemental Jewels are Elemental Jewel Masters, and those who train
with Heavenly Jewels are naturally called Heavenly Jewel Masters.</p>

<p>Heavenly Jewel Masters have a highest level of 12 pairs of jewels, as such
their training progress is known as Heavenly Jewels 12 Changes.</p>

<p>Our MC here is an archer who has such a pair of Heavenly Jewels.
"""


def genlist(book, chapters):
    global origin
    chapterlist = []
    one_pages = [91, 98, 271]
    two_pages = [28, 35, 42, 49, 56, 63, 70, 77, 84, 105, 112, 119, 126, 138,
                 140, 147, 149, 153, 154, 161, 168, 175, 182, 189, 196, 203,
                 210, 217, 224, 231, 238, 245, 252, 259, 266]
    four_pages = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19,
                  20, 21, 22, 24]
    five_pages = [14, 23]
    for i in range(chapters[0], chapters[1]+1):
        if i in one_pages:
            pages = 1
        elif i in two_pages:
            pages = 2
        elif i in four_pages:
            pages = 4
        elif i in five_pages:
            pages = 5
        else:
            pages = 3
        for j in range(1, pages+1):
            url = origin + 'hjc-book-' + str(book) + '-chapter-' + str(i) + \
                '-' + str(j).zfill(2)
            chapterlist.append(url)
    return chapterlist
