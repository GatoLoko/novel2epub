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
Created on 31/07/17

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1 - ',
                       1, 26),
           '2': Volume('2 - ',
                       27, 48),
           '3': Volume('3 - ',
                       49, 71),
           '4': Volume('4 - ',
                       72, 94),
           '5': Volume('5 - ',
                       95, 117),
           '6': Volume('6 - ',
                       118, 140),
           '7': Volume('7 - ',
                       141, 162),
           '8': Volume('8 - ',
                       163, 183),
           '9': Volume('9 - ',
                       184, 203),
           '10': Volume('10 - ',
                        204, 224),
           '11': Volume('11 - ',
                        225, 247),
           '12': Volume('12 - ',
                        248, 269),
           '13': Volume('13 - ',
                        270, 290),
           '14': Volume('14 - ',
                        291, 313),
           '15': Volume('15 - ',
                        314, 335),
           '16': Volume('16 - ',
                        336, 356),
           '17': Volume('17 - ',
                        357, 379),
           '18': Volume('18 - ',
                        380, 397),
           '18.': Volume('18 - END',
                         380, 400)
           }

origin = 'http://www.wuxiaworld.com/novel/the-book-eating-magician/'
author = 'Mekenlo (메켄로)'
cover_file = 'Covers/BookEatingMagician.jpg'
title = 'The Book Eating Magician - Vol'

synopsis_text = """
[‘Lightning Magic Primer’ has been consumed. Your understanding is very high.]
[The 2nd Circle magic ‘Lightning Bolt’ has been acquired.]</p>

<p>The unprecedented magician who will eat all the magic books of the world has
appeared.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i == 94:
            url = origin + "bem-chapter-4-1"
        else:
            url = origin + "bem-chapter-" + str(i)
        chapterlist.append(url)
    return chapterlist
