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
import common
import re

volumes = {'1': Volume('1 - Lian tribal clan',
                       1, 80),
           '2': Volume('2 - Kingdom selection',
                       81, 141),
           '3': Volume('3 - Divine Capital',
                       142, 156),
           '4': Volume('4 - Tai Ah Divine city',
                       157, 212),
           '5': Volume('5 - Rookie ranking competition',
                       213, 254),
           '6': Volume('6 - Desolate Heaven master',
                       255, 277),
           '7': Volume('7 - Divine Wilderness',
                       278, 302),
           '8': Volume('8 - City Lords birthday banquet',
                       303, 343),
           '9': Volume('9 - Tai Ah Divine Kingdom calamity',
                       344, 372),
           '10': Volume('10 - Desolate Heaven technique tea session',
                        373, 407),
           '11': Volume('11 - Great Empress relic trial',
                        408, 427),
           '12': Volume('12 - Great Empress mystic realm',
                        428, 542),
           '13': Volume('13 - Post Great Empress mystic realm',
                        543, 602),
           '14': Volume('14 - Blackstone trials',
                        603, 662),
           '15': Volume('15 - Tian Yuan world disaster',
                        663, 683),
           '16': Volume('16 - Divine Wilderness escapade',
                        684, 718),
           '17': Volume('17 - Black-armored Demon God',
                        719, 767),
           '18': Volume('18 - 12 Empyrean Heavens',
                        768, 802),
           '19': Volume('19 - Pre-Luo Divine Hall trials',
                        803, 854),
           '20': Volume('20 - Empress Luos banquet',
                        855, 871),
           '21': Volume('21 - Luo Divine Hall trials',
                        872, 916),
           '22': Volume('22 - Alliance chanllenger',
                        917, 949),
           '23': Volume('23 - Disciple recruitment',
                        950, 988),
           '24': Volume('24 - Azure Wood Great World',
                        989, 1100),
           '25': Volume('25', 1101, 1200),
           '26': Volume('26', 1201, 1300),
           '27': Volume('27', 1301, 1400),
           '28': Volume('28', 1401, 1500),
           '29': Volume('29', 1501, 1600),
           '30': Volume('30', 1601, 1604),
           'X': Volume('X - ',
                       9999, 9999)
           }

origin = 'http://www.wuxiaworld.co/True-Martial-World/'
author = 'Canjian Li De Niu/Cocooned Cow (蚕茧里的牛)'
cover_file = 'Covers/true-martial-world.jpg'
title = 'True Martial World - Vol'

synopsis_text = """
With the strongest experts from the 33 Skies, the Human Emperor, Lin Ming
and his opponent, the Abyssal Demon King were embroiled in a final battle.
It ended with the Human Emperor destroying the Abyssal World and killing the
Abyssal Demon King. By then, a godly artifact, the mysterious purple card
that had previously sealed the Abyssal Demon King, had long disappeared into
the space-time vortex and tunneled through infinite space-time, with a loved
one of Lin Ming accompanying it.</p>

<p>In the vast wilderness, where martial arts was still slowly growing in its
infancy, several peerless masters tried to find their path in the world of
martial arts.</p>

<p>A young adult named Yi Yun from modern Earth had unwittingly stumbled into
such a world and began that journey with a purple card of unknown origin.</p>

<p>It’s a magnificent yet unknown true martial art world. This is the story of
a normal young adult turning into a legendary peerless expert.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        text = 'Chapter ' + str(i) + ':.*'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist
