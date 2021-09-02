class Video:
    def __init__(self, id, title="youtube", link="youtube.com"):
        self.id = id
        self.title = title
        self.link = link

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'link': self.link
        }

    def copy(self):
        return Video(
            self.id,
            self.title,
            self.link
        )

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def __str__(self):
        return f'[{self.id}] - {self.title}\n\tLink: {self.link}\n'


if __name__ == '__main__':
    v = Video(1)
    v2 = v.copy()
    print(id(v))
    print(id(v2))
