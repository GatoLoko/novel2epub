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
                       100, 114),
           '2': Volume('2',
                       201, 211),
           '3': Volume('3',
                       301, 311),
           '4': Volume('4',
                       401, 416),
           '5': Volume('5',
                       501, 516),
           '6': Volume('6',
                       601, 611),
           '7': Volume('7',
                       701, 711),
           '8': Volume('8',
                       801, 815),
           }

origin = 'http://stabbingwithasyringe.home.blog/translations/tower-dungeon-management/'
author = 'Kurisutara Sakurai (クリスタラー桜井)'
cover_file = 'Covers/armtdm.jpg'
title = 'A reincarnated mage\'s tower dungeon management - Vol'

synopsis_text = """
An otaku with a hobby of masturbating was reincarnated as the son of a great
mage.  As soon as he was born in this life, he vowed with a goal of embracing
women till his death.</p>

<p>That said, when he became 20 years old, the Demon Lord which was sealed by
his ancestors revived, and now it is his role to seal it once again.</p>

<p>And that demon lord is sealed in a tower dungeon that is rumored to be
impossible to capture.</p>

<p>However, by an unexpected coincidence, he had found out that the Demon Lord
is also one of him, a kindred spirit from within, so he joined her instead and
filled several traps in the tower dungeon, and thus they enjoyed a s*x spree
with all the women coming over!
"""


def genlist(start, end):
    origin = 'https://stabbingwithasyringe.home.blog/'
    chapterlist = []
    for i in range(start, end+1):
        if i == 100:
            url = origin + 'mage-tower-management-prologue/'
            chapterlist.append(url)
        elif i == 815:
            url = origin + "translations/tower-dungeon-management/" + \
                "mage-tower-management-epilogue/"
            chapterlist.append(url)
        else:
            url = origin + "translations/tower-dungeon-management/" + \
                "mage-tower-management-volume-" + str(start)[0] + \
                "-chapter-" + str(i)[1:].lstrip('0') + "/"
            chapterlist.append(url)
    return chapterlist


def clean(content):
    for i in content.find_all('script'):
        i.decompose()
    return content
