from db.base import DbBase
from config import configuration
from db.connection_pool import MysqlConn
from utils.log_helper import lg
from utils.status_code import response_code

from werkzeug.security import generate_password_hash,check_password_hash

class DbUserMgr(DbBase):

   def get_user_list(self,current_page,page_size,search_data=None):
      conn = MysqlConn()
      try:
          start_num=(current_page-1)*page_size
          condition = None
          sear_condition =search_data
      except:
          pass

   def get_all_user(self):
       """
       查询所有用户
       :return:
       """
       db_conn = MysqlConn()
       try:
           db_name = configuration.get_database_name()
           table_name = 'users'
           fields = 'id,account,user_name,identify,email,phone,position,head_image,description'
           sql = self.create_select_sql(db_name, table_name, fields)
           result = self.execute_fetch_all(db_conn, sql)
           data = response_code.SUCCESS
           data['data'] = result
           return data
       except Exception as e:
           lg.error(e)
           return response_code.GET_DATA_FAIL
       finally:
           db_conn.close()



user_mgr = DbUserMgr()
