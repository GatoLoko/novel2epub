#!/usr/bin/env python3
# Copyright (C) 2016 GatoLoko

"""
Crated on Sat Nov 12 16:41:00 2016
@author: GatoLoko
"""

import os
import argparse
import psutil
import sys
PROG_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(PROG_DIR, "libs"))
sys.path.append(os.path.join(PROG_DIR, "Novels"))
sys.path.append(os.path.join(PROG_DIR, os.path.join("Novels", "Complete")))
try:
    import common
    from gs_epub import MyBook
except ImportError:
    raise


def arguments():
    parser = argparse.ArgumentParser(
        description="Download web stories and stores them as epub.",
        epilog="This script doesn't support actualizing an existing epub" +
               " with new chapters, so it regenerates them from scratch.",
        argument_default=argparse.SUPPRESS)
    parser.add_argument('novel', metavar='novel', type=str,
                        help='Which novel you want to get')
    parser.add_argument('volume', metavar='volume', type=int,
                        help="Which volume to get")
    parser.add_argument('-d', '--debug', action='store_true', default=False,
                        help='Print debug messages to stdout')
    parser.add_argument('labels', metavar='labels', nargs='*',
                        help='Labels to add as metadata to the epub')
    args = parser.parse_args()

    if args.debug:
        print(args)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2 ** 20)
        print("Used memory: %s MB" % round(mem, 1))

    return args


if __name__ == "__main__":

    args = arguments()

    try:
        novel = __import__(args.novel)
        common.novel_module = args.novel
        print("Loaded %s module" % args.novel)
    except ImportError:
        print("Unsuported novel")
        raise

    volume = novel.volumes[str(args.volume)]
    print("Volume start: %s" % volume.first)
    print("Volume end: %s" % volume.last)
    chapterlist = novel.genlist(volume.first, volume.last)
    fill = ''
    if args.volume < 10:
        fill = '0'
    title = novel.title + fill + volume.title
    # Remove from the file name those characters that FAT does NOT allow, so we
    # can transfer the file to a phone or tablet sdcard: \/:*?"<>|
    for i in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if i in title:
            title = title.replace(i, '')
    filename = title + ".epub"
    print("Title: " + title)
    print("Chapters: " + str(len(chapterlist)))
    print("Filename: " + filename)

    identifier = "novel2epub/%s/%s/%s" % (args.novel, novel.title, volume.last)
    language = 'en'

    book = MyBook(identifier, title, language, 'novel2epub')

    if hasattr(args, 'labels'):
        book.add_labels(args.labels)

    # Add a cover if it's available
    book.add_cover(os.path.join(PROG_DIR, novel.cover_file))

    for i in chapterlist:
        if args.debug:
            print(i)
        ch_title, ch_file, ch_text = common.get_chapter(i)
        book.add_chapter(ch_title, ch_file, language, ch_text)

    # Define CSS style
    with open(os.path.join(PROG_DIR, "CSS/nav.css")) as style_nav:
        book.add_nav_style(style_nav.read())
    with open(os.path.join(PROG_DIR, "CSS/body.css")) as style_body:
        book.add_body_style(style_body.read())

    # Introduction
    book.add_intro(novel.author, novel.origin, novel.synopsis_text,
                   os.path.join(PROG_DIR, 'HTML/intro.xhtml'))

    # Define Table of Contents, NCX, Nav and book spine
    book.finalize()

    if args.debug:
        print(args)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2 ** 20)
        print("Used memory: %s MB" % round(mem, 1))

    book.write(filename)
