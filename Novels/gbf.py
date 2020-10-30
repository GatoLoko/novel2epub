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

volumes = {'1': Volume('1', 0, 100),
           '2': Volume('2', 101, 200),
           '3': Volume('3', 201, 300),
           '4': Volume('4', 301, 318),
           }

origin = 'http://www.wuxiaworld.co/Jikuu-Mahou-de-Isekai-to-Chikyuu-wo-Ittarikitari/'
author = 'Katsu'
cover_file = 'Covers/gbf.jpg'
title = 'Going Back and Forth Between Earth and The Other World with Space Time Magic - Vol'

synopsis_text = """
Though he received the skills necessary to teleport across worlds, the king who
performed the summoning ritual attempted to trick him into wearing a slavery
collar, this annoyed him so he kidnapped the princess and returned to
Earth.</p>

<p>While traveling between worlds with the skills he received, together with
the kidnapped Princess and his little sister, they lived happily ever after?
"""


def genlist(start, end):
    global origin
    list_page = common.get_html(origin)
    chapterlist = []
    for i in range(start, end+1):
        # print(i)
        text = '^Chapter %s – .*' % str(i)
        link = list_page.find('a', text=re.compile(text))
        url = origin + link['href'].split("/")[-1]
        chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'Translator:.*Editor:.*')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    return content
