"""
follow then unfollow another user's followers

use a username to:
	get their id
	use id to get all their followers
	follow each one (save for later)
	like some photos
	unfollow each one after 48 hours

"""

import os
import sys
import time
import argparse
from queue import Queue
from datetime import datetime

from instabot import Bot

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-u', type=str, help="username")
parser.add_argument('-p', type=str, help="password")
parser.add_argument('-user', type=str, help="tags")
parser.add_argument('-proxy', type=str, help="proxy")
args = parser.parse_args()

bot = Bot()
bot.login(username=args.u, password=args.p,
          proxy=args.proxy)

#wait time of 48 hours
wait_time = 48 * 60 * 60
#queue of followed users
q = Queue()

userid = bot.get_userid_from_username(args.user)
followers = bot.get_user_followers(userid)
start_time = datetime.now()

for follower in followers:

	username = bot.get_user_info(follower)['username']
	print("Trying to follow: %s" % username)
	#follow user
	if bot.follow(follower) == True:
		print("Followed: %s" % username)
		print("Trying to like media from: %s" % username)
		#like media from user
		if bot.like_user(follower) == True:
			print("Liked media from: %s" % username)
		else:
			print("Could not like media from %s" % username)
		#if just starting, set timer
		if q.empty() == True:
			start_time = datetime.now()
		q.put(follower)
	else:
		print("Could not follow: %s" % username)


	current_time = datetime.now()
	delta_time = current_time - start_time;
	#if wait is longer than wait time, unfollow first in queue
	if delta_time.total_seconds() >= wait_time:
		queued_user = q.get()
		username = bot.get_user_info(queued_user)['username']
		print("Trying to unfollow: %s" % username)
		if bot.unfollow(queued_user) == True:
			print("Unfollowed: %s" % username)
		else:
			print("Could not unfollow: %s" % username)

bot.logout()


