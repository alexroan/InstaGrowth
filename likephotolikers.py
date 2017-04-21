"""
like likers photos bot

uses hashtags to:
	get photos,
	get the likers of those photos,
	like the first photo of the liker
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

for hashtag in args.t:
	print("hashtag: %s" % hashtag)
	medias = bot.get_hashtag_medias(hashtag)
	for media in medias:
		print("media: %s" % media)
		likers = bot.get_media_likers(media)

		##likes whole feed
		#bot.like_users(likers)
		
		for liker in likers:			
			user_info = bot.get_user_info(liker)
			print("liker: %s" % user_info['username'])
			liker_medias = bot.get_user_medias(liker)
			if len(liker_medias) > 0:
				bot.like(liker_medias[0])
		

bot.logout()