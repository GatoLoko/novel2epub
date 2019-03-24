#!/usr/bin/env python3

# Copyright (C) 2018 GatoLoko
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
Created on 09/01/18

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1 - ',
                       1, 100),
           '2': Volume('2 - ',
                       101, 200),
           '3': Volume('3 - ',
                       201, 300),
           '4': Volume('4 - ',
                       301, 400),
           '5': Volume('5',
                       401, 450),
           }

origin = 'http://www.wuxiaworld.com/novel/tranxending-vision/'
author = 'Li Xianyu (李闲鱼)'
cover_file = 'Covers/tv.jpg'
title = 'TranXendig Vision - Vol'

synopsis_text = """
Xia Lei, whose parents were no longer around, had to work hard to support
himself and his sister. One day, he got into an accident at work which burnt
his left eye. After he awoke in the hospital bed, he discovered that his eye
was not blind – it gained abilities! Now, he is using these abilities to right
wrongs and make a better life for himself and others. Will Xia Lei triumph over
the corrupt and privileged with his newfound power?</p>

<p>I am destined to be the protagonist of this era!
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + 'tv-chapter-' + str(i)
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
