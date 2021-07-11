# 2O8JbAWhoGk6CZk0
##searches Twitter for the term request for startup
This is a software that searches Twitter for the term "request for startup" and extracts information, in other words tweets, then stores this information in a very simple file format, such as a CSV file or a simple text file, and displays results in a simple web interface. It Sort by total number of retweets, likes, and discussions and then date in descending order.

## Setup
To run this project, install this:
TWINT - Twitter Intelligence Tool [click here link](https://github.com/twintproject/twint)

You might want to edit twint/tweet.py adding your field, and twint/storage/write_meta.py to let it be saved into the output file

##Install Flask
[click here link](https://phoenixnap.com/kb/install-flask)

##Example
twint help us to search for term on twitter
```
import twint
from datetime import datetime, timedelta

c = twint.Config()
three_days_ago = (datetime.now() - timedelta(3)).strftime('%Y-%m-%d')
search_key = "request for startup"
c.Search = search_key
c.Since = three_days_ago
c.Format = "User: @{username} | Date: {date} |Tweet: {tweet} |Likes: {likes} |RT: {retweets} |Replies: {replies} " \
           "\n "
c.Store_csv = True
c.Custom['tweet'] = ['username', 'date', 'tweet', 'likes_count', 'retweets_count', 'replies_count']
c.Output = search_key + ".csv"
twint.run.Search(c)

```
