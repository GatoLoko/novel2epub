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
Created on 17/11/18

@author: GatoLoko
"""

import common
import re

Volume = common.Volume

volumes = {'1': Volume('1', 1, 83),
           '2': Volume('2', 84, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 646),
           }

origin = 'http://www.wuxiaworld.co/The-Wizard-World/'
author = 'Get Lost (滚开)'
cover_file = 'Covers/the-wizard-world.jpg'
title = 'The Wizard World - Vol'

synopsis_text = """
Ye Song, who once lived in a technologically-advanced world, died and
reincarnated into a noble teenager’s body in another world.</p>

<p>A fantasy world filled with magic!</p>

<p>A series of events filled with tragedy, action, etc. began to unfold one
after the other when he fatefully encountered one of the most guarded secrets
of this world, obtaining the legendary power of Wizards.</p>

<p>Watch how he reaches unreachable heights as a powerful Wizard in this new
world.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        if i < 632:
            text = 'Chapter ' + str(i) + ':.*'
        else:
            text = '^' + str(i) + '.*'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
