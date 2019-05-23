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
import re

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
           '13': Volume('13', 1201, 1240),
           #
           '14': Volume('14', 1301, 1400),
           '15': Volume('15', 1401, 1500),
           '16': Volume('16', 1501, 1600),
           '17': Volume('17', 1601, 1640),
           '18': Volume('18', 1701, 1800),
           '19': Volume('19', 1801, 1900),
           '20': Volume('20', 1901, 2000),
           '21': Volume('21', 2001, 2100),
           '22': Volume('22', 2101, 2200),
           '23': Volume('23', 2201, 2300),
           }

origin = 'http://gravitytales.com/novel/peerless-battle-spirit/'
author = 'Supreme Villain (极品妖孽)'
cover_file = 'Covers/peerless-battle-spirit.jpg'
title = 'Peerless Battle Spirit - Vol'

synopsis_text = """
<strong>RAW Synopsis</strong></p>

<p>A young master of a clan started out with a useless Martial Spirit. However,
he coincidentally ended up awakening the atavistically-mysterious Divine Battle
Spirit. Since then, he began climbing to the top starting from the very bottom,
stumbling into glamorous beauties while crushing every genius he encounters
under his feet.</p>

<p>"There is none He does not fight against, and none He does not win
against!"</p>

<p><strong>Translator's Synopsis</strong></p>

<p>In the Canglan Continent, there existed a rule: only those who managed to
awaken a Martial Spirit were able to pursue the path of cultivation, and a
Martial Spirit's rank was determined when it was awakened. Born in Linshui
City, Qin Nan was a peerless genius who possessed great talents and was highly
anticipated to become a great cultivator in the future. However, things changed
when he ended up awakening the lowest-grade Martial Spirit, resulting in him
being considered trash.</p>

<p>Fortunately, when Qin Nan was struck by a ray of lightning at a young age,
he coincidentally obtained the atavistic Divine Battle Spirit, which was
capable of ranking up, breaking the ultimate rule of the Canglan Continent.
Little did he know that his Martial Spirit possessed a great secret, which
would continue to be unveiled as he learns more about the story of the Divine
Battle Spirit.</p>

<p>What is the secret behind the Divine Battle Spirit? What is the curse of the
Canglan Continent? Who exactly is the Divine God of Battle?</p>

<p>Join Qin Nan and his companions along their journey, battling against
various opponents, outsmarting their enemies, and seeking the answers to unveil
mysteries!</p>

<p>“Master, please bring me along on your journey battling against the Nine
Heavens, will you?”
"""


def genlist(start, end):
    global origin
    chapterlist = []
    for i in range(start, end+1):
        if i not in [295, 773]:
            url = origin + "pbs-chapter-" + str(i)
            if i == 296:
                url = origin + "pbs-chapter-295"
            chapterlist.append(url)
    return chapterlist


def clean(content):
    credline = re.compile(r'(Translator:.*)|(Editor:.*)|(XephiZ)|(DOCuinn)')
    for i in content.find_all(text=credline):
        i.replaceWith('')
    for i in content.find_all('hr'):
        i.decompose()
    return content
