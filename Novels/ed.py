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
Created on 22/12/18

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
           '21': Volume('21', 2001, 2100),
           '22': Volume('22', 2101, 2200),
           '23': Volume('23', 2201, 2300),
           '24': Volume('24', 2301, 2400),
           '25': Volume('25', 2401, 2500),
           '26': Volume('26', 2501, 2600),
           '27': Volume('27', 2601, 2700),
           '28': Volume('28', 2701, 2800),
           '29': Volume('29', 2801, 2900),
           '30': Volume('30', 2901, 3000),
           '31': Volume('31', 3001, 3100),
           '32': Volume('32', 3101, 3200),
           '33': Volume('33', 3201, 3300),
           '34': Volume('34', 3301, 3400),
           '35': Volume('35', 3401, 3500),
           '36': Volume('36', 3501, 3600),
           '37': Volume('37', 3601, 3700),
           '38': Volume('38', 3701, 3800),
           '39': Volume('39', 3801, 3900),
           '40': Volume('40', 3901, 4000),
           '41': Volume('41', 4001, 4100),
           '42': Volume('42', 4101, 4122),
           #
           '43': Volume('43', 4201, 4201),
           '44': Volume('44', 4301, 4301),
           '45': Volume('45', 4401, 4401),
           '46': Volume('46', 4501, 4501),
           # As of Mar 2021, there are 4300+ chapters in the original novel.
           }

origin = 'https://www.wuxiaworld.com/novel/emperors-domination/'
author = 'Yan Bi Xiao Sheng (厌笔萧生)'
cover_file = 'Covers/ed.jpg'
title = 'Emperor\'s domination - Vol'

synopsis_text = """
<strong>Bao’s Synopsis:</strong> A boy that was imprisoned for millions of
years had regained his mortal body. He became a disciple of the declining
Cleansing Incense Ancient Sect where its patriarch used to be his disciple.
Now, he will bring this sect back to its former glory.</p>

<p>This is his journey to reach the apex and take revenge on those who had
imprisoned him.</p>

<p>This is his story of meeting old friends and making new companions.</p>

<p>This is his path of traversing the Nine Worlds and becoming the next ruler
of the Heavens.</p>

<p><strong>Qidian’s Synopsis:</strong> Ten million years ago, Li Qiye planted a
simple water bamboo into the ground.Eight million years ago, Li Qiye had a koi
fish pet.Five million years ago, Li Qiye cared for a little girl....In the
present day, Li Qiye woke up from his slumber; the water bamboo reached the
apex of cultivation; the koi fish became a Golden Dragon; the little girl
became the Nine Worlds’ Immortal Empress.</p>

<p>This is a tale regarding an immortal human who was the teacher of the Demon
Saint, Heavenly Beast, and Immortal Empress.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + "emperor-chapter-" + str(i)
        chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
