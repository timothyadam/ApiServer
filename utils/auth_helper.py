import json
import sys

import datetime
import jwt
import time
from flask import abort
from werkzeug.security import check_password_hash

import api
from db.user.db_user_mgr import user_mgr
from utils.status_code import response_code


class Auth(object):
    """
       权限校验、token帮助类
       """
    def __encode_auth_token (self,user_key,login_time):
        """
               生成认证Token
               :param USER_KEY: int
               :param login_time: int(timestamp)
               :return: string
               """
        try:
            ##exp: 过期时间
            ##nbf: 表示当前时间在nbf里的时间之前，则Token不被接受
            ##iss: token签发者
            ##aud: 接收者
            ##iat: 发行时间
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'user_key': user_key,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                api.Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e



    def __decode_auth_token(self, auth_token):
        """
        验证Token
        :param auth_token:
        :return: integer|string
        """
        try:
            ###十分钟无访问token过期
            # payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
            # 取消过期时间验证
            payload = jwt.decode(auth_token, api.Config.SECRET_KEY, options={'verify_exp': False})
            if ('data' in payload and 'user_key' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token过期'
        except jwt.InvalidTokenError:
            return '无效Token'
        except TypeError:
            return '无效Token'
        except:
            print(sys.exc_info()[1])


