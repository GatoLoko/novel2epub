#!/usr/bin/env python3

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

"""
Created on 21/02/2020

@author: GatoLoko
"""

from common import Volume
import common
import re

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 700),
           '8': Volume('8', 701, 800),
           '9': Volume('9', 801, 900),
           '10': Volume('10', 901, 1000),
           '11': Volume('11', 1001, 1100),
           '12': Volume('12', 1101, 1198),
           # This novel has over 5000 chapters in the original chinese.
           }

origin = 'http://www.wuxiaworld.co/Martial-Peak/'
author = 'MoMo (莫默)'
cover_file = 'Covers/martial-peak.jpg'
title = 'Martial Peak - Vol'

synopsis_text = """
The journey to the martial peak is a lonely, solitary and long one. In the face
of adversity, you must survive and remain unyielding. Only then can you break
through and continue on your journey to become the strongest. High Heaven
Pavilion tests its disciples in the harshest ways to prepare them for this
journey. One day the lowly sweeper Kai Yang managed to obtain a black book,
setting him on the road to the peak of the martials world.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        if i in list(range(1, 51)) + list(range(52, 505)) + list(range(506,627)):
            text = '^Chapter %s – .*' % str(i)
        elif i in [51]:
            text = '^Chapter %s - .*' % str(i)
        elif i in [505, 981]:
            text = '^Chapter %s( |,).*' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href']
            chapterlist.append(url)
            text = '^Chapter %s.5( |,).*' % str(i)
        elif i == 968:
            text = '^Chapter %s. .*' % str(i)
        else:
            text = '^Chapter %s, .*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
