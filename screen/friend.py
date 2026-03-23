from textual.reactive import reactive
from textual.widgets import ListItem, Label


class Friend(ListItem):
    selected = reactive(False)

    def __init__(self, name: str, friend_id: str, **kwargs) -> None:
        super().__init__(Label(name, **kwargs))
        self.friend_name = name
        self.friend_id = friend_id

    def watch_selected(self, value: bool) -> None:
        self.set_class(value, "-selected")
