from textual.app import ComposeResult
from textual.widget import Widget

from screen.chat_input import ChatInput
from screen.chat_message import ChatMessage, ChatMessageList
from tool.i18n import get_i18n

# 初始化国际化
_ = get_i18n()


class Chat(Widget):
    """聊天窗口组件"""

    def __init__(
            self,
            friend_name: str | None = None,
            friend_id: str | None = None
    ) -> None:
        """初始化聊天窗口
        
        Args:
            friend_name: 好友名称
            friend_id: 好友ID
        """
        super().__init__()
        self.friend_name = friend_name
        self.friend_id = friend_id

    def compose(self) -> ComposeResult:
        """组合聊天窗口组件"""
        if self.friend_name is not None:
            # 生成消息列表，包含两条示例消息
            yield ChatMessageList(
                ChatMessage("Hello MBridge", "00:00:00"),
                ChatMessage("Hello MBridge 1", "00:00:10", is_me=True)
            )
            # 生成输入框
            yield ChatInput("input")

    def on_mount(self) -> None:
        """组件挂载时执行的方法"""
        if self.friend_name is not None:
            # 设置边框标题为好友名称
            self.border_title = self.friend_name
