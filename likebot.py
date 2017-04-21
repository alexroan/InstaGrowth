"""
basic bot

uses hashtags to:
	likes photos
"""

import os
import sys
import time
import argparse

from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-t', type=str, nargs='+', help="tags")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

while True:
	for hashtag in args.t:
		bot.like_hashtag(hashtag, 10)
