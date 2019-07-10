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

import common
import re

Volume = common.Volume

volumes = {'1': Volume('1 - Starting from scratch',
                       1, 248),
           '2': Volume('2 - Rise of heroes',
                       249, 500),
           '3': Volume('3 - The Grandmaster',
                       501, 748),
           '4': Volume('4 - The chase to the top',
                       749, 868),
           '5': Volume('5',
                       1001, 1001),
           '6': Volume('6 - END',
                       1251, 1251),
           # This novel ends with chapter 1379
           }

origin = 'http://www.wuxiaworld.co/Zhan-Long/'
author = 'Shi Luo Ye'
cover_file = 'Covers/zhan-long.jpg'
title = 'Zhan Long - Vol'

synopsis_text = """
Li Xiao Yao left S.W.A.T to become an ordinary security guard. While working,
he happened to enter the VIP room and found Lin Wang Er still in the middle of
changing. As revenge, she took him on a ride and kicked him out of the car.</p>

<p>After hours of walking, Li Xiao Yao finally managed to get back home just to
be kicked out of the house. He then got an offer from his previous supervisor
to become the bodyguard of the Tian Xi group CEO’s daughter both in game and in
reality. But unknown to Li Xiao Yao the girl was actually…
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        text = '^Chapter %s .*' % str(i)
        if i in [30, 236, 237, 406, 408, 548, 749, 828]:
            text = '^Chapter %s' % str(i)
        elif i == 336:
            text = '^Chapter 336 – You Lump of Meat!'
        elif i == 337:
            text = '^Chapter 336 – The Tyrannical Ye Lai'
        elif i == 490:
            text = '^Chapter 490 – The Endless Chase'
        elif i == 590:
            text = '^Chapter 490 – The Red Dragon Queen'
        elif i == 830:
            text = '^Chapter 830 Rotten and Rusty Army Part 1 ?'
            link = list_page.find('a', text=re.compile(text))
            url = origin + link['href']
            chapterlist.append(url)
            text = '^Chapter 830 – Rotten and Rusty Army Part 2 ?'
        elif i == 857:
            text = '^Chapter %s.*' % str(i)
        elif i == 51 or i >= 841:
            text = '^Chapter %s-.*' % str(i)
        elif i == 839:
            text = '^hapter 839 – The Flying Slash Part 1'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
