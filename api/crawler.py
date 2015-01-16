# coding=utf-8

import re
import json
import os.path
import logging
from datetime import datetime
from requests_oauthlib import OAuth1Session

from models import AirCondition, AirAverage
from leda import settings

# From https://twitter.com/Guangzhou_Air/following
CITYS = {
    'Guangzhou_Air': 'Guangzhou',
    'BeijingAir': 'Beijing',
    'Shenyang_Air': 'Shenyang',
    'CGChengduAir': 'Chengdu',
}

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

logger = logging.getLogger('crawler')


class SinceId(object):
    """Creating a file to save since id"""
    def __init__(self, fname='since_id.json'):
        self._module_path = os.path.dirname(__file__)
        self._file_path = os.path.join(self._module_path, fname)
        self._ids = self._recover()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._save()

    def __getitem__(self, item):
        if not self._ids:
            return None
        return self._ids.get(item)

    def __setitem__(self, key, value):
        self._ids[key] = value

    def _save(self):
        if not self._ids:
            return
        with open(self._file_path, mode='w') as f:
            json.dump(self._ids, f)

    def _recover(self):
        """Recovery `since_id` from file"""
        if os.path.isfile(self._file_path):
            with open(self._file_path) as f:
                json_data = json.load(f)
                return json_data
        return dict()


def get_datetime(s):
    return datetime.strptime(s, "%m-%d-%Y %H:%M")


def get_timeline(username, since_id=None, count=0):
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
    }
    if since_id:
        params.update(since_id=since_id)
    if count:
        params.update(count=count)
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
        logger.debug("No data")
        return nodata.groupdict()
    logger.warning("Fail to match tweet")
    logger.warning(text)
    return None


def crawl(since_id, city, count=200):
    logger.debug("Start crawling {}".format(city))
    tweets = get_timeline(city, since_id=since_id[city], count=count)
    for tweet in tweets:
        logger.debug(tweet['text'])
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
                air = AirCondition(pm2_5=float(-1.0), aqi=int(-1), time=get_datetime(msg.get('time')),
                                   level=-1)
            # unknown
            else:
                break
            air.save()
            logger.debug('New data saved.')
    # save since_id after success
    if tweets:
        # since_id.save(city, tweets[0]['id'])
        since_id[city] = tweets[0]['id']
        logger.debug("{}: {}".format(city, tweets[0]['id']))
    logger.debug('done')


def run():
    with SinceId() as since_id:
        for city in CITYS.keys():
            crawl(since_id, city, 2)
