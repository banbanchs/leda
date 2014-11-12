# coding=utf-8

import re
import os.path
import logging
from datetime import datetime
from requests_oauthlib import OAuth1Session

from models import AirCondition, AirAverage
from leda import settings

# From http://aqicn.org/faq/2013-09-09/revised-pm25-aqi-breakpoints/
level_map = {
    'No data': -1,
    'Good': 1,
    'Moderate': 2,
    'Unhealthy for Sensitive Groups': 3,
    'Unhealthy': 4,  # 100 < value < 150
    'Very Unhealthy': 5,
    'Hazardous': 6,
    'Unknown': 7,
}


class SinceId(object):
    """Creating a file to save since id"""
    def __init__(self):
        self._module_path = os.path.dirname(__file__)
        self._file_path = os.path.join(self._module_path, 'since_id.txt')
        self._id = self._recover()

    def _save(self):
        with open(self._file_path, mode='w') as f:
            f.write(self._id)

    @property
    def value(self):
        return self._id

    def _recover(self):
        """Recovery `since_id` from file"""
        if os.path.isfile(self._file_path):
            with open(self._file_path) as f:
                since_id = f.readline()
            if since_id:
                return since_id.strip()
        return None

    def save(self, new_id):
        new_id = str(new_id)
        if self._id == new_id:
            return
        self._id = new_id
        self._save()


def get_datetime(s):
    return datetime.strptime(s, "%m-%d-%Y %H:%M")


def get_timeline(username, since_id=None, count=10):
    """Get the specified twitter user's timeline.

    :param username: The screen name of the user for whom to return results for.
    :type username: str
    :param since_id: Returns results with an ID greater than the specified ID.
    :type since_id: str or None
    :param count: Specifies the number of tweets to try and retrieve.
    :type count: int
    :rtype : list
    """
    twitter = OAuth1Session(client_key=settings.CLIENT_KEY, client_secret=settings.CLIENT_SECRET,
                            resource_owner_key=settings.ACCESS_TOKEN_KEY,
                            resource_owner_secret=settings.ACCESS_TOKEN_SECRET)
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {
        'screen_name': username,
        'count': count,
    }
    if since_id:
        params.update(since_id=since_id)
    r = twitter.get(url, params=params)
    return r.json()


def match(tweet=None):
    """Get the information we need in tweet and return the match group dict.

    :type tweet dict
    :rtype : dict
    """
    text = tweet['text']
    if 'avg' in text:
        pattern = re.compile(r'^(?P<from_time>\d{2}-\d{2}-\d{4}\s\d{2}:\d{2})\sto\s'
                             r'(?P<to_time>\d{2}-\d{2}-\d{4}\s\d{2}:\d{2});[^;]+;\s'
                             r'(?P<pm2_5>\d+\.\d);\s(?P<aqi>\d+);\s(?P<level>[^(]+)$', flags=re.UNICODE)
    else:
        pattern = re.compile(r'^(?P<time>\d{2}-\d{2}-\d{4}\s\d{2}:\d{2});\sPM2.5;\s(?P<pm2_5>\d+\.\d);\s'
                             r'(?P<aqi>\d+);\s(?P<level>[^(]+)', flags=re.UNICODE)
    data = re.match(pattern, text)
    if data:
        return data.groupdict()

    # try find out this tweet is "no data" or not
    nodata = re.match(r'(?P<time>\d{2}-\d{2}-\d{4}\s\d{2}:\d{2});\sPM2.5;\s(?P<info>No\sData)', text, flags=re.UNICODE)
    if nodata:
        logging.info("No data")
        return nodata.groupdict()
    logging.warning("Fail to match tweet")
    logging.warning(text)
    return None


def run():
    since_id = SinceId()
    tweets = get_timeline('Guangzhou_Air', since_id=since_id.value)
    print(len(tweets))
    if tweets:
        since_id.save(tweets[0]['id'])
    for tweet in tweets:
        msg = match(tweet)
        # if it match tweet, there are three condition: avg, hourly or nodata
        if msg:
            # hourly
            if 'aqi' in msg and 'time' in msg:
                air = AirCondition(pm2_5=float(msg.get('pm2_5')), aqi=int(msg.get('aqi')),
                                   time=get_datetime(msg.get('time')),
                                   level=level_map[msg.get('level').strip()])
            # 12h avg
            elif 'from_time' in msg:
                air = AirAverage(pm2_5=float(msg.get('pm2_5')), aqi=int(msg.get('aqi')),
                                 from_time=get_datetime(msg.get('from_time')), to_time=get_datetime(msg.get('to_time')),
                                 level=level_map[msg.get('level').strip()])
            # no data
            elif 'info' in msg:
                air = AirCondition(pm2_5=float(0.0), aqi=int(0), time=get_datetime(msg.get('time')),
                                   level=level_map[msg.get('info', 'No data').strip()])
            # unknown
            else:
                break
            air.save()
            logging.info('New data saved.')
    logging.debug('done')
