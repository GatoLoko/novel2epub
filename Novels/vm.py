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
Created on 04/11/18

@author: GatoLoko
"""

import common
import re
Volume = common.Volume

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 700),
           '8': Volume('8', 701, 800),
           '9': Volume('9', 801, 900),
           '10': Volume('10', 901, 960),
           #
           '11': Volume('11', 1001, 1100),
           '12': Volume('12', 1101, 1200),
           '13': Volume('13', 1201, 1300),
           '14': Volume('14', 1301, 1400),
           '15': Volume('15', 1401, 1500),
           '16': Volume('16', 1501, 1600),
           '17': Volume('17', 1601, 1640),
           '18': Volume('18', 1701, 1800),
           '19': Volume('19', 1801, 1900),
           '20': Volume('20', 1901, 2000),
           '21': Volume('21', 2001, 2100),
           '22': Volume('22', 2101, 2200),
           '23': Volume('23', 2201, 2300),
           '24': Volume('24', 2301, 2400),
           '25': Volume('25', 2401, 2500),
           '26': Volume('26', 2501, 2600),
           '27': Volume('27', 2601, 2700),
           '28': Volume('28', 2701, 2800),
           # As of Jun 2019, this novel has 2786+ chapters
           }

origin = 'http://www.wuxiaworld.co/Versatile-Mage/'
author = 'Chaos (乱)'
cover_file = 'Covers/versatile-mage.jpg'
title = 'Versatile Mage - Vol'

synopsis_text = """
He woke up in a familiar world that had vastly changed.</p>

<p>His familiar school had become a mystical school that teaches magic,
encouraging everyone to become a mighty magician.</p>

<p>Outside the city, many wandering magical beasts and monsters attacked and
preyed on humans.</p>

<p>His world of advanced science changed into one that praised magic. Despite
this, his ambition in life, and his social status remained the same; one of the
dregs of the society with a struggling father and a disabled step sister that
couldn’t walk.</p>

<p>However, Mo Fan found that when most people could only practice a single
major element of magic, he was a Versatile Mage!
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        if i < 256:
            text = "Chapter %s .*" % str(i)
            if i == 61:
                text = "Chapter %s.*" % str(i)
            if i in [124, 135, 251]:
                text = "Chapter 0%s .*" % str(i)
        else:
            text = "^%s .*" % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = "%s%s" % (origin, link['href'])
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
