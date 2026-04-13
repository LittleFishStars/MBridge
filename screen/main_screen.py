from textual.app import ComposeResult
from textual.widget import Widget

from screen.chat import Chat
from screen.friend import FriendItem, FriendList


class MainScreen(Widget):
    """主屏幕组件"""
    # 聊天窗口组件
    _chat_widget = Chat()

    def compose(self) -> ComposeResult:
        """组合主屏幕组件"""
        # 生成好友列表，包含三个示例好友
        yield FriendList(
            FriendItem("Amy", "1"),
            FriendItem("Bob", "2"),
            FriendItem("Charlie", "3"),
        )
        # 生成聊天窗口
        yield self._chat_widget

    def on_friend_list_chat_changed(self, event: FriendList.ChatChanged) -> None:
        """处理好友列表聊天变更事件
        
        Args:
            event: 聊天变更事件，包含好友名称和ID
        """
        # 移除当前聊天窗口
        self._chat_widget.remove()
        # 创建新的聊天窗口，设置好友名称和ID
        self._chat_widget = Chat(event.name, event.id)
        # 挂载新的聊天窗口
        self.mount(self._chat_widget)
