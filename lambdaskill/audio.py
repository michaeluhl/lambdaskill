import enum


class PLAY_BEHAVIOR(enum):
    ENQUEUE = "ENQUEUE"
    REPLACE_ALL = "REPLACE_ALL"
    REPLACE_ENQUEUED = "REPLACE_ENQUEUED"


class AudioStream(object):

    def __init__(self, url, token, expected_previous_token=None, offset=0):
        self.url = url
        self.token = token
        self.expected_previous_token = expected_previous_token
        self.offset = offset

    def prepare(self):
        return {
            'stream': {
                'url': self.url,
                'token': self.token,
                'expectedPreviousToken': self.expected_previous_token
                'offset': self.offset
            }
        }
