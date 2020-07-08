
from db.user.db_user_mgr import user_mgr

__all__ = {"UserSingleton"}

class UserSingleton:
    """"
    """
    def get_all_user(self):
        """
        获取所有用户
        :return: userlist
        """
        return user_mgr.get_all_user()