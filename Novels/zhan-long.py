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

volumes = {'1': Volume('1 - Starting from scratch',
                       11, 248),
           '2': Volume('2 - Rise of heroes',
                       249, 500),
           '3': Volume('3 - The Grandmaster',
                       501, 748),
           '4': Volume('4 - The chase to the top',
                       749, 821),
           '5': Volume('5',
                       1001, 1250),
           '6': Volume('6 - END',
                       1251, 1379),
           }

origin = 'http://gravitytales.com/novel/Zhan-Long/'
author = 'Shi Luo Ye'
cover_file = 'Covers/zhan-long.jpg'
title = 'Zhan Long - Vol'

synopsis_text = """
Li Xiao Yao. Former S.W.A.T member, but retired into an ordinary security
guard. While being sent to grab a ladder, he accidentally stumbled upon the
VIP room instead of the storage room, and found a women in the middle of
changing. As revenge, she brought him out in the middle of nowhere and
kicked him off there. He spent hours walking back, only to find himself
being kicked out due to lack of payment. As bad things pile one after
another, his previous supervisor offers him a new job as the bodyguard for
the daughter of the Tian Xin group CEO, both in reality, and in a virtual
reality game.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + 'zl-chapter-' + str(i)
        if i in [12, 30, 31, 32, 33, 34, 35, 236, 237, 238, 472]:
            url += "-2"
        elif i is 11:
            url += "-3"
        chapterlist.append(url)
    return chapterlist
