import twint
from datetime import datetime, timedelta


def f_access():
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
    print('==============================================================')
    print("View in Web application navigate to view_web_app then run it")
    print('==============================================================')


if __name__ == '__main__':
    f_access()
