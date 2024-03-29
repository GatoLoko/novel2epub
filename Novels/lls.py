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
Created on 19/02/19

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
           '9': Volume('9', 801, 851),
           #
           '10': Volume('10', 901, 900),
           '11': Volume('11', 1001, 1001),
           '12': Volume('12', 1101, 1101),
           '13': Volume('13', 1201, 1201),
           '14': Volume('14', 1301, 1301),
           # This novel ends with chapter 1399.
           }

origin = 'http://www.wuxiaworld.co/Long-Live-Summons/'
author = 'Xia Fei Shuang Jia (霞飞双颊)'
cover_file = 'Covers/Long-Live-Summons.jpg'
title = 'Long Live Summons - Vol'

synopsis_text = """
</p>The Soaring Dragon Continent is a world of summons, you can only become
strong if you become a summoner! Yue Yang, an average high school boy, was
suddenly transported into this world. When he woke up, he was greeted with a
lot of worried faces and found out that he had assumed another person’s
identity. Turns out he’s the good-for-nothing third son of the Yue Family, who
had just recently drowned himself because of a failed engagement. Unlike the
third son of the Yue Family who was useless in summoning, Yue Yang succeeded in
making a contract with a summoning grimoire on his first try, even when the
other guy failed for the past fifteen years. Others would have a headache
making contracts with beasts afterwards, but countless beasts tried to gain
favour with Yue Yang instead, acting like a good kid before him.

<p>Yue Yang the brat, however, didn’t feel grateful at all: “Scram, Mythical
Beasts! Do you think you are cool like that? Go away from me now, I only like
beautiful summons!”</p>

<p>Even when royal families approached him for his talents, the shameless brat
replied, “I’m not interested in government stuff, I’m only interested in
beauties!”
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        if i in [186, 284, 286, 293, 295, 296, 361]:
            # Some chapters have 2 parts, first kind (with: –)
            text = '^Chapter %s Part 1 – .*' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href'].split("/")[-1]
            chapterlist.append(url)
            text = '^Chapter %s Part 2 – .*' % str(i)
        elif i in range(717, 753):
            # Some chapters have 2 parts, second kind (no separator)
            text = '^Chapter %s .* Part 1' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href'].split("/")[-1]
            chapterlist.append(url)
            text = '^Chapter %s .* Part 2' % str(i)
        elif i == 761:
            # Some chapters have 2 parts, third kind (with . for second part)
            text = '^Chapter %s: .*' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href'].split("/")[-1]
            chapterlist.append(url)
            text = '^Chapter %s.2 .*' % str(i)
        elif i == 762 or (i >= 765 and i <= 816):
            # Some chapters have 2 parts, fourth kind (with . for both parts
            if i == 790:
                text = '^Chapter %s .1.*' % str(i)
            else:
                text = '^Chapter %s.1.*' % str(i)
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href'].split("/")[-1]
            chapterlist.append(url)
            text = '^Chapter %s.2.*' % str(i)
        else:
            text = '^Chapter %s – .*' % str(i)
            if i == 212:
                text = '^Chapter %s- .*' % str(i)
            elif i == 356:
                text = '^Chapter 356'
            elif i in [647, 651, 763, 764]:
                text = '^Chapter %s - .*' % str(i)
            elif i >= 817:
                text = '^Chapter %s: .*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    return content
