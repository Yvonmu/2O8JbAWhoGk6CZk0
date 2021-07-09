# import twint
# from datetime import datetime, timedelta
#
# three_days_ago = (datetime.now() - timedelta(3)).strftime('%Y-%m-%d')
#
# # type keywords you want
# keywords = ["request for startup"]
#
# # loop for the keywords
# for words in keywords:
#     # Configure
#     c = twint.Config()
#     c.Since = three_days_ago
#     c.Search = words
# #     c.Format = "Username: @{username} | Tweet id: {id} | Tweet: {tweet} | Date: {date} | Time: {time} \n"
#     c.Format = "User: {username} | Date: {date} |Tweet: {tweet} |Likes: {likes} |RT: {retweets} |Replies: {replies} \n "
#
#     # add this lines to your script
#     c.Store_csv = True
#     # here you can filter the needed columns (optional)
#     # c.Custom_csv = ["id", "user_id", "username", "tweet"]
#     c.Custom_csv = ['author', 'Date', 'tweet','Likes', 'retweets', 'Discussions']
#     # here name your output
#     csv_file = open(words + ".csv", 'a+')
#     c.Output = words + ".csv"
#
#     twint.run.Search(c)

import twint
from datetime import datetime, timedelta
c = twint.Config()
three_days_ago = (datetime.now() - timedelta(3)).strftime('%Y-%m-%d')
search_key = "request for startup"
c.Search = search_key
c.Since = three_days_ago
c.Format = "User: @{username} | Date: {date} |Tweet: {tweet} |Likes: {likes} |RT: {retweets} |Replies: {replies} \n "
c.Store_csv = True
c.Custom['tweet'] = ['username', 'date', 'tweet','likes_count', 'retweets_count', 'replies_count']
c.Output = search_key + ".csv"
twint.run.Search(c)
