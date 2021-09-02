from service import Storage
from menu import Menu


def main():
    Storage.load()
    Menu.start()


if __name__ == '__main__':
    main()
