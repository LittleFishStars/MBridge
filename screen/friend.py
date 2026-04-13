from loguru import logger
from textual.binding import Binding
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import ListItem, Label, ListView

from tool.i18n import get_i18n

# 初始化国际化
_ = get_i18n()


class FriendItem(ListItem):
    """好友列表项组件"""
    # 响应式属性，标记是否被选中
    selected = reactive(False)

    def __init__(self, name: str, friend_id: str, **kwargs) -> None:
        """初始化好友列表项
        
        Args:
            name: 好友名称
            friend_id: 好友ID
            **kwargs: 其他参数
        """
        super().__init__(Label(name), **kwargs)
        self.friend_name = name
        self.friend_id = friend_id

    def watch_selected(self, value: bool) -> None:
        """监听selected属性变化，更新样式
        
        Args:
            value: 是否被选中
        """
        self.set_class(value, "-selected")


class FriendList(ListView):
    """好友列表组件"""
    # 快捷键绑定
    BINDINGS = [
        Binding("enter", "select_cursor", _("Select")),
        Binding("up", "cursor_up", _("Cursor up")),
        Binding("down", "cursor_down", _("Cursor down")),
    ]

    # 当前选中的好友项
    selected_child: FriendItem = None

    class ChatChanged(Message):
        """自定义事件：更换聊天对象"""

        def __init__(self, name: str, id: str) -> None:
            """初始化聊天变更事件
            
            Args:
                name: 好友名称
                id: 好友ID
            """
            super().__init__()
            self.name = name
            self.id = id

    def on_mount(self) -> None:
        """组件挂载时执行的方法"""
        # 设置边框标题
        self.border_title = _("FriendList")
        # 失去焦点
        self.blur()

    def on_list_view_selected(self, event) -> None:
        """处理列表项选择事件
        
        Args:
            event: 选择事件
        """
        friend: FriendItem = event.item
        # 如果选择的不是当前选中的好友
        if friend != self.selected_child:
            logger.debug(f"ChooseFriend {friend.friend_name}")
            # 取消之前选中的好友的选中状态
            if self.selected_child is not None:
                self.selected_child.selected = False
            # 更新当前选中的好友
            self.selected_child = friend
            friend.selected = True
            # 发送聊天变更事件
            self.post_message(self.ChatChanged(friend.friend_name, friend.friend_id))
