#!/usr/bin/env python3

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

"""
Created on 09/01/18

@author: GatoLoko
"""

from common import Volume
import re

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 700),
           '8': Volume('8', 701, 800),
           '9': Volume('9', 801, 856),
           #
           '10': Volume('10', 901, 901),
           '11': Volume('11', 1001, 1001),
           '12': Volume('12', 1101, 1101),
           '13': Volume('13', 1201, 1201),
           '14': Volume('14', 1301, 1301),
           '15': Volume('15', 1401, 1401),
           '16': Volume('16', 1501, 1501),
           '17': Volume('17', 1601, 1601),
           '18': Volume('18', 1701, 1701),
           '19': Volume('19', 1801, 1801),
           '20': Volume('20', 1901, 1901),
           '21': Volume('21', 2001, 2001),
           '22': Volume('22', 2101, 2101),
           '23': Volume('23', 2201, 2201),
           '24': Volume('24', 2301, 2301),
           '25': Volume('25', 2401, 2401),
           '26': Volume('26', 2501, 2501),
           '27': Volume('27', 2601, 2601)
           # This novel ends with chapter 2621
           }

origin = 'http://www.wuxiaworld.com/novel/tranxending-vision/'
author = 'Li Xianyu (李闲鱼)'
cover_file = 'Covers/tv.jpg'
title = 'TranXending Vision - Vol'

synopsis_text = """
Xia Lei, whose parents were no longer around, had to work hard to support
himself and his sister. One day, he got into an accident at work which burnt
his left eye. After he awoke in the hospital bed, he discovered that his eye
was not blind – it gained abilities! Now, he is using these abilities to right
wrongs and make a better life for himself and others. Will Xia Lei triumph over
the corrupt and privileged with his newfound power?</p>

<p>I am destined to be the protagonist of this era!
"""

april1st = re.compile(r"^(Rezydencja)|(Szybko)|(Następnie)|(Mają)|(W międzyczasie)|(PEW PEW PEW.)|(Tatuś)|(„Idź)|(Hiena: OK.)")


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + 'tv-chapter-' + str(i)
        chapterlist.append(url)
    return chapterlist


def clean(content):
    for i in content.find_all(text=april1st):
        i.replaceWith("")
    return content
