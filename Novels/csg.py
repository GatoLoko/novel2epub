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
Created on 04/11/18

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1', 1, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 400),
           '5': Volume('5', 401, 500),
           '6': Volume('6', 501, 600),
           '7': Volume('7', 601, 700),
           '8': Volume('8', 701, 800),
           '9': Volume('9', 801, 900),
           '10': Volume('10', 901, 1000),
           '11': Volume('11', 1001, 1100),
           '12': Volume('12', 1101, 1200),
           '13': Volume('13', 1201, 1300),
           '14': Volume('14', 1301, 1400),
           '15': Volume('15', 1401, 1500),
           '16': Volume('16', 1501, 1600),
           '17': Volume('17', 1601, 1700),
           '18': Volume('18', 1701, 1800),
           '19': Volume('19', 1801, 1900),
           '20': Volume('20', 1901, 2000),
           '21': Volume('21', 2001, 2032),
           #
           '22': Volume('22', 2101, 2200),
           '23': Volume('23', 2201, 2300),
           }

origin = 'http://gravitytales.com/novel/chaotic-sword-god/'
author = 'Xin Xing Xiao Yao (心星逍遥)'
cover_file = 'Covers/chaotic-sword-god.jpg'
title = 'Chaotic Sword God - Vol'

synopsis_text = """
Jian Chen, the publicly recognized number one expert of the Jianghu. His skill
with the sword went beyond perfection and was undefeatable in battle, After a
battle with the exceptional expert Dugu Qiubai who had gone missing over a
hundred years ago, Jian Chen succumbed to his injuries and died.</p>

<p>After death, Jian Chen’s spirit was transmigrated into a completely foreign
world. Following an extremely fast growth, his enemies piled up one after
another before becoming gravely injured once more. On the gates of death, his
spirit had mutated, and from that moment henceforth, he would tread on a
completely different path of the art of the sword to become the sword god of
his generation.</p>

<p>Strength System, from low to high — Saint, Great Saint, Saint Master, Great
Saint Master, Earth Saint Master, Heaven Saint Master, Saint Ruler, Saint King,
Saint Emperor.</p>

<p>A Xuanhuan webnovel.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + "csg-chapter-" + str(i)
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
