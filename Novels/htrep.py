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

volumes = {'1': Volume('1',
                       100, 113),
           '2': Volume('2',
                       201, 212),
           '3': Volume('3',
                       301, 313),
           '4': Volume('4',
                       401, 412),
           '5': Volume('5',
                       501, 512),
           '6': Volume('6',
                       601, 613),
           '7': Volume('7 - Omake1',
                       701, 710),
           '8': Volume('8 - Omake2',
                       801, 810),
           }

origin = 'http://stabbingwithasyringe.home.blog/translations/harem-tales' + \
    '-of-reincarnated-elf-prince/'
author = 'Warui Baketsu (わるいバケツ)'
cover_file = 'Covers/htrep.jpg'
title = 'Harem tales of a reincarnated elf prince - Vol'

synopsis_text = """
I was a good looking prince when I was reborn, and because I could do
indecent things as much as I like, I decided to make a harem while traveling
with a beautiful female elf</p>

<p>Formerly an otaku, the hero who was just reincarnated became a handsome elf
prince of another world.</p>

<p>In his previous life he was just a plain-faced man, so in this world he uses
his high position as a prince to his advantage and keep holding beautiful women
in his arms, every day in his life.</p>

<p>With his status as a prince and a handsome face, together with the high
abilities of the elves……he will thoroughly enjoy the life that he hasn’t done
in his previous world!
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i == 100:
            url = origin + 'harem-tales-of-a-reincarnated-elf-prince-prologue-1/'
            chapterlist.append(url)
            url = origin + 'reincarnated-elf-prince-prologue-2-2/'
            chapterlist.append(url)
        elif i in range(100, 105+1):
            url = origin + "reincarnated-elf-prince-chapter-" + \
                str(i)[1:].lstrip('0') + "/"
            chapterlist.append(url)
        elif i == 613:
            url = origin + "translations/tower-dungeon-management/" + \
                "mage-tower-management-epilogue/"
            chapterlist.append(url)
        elif i in range(700, 711):
            url = origin + "reincarnated-elf-prince-extra-volume-1-chapter-" \
                + str(i)[1:].lstrip('0') + "/"
            chapterlist.append(url)
        elif i in range(800, 811):
            url = origin + "reincarnated-elf-prince-extra-volume-2-chapter-" \
                + str(i)[1:].lstrip('0') + "/"
            chapterlist.append(url)
        else:
            url = origin + "reincarnated-elf-prince-volume-" + str(i)[0] + \
                "-chapter-" + str(i)[1:].lstrip('0') + "/"
            chapterlist.append(url)
    return chapterlist


def clean(content):
    for i in content.find_all('script'):
        i.decompose()
    return content
