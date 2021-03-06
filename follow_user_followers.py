"""
    instabot example

    Workflow:
        Follow user's followers by username.
"""

import sys
import os
import time
import random
from tqdm import tqdm
import argparse

sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-proxy', type=str, help="proxy")
parser.add_argument('users', type=str, nargs='+', help='users')
args = parser.parse_args()

bot = Bot(filter_users=False, follow_delay=60, unfollow_delay=60)
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

for username in args.users:
    bot.follow_followers(username)
