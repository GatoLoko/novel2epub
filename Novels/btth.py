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

volumes = {'1': Volume('1', 1, 99),
           '2': Volume('2', 100, 199),
           '3': Volume('3', 200, 299),
           '4': Volume('4', 300, 399),
           '5': Volume('5', 400, 499),
           '6': Volume('6', 500, 599),
           '7': Volume('7', 600, 699),
           '8': Volume('8', 700, 799),
           '9': Volume('9', 800, 899),
           '10': Volume('10', 900, 999),
           '11': Volume('11', 1000, 1099),
           '12': Volume('12', 1100, 1199),
           '13': Volume('13', 1200, 1299),
           '14': Volume('14', 1300, 1399),
           '15': Volume('15', 1400, 1499),
           '16': Volume('16', 1500, 1526),
           }

origin = 'http://www.wuxiaworld.com/btth-index/'
author = 'Heavenly Silkworm Potato (天蚕土豆)'
cover_file = 'Covers/btth.jpg'
title = 'Battle through the heavens - Vol'

synopsis_text = """
In a land where no magic is present. A land where the strong make the rules
and the weak have to obey. A land filled with alluring treasures and beauty,
yet also filled with unforeseen danger. Three years ago, Xiao Yan, who had
shown talents none had seen in decades, suddenly lost everything. His powers,
his reputation, and his promise to his mother. What sorcery has caused him to
lose all of his powers? And why has his fiancee suddenly shown up?
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        url = origin + 'btth-chapter-' + str(i)
        chapterlist.append(url)
    return chapterlist
