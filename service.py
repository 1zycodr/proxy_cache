from video import Video
from cache import Cache
import json
import datetime


class Storage(object):
    _videos = []

    @classmethod
    def load(cls):
        with open('data.json', 'r') as file:
            data = json.loads(file.read())
            cls._videos = [
                Video.from_dict(video)
                for video in data['videos']
            ]

    @classmethod
    def save(cls):
        with open('data.json', 'w') as file:
            json.dump(
                {
                    'videos': [
                        video.to_dict()
                        for video in cls._videos
                    ]
                },
                file,
                ensure_ascii=False,
                indent=4
            )


class StorageRepository:
    __storage = Storage

    @classmethod
    def get_video(cls, id: int):
        for video in cls.__storage._videos:
            if video.id == id:
                return True, video.copy()
        return None, None

    @classmethod
    def list_videos(cls):
        return [
            video.copy()
            for video in cls.__storage._videos
        ]


class StorageRepositoryProxy:
    delta = datetime.timedelta(seconds=10)
    __storage_repo = StorageRepository
    __list_cache = None
    __get_cache = {}

    @classmethod
    def get_video(cls, id: int):
        data = cls.__get_cache.get(id)
        if not data or data.end_time <= datetime.datetime.now():
            cls.__get_cache[id] = Cache(
                cls.__storage_repo.get_video(id),
                datetime.datetime.now() + cls.delta
            )

        return cls.__get_cache.get(id).data

    @classmethod
    def list_videos(cls):
        if not cls.__list_cache\
           or cls.__list_cache.end_time <= datetime.datetime.now():
            cls.__list_cache = Cache(
                cls.__storage_repo.list_videos(),
                datetime.datetime.now() + cls.delta
            )
        return cls.__list_cache.data


if __name__ == '__main__':
    Storage.load()
