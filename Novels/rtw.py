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

volumes = {'1': Volume('1', 1, 88),
           '2': Volume('2', 89, 96),
           '3': Volume('3', 97, 481),
           '4': Volume('4', 482, 825),
           '5': Volume('5', 826, 1218),
           '6': Volume('6', 1219, 1429),
           }

origin = 'http://www.wuxiaworld.co/Release-that-Witch/'
author = 'Er Mu (二目)'
cover_file = 'Covers/release-that-witch.jpg'
title = 'Release that witch - Vol'

synopsis_text = """
Chen Yan travels through time, only to end up becoming an honorable prince in
the Middle Ages of Europe. Yet this world was not quite as simple as he
thought. Witches with magical powers abound, and fearsome wars between churches
and kingdoms rage throughout the land.</p>

<p>Roland, a prince regarded as hopeless by his own father and assigned to the
worst fief, spends his time developing a poor and backward town into a strong
and modern city, while fighting against his siblings for the throne and
absolute control over the kingdom. Join Roland as he befriends and allies with
witches and, through fighting and even farming, pushes back invaders coming
from the realm of evil.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        text = '^%s .*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href']
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    return content
