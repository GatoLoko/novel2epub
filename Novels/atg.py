#!/usr/bin/env python3

# -*- coding: utf-8 -*-

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

volumes = {'1': Volume('1 - Red-Colored calamity',
                       0, 100),
           '2': Volume('2 - Blue Wind continent',
                       101, 200),
           '3': Volume('3 - Name that shakes the Profound Sky',
                       201, 300),
           '4': Volume('4 - Fury that burns the heavens',
                       301, 400),
           '5': Volume('5 - Primordial Profound Ark',
                       401, 500),
           '6': Volume('6 - Lordship in Illusory Demon',
                       501, 650),
           '7': Volume('7 - Heaven Smiting shakes the world',
                       651, 800),
           '8': Volume('8 - Cloud\'s End Mirage',
                       801, 900),
           '9': Volume('9 - Realm of the gods',
                       901, 1000),
           '10': Volume('10 - Snow Song\'s flame God',
                        1001, 1100),
           '11': Volume('11 - Profound God convention',
                        1101, 1200),
           '12': Volume('12 - Infatuation in dreams',
                        1201, 1273),
           'X': Volume('X - END',
                       0000, 0000)
           }

origin = 'http://www.wuxiaworld.com/novel/against-the-gods/'
author = 'Mars Gravity (火星引力)'
cover_file = 'Covers/againstthegods-225x300.jpg'
title = 'Against the Gods - Vol'

synopsis_text = """
Official description:</p>
<p>Wielding the Sky Poison Pearl, receiving the blood of an Evil God,
cultivating the strength to oppose heaven, a lord overlooking the world!<p>

<p>Synopsis by alyschu:</p>
<p>A boy is being chased by various people because he alone holds some kind of
treasure. He jumps off a cliff to not let any of them have it and wakes up in
the body of a boy with the same name in another world. Fortunately, he has kept
the treasure he ran off with.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i == 761:
            url = origin + "atg-chapter-" + str(i)
            chapterlist.append(url)
            url = origin + "atg-chapter-" + str(i) + "-05"
            chapterlist.append(url)
        if i in [1043, 1044]:
            url = origin + "chapter-" + str(i)
            chapterlist.append(url)
        else:
            url = origin + "atg-chapter-" + str(i)
            chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
