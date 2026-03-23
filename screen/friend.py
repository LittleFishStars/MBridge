from textual.widgets import ListItem, Label


class Friend(ListItem):
    def __init__(self, name: str, friend_id: str, **kwargs) -> None:
        super().__init__(Label(name, **kwargs))
        self.friend_name = name
        self.friend_id = friend_id
