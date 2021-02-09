# -*- coding: utf-8 -*-
import datetime

import attr


class Twitter:

    def __init__(self, peony_client):
        self.client = peony_client

    async def get_tweets(self, screen_name, n_tweets=500,
                         include_rts=True, exclude_replies=True):
        api = self.client.api.statuses.user_timeline
        responses = api.get.iterator.with_max_id(
            screen_name=screen_name,
            count=200,
            include_rts=include_rts,
            exclude_replies=exclude_replies
        )
        user_tweets = []

        async for tweets in responses:
            user_tweets.extend(tweets)
            if len(user_tweets) >= n_tweets:
                user_tweets = user_tweets[:n_tweets]
                break

        return user_tweets

    def parse_medias_from_tweets(self, tweets):
        for tweet in tweets:
            medias = []
            for media in self.parse_medias_from_tweet(tweet):
                media.append(media)
            yield medias

    def parse_medias_from_tweet(self, tweet):
        media_sizes = ('large', 'medium', 'small', 'thumb')
        text = tweet.get('text', '')
        created_at_s = tweet['created_at']
        created_at = datetime.datetime.strptime(
            created_at_s, '%a %b %d %H:%M:%S %z %Y'
        )
        extended_entities = tweet.get('extended_entities', {}).get('media', [])
        entities = tweet['entities'].get('media', [])
        if len(extended_entities) > 0:
            entities = extended_entities

        for entity in entities:
            sizes = entity['sizes']
            size = sorted(sizes.keys(), key=lambda x: media_sizes.index(x))[0]
            origin_url = entity['expanded_url']
            media_url = entity['media_url_https']
            media_url = '{url}:{size}'.format(url=media_url, size=size)
            yield Media(origin_url=origin_url, media_url=media_url,
                        text=text, created_at=created_at)


async def get_user_medias(peony_client, screen_name, n_tweets=100):
    twitter = Twitter(peony_client)
    tweets = await twitter.get_tweets(screen_name, n_tweets=n_tweets)
    medias = twitter.parse_medias_from_tweets(tweets)
    return list(medias)


@attr.s
class Media:
    origin_url = attr.ib()
    media_url = attr.ib()
    text = attr.ib()
    created_at = attr.ib()
