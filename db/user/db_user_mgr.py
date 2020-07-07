from db.base import DbBase
from config import configuration
from db.connection_pool import MysqlConn
from utils.log_helper import lg

from werkzeug.security import generate_password_hash,check_password_hash

class DbUserMgr(DbBase):

   def get_user_list(self,current_page,page_size,search_data=None):
      conn = MysqlConn()
      try:
          start_num=(current_page-1)*page_size
          condition = None
          sear_condition =search_data

      except: