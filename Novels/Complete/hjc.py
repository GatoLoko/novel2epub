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
Created on 09/05/18

@author: GatoLoko
"""

import common
import re

Volume = common.Volume

volumes = {'1': Volume('1', 1, 27),
           '2': Volume('2', 28, 56),
           '3': Volume('3', 57, 84),
           '4': Volume('4', 85, 96),
           '5': Volume('5', 97, 100),
           '6': Volume('6', 101, 200),
           '7': Volume('7', 201, 300),
           '8': Volume('8', 301, 400),
           '9': Volume('9', 401, 500),
           '10': Volume('10', 501, 600),
           '11': Volume('11', 601, 700),
           '12': Volume('12', 701, 800),
           '13': Volume('13', 801, 848),
           }

origin = 'http://www.wuxiaworld.co/Heavenly-Jewel-Change/'
author = 'Tang Jia San Shao (唐家三少)'
cover_file = 'Covers/heavenly-jewel-change.jpg'
title = 'Heavenly Jewel Change - Vol'

synopsis_text = """
Every human has their Personal Jewel of power, when awakened it can either be
an Elemental Jewel or Physical Jewel. They circle the right and left wrists
like bracelets of power.</p>

<p>Heavenly Jewels are like the twins born, meaning when both Elemental and
Physical Jewels are Awakened for the same person, the pair is known as Heavenly
Jewels.</p>

<p>Those who have the Physical Jewels are known as Physical Jewel Masters, those
with Elemental Jewels are Elemental Jewel Masters, and those who train with
Heavenly Jewels are naturally called Heavenly Jewel Masters.</p>

<p>Heavenly Jewel Masters have a highest level of 12 pairs of jewels, as such
their training progress is known as Heavenly Jewels 12 Changes.</p>

<p>Our MC here is an archer who has such a pair of Heavenly Jewels.
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        text = '^%s .*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
