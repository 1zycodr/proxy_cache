from manager import StorageRepositoryManager


class Menu:
    title = '-' * 10 + ' Main Menu ' + '-' * 10
    manager = StorageRepositoryManager

    @classmethod
    def start(cls):
        while True:
            op = input(f'{cls.title}\n[1] - list\n[2] - get\n> ')

            if op == '1':
                cls.manager.show_videos()
            elif op == '2':
                cls.manager.show_video(
                    int(input('id: '))
                )
