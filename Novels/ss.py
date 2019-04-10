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
Created on 30/01/19

@author: GatoLoko
"""

import common
import re

Volume = common.Volume

volumes = {'1': Volume('1 - Awakening in the night', 1, 20),
           '2': Volume('2 - Fighter', 21, 40),
           '3': Volume('3 - Nine stage Thunder Blade', 41, 60),
           '4': Volume('4 - Astronomical bounty', 61, 85),
           '5': Volume('5 - Wargod Luo Feng', 86, 100),
           '6': Volume('6 - The fifty thousand year old corpse', 101, 173),
           '7': Volume('7 - Rebirth', 174, 223),
           '8': Volume('8 - Universe adventure', 224, 259),
           '9': Volume('9', 260, 314),
           '10': Volume('10', 315, 364),
           '11': Volume('11', 365, 439),
           '12': Volume('12', 440, 478),
           '13': Volume('13', 479, 541),
           '14': Volume('14', 542, 606),
           '15': Volume('15', 607, 668),
           '16': Volume('16', 669, 714),
           '17': Volume('17', 715, 753),
           '18': Volume('18', 754, 792),
           '19': Volume('19', 793, 861),
           '20': Volume('20', 862, 888),
           '21': Volume('21', 889, 943),
           '22': Volume('22', 944, 994),
           '23': Volume('23', 995, 1027),
           '24': Volume('24', 1028, 1092),
           '25': Volume('25', 1093, 1129),
           '26': Volume('26', 1130, 1158),
           '27': Volume('27', 1159, 1213),
           '28': Volume('28', 1214, 1259),
           '29': Volume('29', 1260, 1334),
           }

origin = 'http://www.wuxiaworld.co/Swallowed-Star/'
author = 'I Eat Tomatoes (我吃西红柿)'
cover_file = 'Covers/swallowed-star.jpg'
title = 'Swallowd Star - Vol'

synopsis_text = """
Year 2056, in a city in the Yuan Jiang Su Jin area. On top of a ruined,
shattered six story residential apartment sits a teenager wearing a combat
vest, militaristic trousers, and alloyed battle boots. On his back is a
hexagonal shield and equipped is a blood-shadow battle knife. He sits there
silently on the edge of the roof. At this time, the sparkling sky was shining
and there was a refreshing breath within the air that blew towards him.
However, there was only silence within the ruined, deserted city, with an
occasional howl that makes your heart skip a beat.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        text = '^' + str(i) + ' .*'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
