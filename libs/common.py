# Created on 28/12/2016
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

import re
import string

from bs4 import BeautifulSoup

from libs import gsweb

novel_module: str = ""

# Limit chapter file names to characters that wont cause problems.
VALID_CHARS = f"-_.() {string.ascii_letters}{string.digits}"


class Volume:
    def __init__(self, title: str, first: int, last: int) -> None:
        self.title = title
        self.first = first
        self.last = last


def get_html(url: str) -> BeautifulSoup:
    return gsweb.get_soup(url)


def get_wuxiaworld_com(html):
    html_title = html.find("title").text
    title_parts = html_title.split(" - ")
    chapter_title = " - ".join(title_parts[1:-1])
    if len(title_parts) == 3:
        chapter_title = title_parts[1]
    # Extract the main text DIV content and turn it into a string
    contents = html.find("div", "panel-default").find("div", "fr-view")
    # Site dependant cleanup
    # Remove links to previous and next chapter
    nav_links = re.compile(r"[\s]*(Previous|Next) Chapter[\s]*")
    for link in contents.find_all("a", text=nav_links):
        link.decompose()
    for link in contents.find_all("p", text=nav_links):
        link.decompose()
    return (chapter_title, contents)


def get_wuxiaworld_co(html):
    html_title = html.find("title").text
    chapter_title = html_title.split("_")[1].split(" - ")[0]
    # if len(title_parts) == 3:
    #    chapter_title = title_parts[1]
    # Site dependant cleanup
    # Extract the main text DIV content and turn it into a string
    contents = html.find("div", {"id": "section-list-wp"})
    paragline = re.compile(r".*&lt;/p&gt;&lt;p&gt;.*")
    for i in contents.find_all(text=paragline):
        istring = re.sub("&lt;/p&gt;&lt;p&gt;", "</p><p>", i)
        i.replaceWith(istring)
    credline = re.compile(r"Translator:.*Editor:.*")
    if contents.find(text=credline):
        contents.find(text=credline).replaceWith("")
    goto = re.compile(r"Please go to: http.* to read .* chapters for free.*")
    if contents.find(text=goto):
        contents.find(text=goto).replaceWith("")
    # Remove all scripts
    for script in contents.find_all("script"):
        script.decompose()
    return (chapter_title, contents)


def get_syringe(html):
    html_title = html.find("title").text
    title_parts = html_title.split(" – ")
    chapter_title = " - ".join(title_parts[0:-1])
    # Extract the main text DIV content and turn it into a string
    contents = html.find("div", "entry-content")
    # Site dependant cleanup
    for i in contents.find_all("h6", "has-background-color"):
        i.decompose()
    for i in contents.find_all("div", "aligncenter wpcnt"):
        i.decompose()
    for i in contents.find_all("div", "wpa"):
        i.decompose()
    for i in contents.find_all("script"):
        i.decompose()
    for i in contents.find_all("div", "sharedaddy"):
        i.decompose()
    for i in contents.find_all("div", id=re.compile("^atatags-")):
        i.decompose()
    for i in contents.find_all("p", "has-text-align-center"):
        i.decompose()
    credline = re.compile(r".*stabbingwithasyringe.*")
    for i in contents.find_all(text=credline):
        i.replaceWith("")
    adultline = re.compile(r"This chapter contains.*18\+.*Be aware\.")
    for i in contents.find_all(text=adultline):
        i.replaceWith("")
    stabbing = re.compile(r"stabbing.*blog|translator.*site")
    for i in contents.find_all(text=stabbing):
        i.replaceWith("")
    return (chapter_title, contents)


def clean_chapter_name(chapter_title: str) -> str:
    # Replace spaces with underscore
    chapter_file = f"{chapter_title.replace(' ', '_')}{'.xhtml'}"
    # Also replace non ascii "–" with "-"
    chapter_file = chapter_file.replace("–", "-")
    # Remove any remaining non-ascii character to avoid problems
    return "".join(c for c in chapter_file if c in VALID_CHARS)


def get_chapter(url):
    print("Processing: " + url)
    html = gsweb.get_soup(url)
    if "wuxiaworld.com" in url:
        chapter_title, contents = get_wuxiaworld_com(html)
    elif "wuxiaworld.co" in url:
        chapter_title, contents = get_wuxiaworld_co(html)
    elif "stabbingwithasyringe" in url:
        chapter_title, contents = get_syringe(html)
    else:
        exception_text = "Something went wront! Unsuported server!"
        raise SystemExit(exception_text)
    # Novel dependant cleanup
    try:
        print("Cleaning...")
        novel = __import__(novel_module)
        contents = novel.clean(contents)
        print("Clean")
    except ImportError:
        pass
    soup_str = "".join(map(str, contents))
    # Before turning the html into a soup, replace all weird chinese spaces
    # with actual spaces.
    soup_str = soup_str.replace("　", " ")
    # And replace double br tags with a paragraph break
    soup_str = re.sub(r"</br>", "", soup_str)
    soup_str = re.sub(r"<br/>[\t\n\r\f\v\s　]*<br/>", "\n<p>", soup_str)
    soup_str = re.sub(r"<br/>", "</p>\n<p>", soup_str)

    print(chapter_title)
    chapter_file = clean_chapter_name(chapter_title)
    print(chapter_file)
    # Then turn the string back into a soup
    soup_text = BeautifulSoup(soup_str, "lxml")
    # Remove all atributes from all tags
    for tag in soup_text.findAll(True):
        tag.attrs = {}
    # Remove empty paragraphs, including those which only contain br tags or
    # the weird space character (why the &·$% do you have a paragraph with
    # nothing?)
    for paragraph in soup_text.findAll(["span", "p"]):
        if not paragraph.text or paragraph.text in [" ", "。"]:
            paragraph.decompose()
    # Remove stray br tags
    # for br_tag in soup_text.findAll('br'):
    #     br_tag.decompose()
    # Turn the soup into text
    # text = str(soup_text)
    text = soup_text.prettify()

    # Undo some ridiculous censoring
    # text = damnit.sub('damn it', text)
    # text = damned.sub('damned', text)
    # text = fuck.sub('fuck', text)

    return chapter_title, chapter_file, text
