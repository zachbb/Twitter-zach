from twython import Twython
twitter = Twython()
# Some basic search functionality.
print(twitter.search(q='pythoncentral'))
