from textual.app import ComposeResult
from textual.containers import Right
from textual.widget import Widget
from textual.widgets import ListItem, Label, ListView


class ChatMessage(ListItem):
    """聊天消息组件"""
    # 默认CSS样式
    DEFAULT_CSS = """
    #content {
        color: $text-accent;
        background: $accent-muted;
    }
    #time {
        color: $text-secondary;
        background: $background;
    }
    """

    def __init__(self, message, time: str, is_me: bool = False, *children: Widget):
        super().__init__(*children)
        self.message = message
        self.time = time
        self.is_me = is_me

    def compose(self) -> ComposeResult:
        if self.is_me:
            yield Right(Label(self.message, id="content"))
            yield Right(Label(self.time, id="time"))
        else:
            yield Label(self.message, id="content")
            yield Label(self.time, id="time")


class ChatMessageList(ListView):
    """聊天消息列表组件"""

    def __init__(
            self,
            *children: ListItem,
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None
    ):
        super().__init__(
            *children,
            initial_index=None,
            name=name,
            id=id,
            classes=classes,
            disabled=True
        )
