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
           '4': Volume('4', 301, 311),
           }

origin = 'http://www.wuxiaworld.co/In-a-Different-World-with-a-Smartphone/'
author = 'Ming Yu (明宇)'
cover_file = 'Covers/iadwwas.jpg'
title = 'In a different world with a smartphone - Vol'

synopsis_text = """
After a freak accident involving some lightning winds up zapping him dead,
15-year-old Mochizuki Touya wakes up to find himself face-to-face with God. “I
am afraid to say that I have made a bit of a blunder…” laments the old coot.
But all is not lost! God says that he can reincarnate Touya into a world of
fantasy, and as a bonus, he gets to bring his smartphone along with! So begins
Touya’s adventure in a new, anachronistic pseudo-medieval world. Friends!
Laughs! Tears! Inexplicable Deus ex Machina! He sets off on a journey full of
wonder as he absentmindedly travels from place to place, following whatever
goal catches his fancy. The curtains lift on an epic tale of swords, sorcery,
and smartphone apps!
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        text = '^Chapter %s: .*' % str(i)
        if i == 34:
            text = '^Chatper %s: .*' % str(i)
        if i in [187, 300]:  # Skip missing chapters
            continue
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    return content
