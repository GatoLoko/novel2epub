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

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 477),
           # This author pisses me off, holding back the novel while the manga
           # catches up.
           }

origin = 'http://www.wuxiaworld.com/novel/tales-of-demons-and-gods/'
author = 'Mad Snail (发飙的蜗牛)'
cover_file = 'Covers/todg.jpg'
title = 'Tales of Demons and Gods - Vol'

synopsis_text = """
Killed by a Sage Emperor and reborn as his 13 year old self, Nie Li was
given a second chance at life. A second chance to change everything,
save his loved ones and his beloved city. He shall once again battle with
the Sage Emperor to avenge his death. With the vast knowledge he accumulated
in his previous life, he shall have a new starting point. Although he
started as the weakest, without a doubt, he will climb the steps towards the
strongest.</p>

<p>Cultivating the strongest cultivation technique, wielding the strongest
demon spirits, he shall reach the pinnacle of Martial Arts. Enmities of the
past will be settled in this new lifetime.</p>

<p>“Since I’m back, then in this lifetime, I shall become the King of Gods that
dominates everything. Let everything else tremble beneath my feet!”
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + 'tdg-chapter-' + str(i)
        # if i >= 472:
        #     url = origin + 'tdg-chapter-' + str(i+1)
        if i == 278:
            url = origin + 'tdg-chapter-' + str(i) + "-1"
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
