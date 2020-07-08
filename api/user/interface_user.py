from flask import request
from flask_restful import Resource

from utils.log_helper import lg
from utils.status_code import response_code
from service.user_singleton import user_mgr
class interfaceUser(Resource):

   def get(self):
       try:
          return user_mgr.get_all_user()
       except Exception as e:
           lg.error(e)