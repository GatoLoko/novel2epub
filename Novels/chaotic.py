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

import common
import re
Volume = common.Volume

volumes = {'1': Volume('1', 1, 50),
           '2': Volume('2', 51, 100),
           '3': Volume('3', 101, 150),
           '4': Volume('4', 151, 200),
           '5': Volume('5', 201, 250),
           '6': Volume('6', 251, 289),
           #
           '7..': Volume('5', 301, 349),
           '8..': Volume('5', 351, 400),
           '9..': Volume('5', 401, 449),
           '10.': Volume('5', 450, 500),
           '11.': Volume('5', 501, 549),
           '12.': Volume('5', 551, 600),
           '13.': Volume('5', 601, 649),
           '14.': Volume('5', 651, 700),
           '15.': Volume('5', 701, 749),
           '16.': Volume('5', 751, 800),
           '17.': Volume('5', 801, 849),
           '18.': Volume('5', 851, 900),
           '19.': Volume('5 - END', 901, 954),
           }

origin = 'http://www.wuxiaworld.co/Chaotic-Lightning-Cultivation/'
author = 'Xie Zi Ban (写字板)'
cover_file = 'Covers/chaotic-lightning-cultivation.jpg'
title = 'Chaotic Lightning Cultivation - Vol'

synopsis_text = """
His parents were the geniuses of the sect. But they were apparently killed
while on a mission when he was barely 6. As he apparently did not excel in
any of the 5 elements, in fact, all 5 elements are in balance in his body.
Thus, our fatty is deemed to be trash and does not deserve the respect his
parents had.</p>

<p>He is allowed to have one task, to collect garbage of the sect until he
reaches the initial test-age where he has to proof to be worthy to stay in
the sect.<br/>
Our fatty has no choice but to cultivate the only heritage his parents gave
him. A mysterious black pearl.</p>

<p>Unfortunately for him, this pearl seems to be only useful for… collecting
garbage…</p>

<p><strong>Original Synopsis:</strong></p>

<p>A Little Fatty who was constantly bullied in his sect, by relying on the
Magical Artifact his parents left behind, cultivated the peerless, primally
chaotic Five Elements Lightning technique. Using this, he slowly rose and
dominated the continents. 10th Step Water Divine Lighting, 3rd Step Fire
Divine Lightning, 5th Step Earth Divine Lighting, 7th Step Metal Divine
Lighting, Lesser 5 Element Soul Divine Lighting, Greater 5 Element
Destruction Divine Lighting, Dark Purple Divine Lighting, Pure Divine
Lighting, Clear Sky Divine Lighting, Righteous Taichi Divine Lightning.</p>

<p>A monk once said, “One who has dissatisfactions should get struck by all 5
bolts of lightning”
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        text = "Chapter %s: " % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = "%s%s" % (origin, link['href'])
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
