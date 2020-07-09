from flask_restful import Api

from api.user.interface_user import interfaceUser
from api.login.interface_login import interfaceLogin

api = Api()
api.add_resource(interfaceUser,'/li-boss/user')


#登录
api.add_resource(
    interfaceLogin,
    '/li-boss/<version>/login'
)