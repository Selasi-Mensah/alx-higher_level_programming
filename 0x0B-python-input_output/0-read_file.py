#!/usr/bin/python3
"""``read_file`` module"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")