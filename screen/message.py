from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import ListItem, Label


class Message(ListItem):
    def __init__(self, message, *children: Widget):
        super().__init__(*children)
        self.message = message

    def compose(self) -> ComposeResult:
        yield Label()
