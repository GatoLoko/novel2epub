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
Created on 25/03/19

@author: GatoLoko
"""

from common import Volume
import common
import re

volumes = {'1': Volume('1', 1, 113),
           '2': Volume('2', 114, 339),
           '3': Volume('3', 340, 409),
           '4': Volume('4', 410, 511),
           '5': Volume('5', 512, 580),
           '6': Volume('6', 581, 735),
           '7': Volume('7', 736, 1026),
           }

origin = 'http://www.wuxiaworld.co/God-and-Devil-World/'
author = 'Zi Chan Bao Zeng (资产暴增)'
cover_file = 'Covers/godanddevilworld.jpg'
title = 'God and Devil world - Vol'

synopsis_text = """
In less than an instant the world as we knew it was at its end.</p>

<p>That’s right. The Apocalypse. In a single blink Zombies appeared and mutated
monsters began to rampage all throughout the world. Now it was the human
species turn to fight for survival and planetary dominance!</p>

<p>On the same day that the world descends into chaos we meet Yue Zhong.
Initially only hoping to get to his friends and escape to a refugee camp our
protagonist sets out, inadvertently building a team along the way. After a
series of fortuitous events and a few serious hunches our hero decides it’s
time to do more than just survive!</p>

<p>Yue Zhong begins to form the foundations of an enormous survival plan…
before he suddenly discovers that he has only gotten over the first hurdle….
Unbeknownst to Yue Zhong and company, the world outside of China is mostly a
wasteland! Country sized swathes of nuclear radiation and an extreme shortage
of supplies in the world after the nuclear explosions was quickly becoming the
“norm”. Mutants, Evolved animals and what’s worse, intelligent out of control
dinosaurs had quickly appeared and claimed their own sections of the planet.
There were several innately powerful Evolved races which appeared that were
more than 10 times stronger than humans, nearly all of them possessing bodies
impenetrable by normal bullets. The fabled orcs’ were another of these Evolved
races, the leader of which had in fact enslaved many of the remaining human
beings.</p>

<p>Unceremoniously exposed to such a cold and heartless new world, Yue Zhong is
faced with a choice: Find a deep dark hole and hope it goes back to “normal”?
Or overcome all obstacles and struggle towards Evolution!!!
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        text = '^' + str(i) + ' .*'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    # credline = re.compile(r'Translator:.*Editor:.*')
    # for i in content.find_all(text=credline):
    #     i.replaceWith('')
    return content
