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
import gzip
from io import BytesIO


# List of User-Agent strings we may want to try
minimum = 'Mozilla/5.0 (Linux x86_64)'

# Woxter QX95
# Mozilla/5.0 (Linux; Android 4.4.2; Woxter QX95 Build/KOT49H)
#     AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0
#     Safari/537.36
qx95 = 'Mozilla/5.0 (Linux; Android 4.4.2; Woxter QX95 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Safari/537.36'

# Webview (KitKat & Lolipop)
# Mozilla/5.0 (Linux; Android 4.4; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36
#     (KHTML, like Gecko) Version 4.0 Chrome/30.0.0.0 Mobile Safari/537.36

# Nexus 5 WebView (nuevo):
# Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv)
#     AppleWebKit/537.36 (KHTML, like Gecko) Version 4.0 Chrome/43.0.2357.65
#     Mobile Safari/537.36

user_agent = qx95


def get_html(url):
    tryes = 5
    html = ""
    # Build our request
    req = urllib.request.Request(url)
    # Accept gziped content
    req.add_header('Accepting-encoding', 'gzip')
    # Fake user aggent
    req.add_header('User-Agent', user_agent)
    while tryes > 0:
        try:
            request = urllib.request.urlopen(req)
            break
        except socket.timeout:
            tryes -= 1
        except urllib.error.URLError as error:
            if isinstance(error.reason, socket.timeout):
                tryes -= 1
            else:
                print("URL error: " + error.reason)
                quit()
    if request.info().get('Content-Encoding') == 'gzip':
        buf = BytesIO(request.read())
        f = gzip.GzipFile(fileobj=buf)
        html = BeautifulSoup(f.read(), 'lxml')
    else:
        html = BeautifulSoup(request.read(), "lxml")
    request.close()
    return html


def get_image(cover_url, referer):
    # print(cover_url)
    tries = 5
    while tries > 0:
        try:
            req = urllib.request.Request(cover_url)
            # Accept gziped content
            req.add_header('Accepting-encoding', 'gzip')
            # Fake user agent
            req.add_header('User-agent', 'Mozilla/5.0 (Linux x86_64)')
            # Referer?
            req.add_header('referer', referer)
            request = urllib.request.urlopen(req)
            if request.info().get('Content-Encoding') == 'gzip':
                buf = BytesIO(request.read())
                temp = gzip.GzipFile(fileobj=buf)
            else:
                temp = request.read()
            with open('cover.jpg', 'wb') as f:
                f.write(temp)
            tries = 0
            # break
            return 1
        except Exception as error:
            tries -= 1
            print("Can't retrieve the image")
            print(error)
            return 0
