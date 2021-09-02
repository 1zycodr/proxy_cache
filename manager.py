from service import StorageRepositoryProxy, Storage


class StorageRepositoryManager:
    _service = StorageRepositoryProxy

    @classmethod
    def show_videos(cls):
        videos = StorageRepositoryProxy.list_videos()
        if videos:
            print('\n'.join([
                str(video)
                for video in videos
            ]))
        else:
            print('No videos!')

    @classmethod
    def show_video(cls, id):
        exists, video = StorageRepositoryProxy.get_video(id)

        if exists:
            print(video)
        else:
            print(f'No such video with id {id}\n')


if __name__ == '__main__':
    Storage.load()
    StorageRepositoryManager.show_videos()
    StorageRepositoryManager.show_video(2)
    StorageRepositoryManager.show_video(3)
    StorageRepositoryManager.show_video(4)
    StorageRepositoryManager.show_video(5)
    StorageRepositoryManager.show_video(2)
    StorageRepositoryManager.show_video(3)
    StorageRepositoryManager.show_video(4)
    StorageRepositoryManager.show_video(5)
