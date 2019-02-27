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
Created on 25/07/18

@author: GatoLoko
"""

from common import Volume

volumes = {'1': Volume('1',
                       1, 100),
           '2': Volume('2',
                       101, 200),
           '3': Volume('3',
                       201, 300),
           '4': Volume('4',
                       301, 400),
           '5': Volume('5',
                       401, 500),
           '6': Volume('6',
                       501, 603),
           '7': Volume('7',
                       601, 700),
           '8': Volume('8',
                       701, 800),
           '9': Volume('9',
                       801, 900),
           '10': Volume('10',
                        901, 1000),
           '11': Volume('11',
                        1001, 1100),
           '12': Volume('12',
                        1101, 1200),
           '13': Volume('13',
                        1201, 1300),
           '14': Volume('14',
                        1301, 1307),
           #
           '15': Volume('15',
                        1401, 1401),
           '16': Volume('16',
                        1501, 1501),
           '17': Volume('17',
                        1601, 1601),
           '18': Volume('18',
                        1701, 1701),
           '19': Volume('19',
                        1801, 1801),
           # 1841 is last chapter
           }

origin = 'http://www.wuxiaworld.com/novel/spirit-realm/'
author = 'Ni Cang Tian (逆蒼天)'
cover_file = 'Covers/spirit-realm.jpg'
title = 'Spirit Realm - Vol'

synopsis_text = """
Thirty thousand years ago, the Heaven Fighting Race who called themselves
“Gods” invaded Spirit Realm. Hundreds of races rose up in resistance, but
ultimately suffered a crushing defeat. The human race was the first to concede,
and the rest of the Hundred Races soon followed in succession.</p>

<p>During the subsequent ten thousand years, all of the races were enslaved by
the Heaven Fighting Race. They were cruelly treated, and lived beneath the
shadow of terror.</p>

<p>The Heaven Fighting Race’s march of conquest did not stop there. With Spirit
Realm as the starting point, they invaded other secret dimensions, and spread
war to all corners of existence. After greatly exhausting their combat
strength, they were finally defeated by the Hundred Races who took advantage of
this opportunity. With no other choice, they fled to the starry skies outside
the realm.</p>

<p>Thirty thousand years later, in an era where the Heaven Fighting Race has
already faded to become ancient legend, an amnesiac youth possessing the Heaven
Fighting Race’s bloodline is being fostered in an insignificant household.
Whilst struggling to live on, he silently awaits the day of the bloodline’s
awakening.
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i not in [833, ]:
            url = origin + "sr-chapter-" + str(i)
        #     url = origin + "ast-chapter-" + str(i)
        #     if i == 28:
        #         url = origin + "ast-chapter-28-1"
        #     elif i == 115:
        #         url = origin + "ast-chapter-5-1"
        #     elif i == 232:
        #         url = origin + "ast-chapter-232-part-1000"
        #     elif i in [246, 248]:
        #         url = origin + "ast-chapter-" + str(i) + "-part-1"
        #     elif i == 329:
        #         url = origin + "ast-chapter-329-part-4"
        #     elif i == 1421:
        #         url = origin + "chapter-1421"
        #     elif i == 1661:
        #         url = origin + "ast-chapter-16611"
            chapterlist.append(url)
    return chapterlist


def clean(content):
    return content
