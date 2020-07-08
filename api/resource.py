from flask_restful import Api

from api.user.interface_user import interfaceUser


api = Api()
api.add_resource(interfaceUser,'/li-boss/user')