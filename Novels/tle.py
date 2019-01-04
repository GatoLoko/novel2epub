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
Created on 20/10/18

@author: GatoLoko
"""

import common
import re

Volume = common.Volume

volumes = {'1': Volume('1', 0, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 650),
           }

origin = 'http://www.wuxiaworld.co/The-Lord-is-Empire/'
author = ' (神天衣)'
cover_file = 'Covers/the-lords-empire.jpg'
title = "The Lord's Empire - Vol"

synopsis_text = """
"Ding! Soulbinding has been successfully completed; you will now head to the
Heaven Awaken World.” After hearing this, Zhao Fu’s vision darkened as he fell
to the ground.</p>

<p>With bleak prospects in the real world, Zhao Fu's life is turned around when
countless crystals fell from the sky one night, which people could use to enter
an alternate, game-like world. After obtaining an ancient Chinese empire's
legacy, Zhao Fu uses his intellect and resourcefulness to develop his own
empire from a tiny village. However, with enemies both in the real world and in
the Heaven Awaken World, he must make brilliant decisions and use creative
schemes to survive.</p>

<p>If you enjoy kingdom-building, game-like alternate worlds, incorporation of
ancient history (though some is romanticised), and strategy, you'll be sure to
love The Lord's Empire!
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        if i < 608:
            text = 'Chapter ' + str(i) + '.*'
        else:
            text = '^' + str(i) + '.*'
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist
