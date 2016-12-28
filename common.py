#!/usr/bin/env python3

# Copyright (C) 2016 GatoLoko
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
Created on 28/12/16

@author: GatoLoko
"""

import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import socket


def get_html(url):
    tryes = 5
    html = ""
    while tryes > 0:
        try:
            # TODO: Add support for compressed content
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Linux x86_64)')
            request = urllib.request.urlopen(req)
            html = BeautifulSoup(request.read(), "lxml")
            break
        except socket.timeout:
            tryes -= 1
        except urllib.error.URLError as error:
            if isinstance(error.reason, socket.timeout):
                tryes -= 1
            else:
                print("URL error: " + error.reason)
                quit()
    return html

