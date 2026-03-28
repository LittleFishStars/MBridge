from loguru import logger
from textual.binding import Binding
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import ListItem, Label, ListView

from tool.i18n import get_i18n

_ = get_i18n()


class FriendItem(ListItem):
    selected = reactive(False)

    def __init__(self, name: str, friend_id: str, **kwargs) -> None:
        super().__init__(Label(name), **kwargs)
        self.friend_name = name
        self.friend_id = friend_id

    def watch_selected(self, value: bool) -> None:
        self.set_class(value, "-selected")


class FriendList(ListView):
    BINDINGS = [
        Binding("enter", "select_cursor", _("Select")),
        Binding("up", "cursor_up", _("Cursor up")),
        Binding("down", "cursor_down", _("Cursor down")),
    ]

    selected_child: FriendItem = None

    class ChatChanged(Message):
        """自定义事件：更换聊天对象"""

        def __init__(self, name: str, id: str) -> None:
            super().__init__()
            self.name = name
            self.id = id

    def on_mount(self) -> None:
        self.border_title = _("FriendList")
        self.blur()

    def on_list_view_selected(self, event) -> None:
        friend: FriendItem = event.item
        if friend != self.selected_child:
            logger.debug(f"ChooseFriend {friend.friend_name}")
            if self.selected_child is not None:
                self.selected_child.selected = False
            self.selected_child = friend
            friend.selected = True
            self.post_message(self.ChatChanged(friend.friend_name, friend.friend_id))
