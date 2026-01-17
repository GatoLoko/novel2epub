#!/usr/bin/env python3

# Copyright (C) 2016 GatoLoko
# Crated on Sat Nov 12 16:41:00 2016
# Author: GatoLoko.

import argparse
import os
import sys
from pathlib import Path, PurePath

import psutil

from libs import common
from libs.gs_epub import MyBook

PROG_DIR = Path(__file__).resolve().parent
sys.path.append(str(PurePath(PROG_DIR).joinpath("Novels")))
sys.path.append(str(PurePath(PROG_DIR).joinpath("Novels", "Complete")))


class Config:
    """Config.

    Config stores variables that need to be available to multiple functions
    """

    novel: str
    volume: int
    debug: bool
    labels: list[str]


config = Config


def arguments() -> None:
    """Manage all supported arguments."""
    parser = argparse.ArgumentParser(
        description="Download web stories and stores them as epub.",
        epilog="This script doesn't support actualizing an existing epub"
        " with new chapters, so it regenerates them from scratch.",
        argument_default=argparse.SUPPRESS,
    )
    parser.add_argument(
        "novel",
        metavar="novel",
        type=str,
        help="Which novel you want to get",
    )
    parser.add_argument(
        "volume",
        metavar="volume",
        type=int,
        help="Which volume to get",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="Print debug messages to stdout",
    )
    parser.add_argument(
        "labels",
        metavar="labels",
        nargs="*",
        help="Labels to add as metadata to the epub",
    )
    parsed_args = parser.parse_args()
    config.novel = parsed_args.novel
    config.volume = parsed_args.volume
    config.debug = parsed_args.debug
    if hasattr(parsed_args, "labels"):
        config.labels = parsed_args.labels

    if parsed_args.debug:
        print(parsed_args)
        memory = psutil.Process(os.getpid()).memory_info()[0] / float(2**20)
        print(f"Used memory: {round(memory, 1)} MB")


def main() -> None:
    try:
        novel = __import__(config.novel)
        common.novel_module = config.novel
        print(f"Loaded {config.novel} module")
    except ImportError:
        print("Unsupported novel")
        raise

    volume = novel.volumes[str(config.volume)]
    print(f"Volume start: {volume.first}")
    print(f"Volume end: {volume.last}")
    chapterlist = novel.genlist(volume.first, volume.last)
    fill = "0" if config.volume < 10 else ""
    title = novel.title + fill + volume.title
    # Remove from the file name those characters that FAT does NOT allow, so we
    # can transfer the file to a phone's or tablet's sdcard: \/:*?"<>|
    for i in ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]:
        if i in title:
            title = title.replace(i, "")
    filename = title + ".epub"
    print("Title: " + title)
    print("Chapters: " + str(len(chapterlist)))
    print("Filename: " + filename)

    identifier = f"novel2epub/{config.novel}/{novel.title}/volume.last"
    language = "en"

    book = MyBook(identifier, title, language, "novel2epub")

    if config.labels:
        book.add_labels(config.labels)

    # Add a cover if it's available
    book.add_cover(Path(PROG_DIR).joinpath(novel.cover_file))

    for i in chapterlist:
        if config.debug:
            print(i)
        ch_title, ch_file, ch_text = common.get_chapter(i)
        book.add_chapter(ch_title, ch_file, language, ch_text)

    # Define CSS style
    # with open(os.path.join(PROG_DIR, "CSS/nav.css")) as style_nav:
    with Path(PROG_DIR).joinpath("CSS", "nav.css").open() as style_nav:
        book.add_nav_style(style_nav.read())
    # with open(os.path.join(PROG_DIR, "CSS/body.css")) as style_body:
    with Path(PROG_DIR).joinpath("CSS", "body.css").open() as style_body:
        book.add_body_style(style_body.read())

    # Introduction
    book.add_intro(
        novel.author,
        novel.origin,
        novel.synopsis_text,
        Path(PROG_DIR).joinpath("HTML", "intro.xhtml"),
    )

    # Define Table of Contents, NCX, Nav and book spine
    book.finalize()

    if config.debug:
        print(config)
        mem = psutil.Process(os.getpid()).memory_info()[0] / float(2**20)
        print(f"Used memory: {round(mem, 1)} MB")

    book.write(filename)


if __name__ == "__main__":
    arguments()
    main()
