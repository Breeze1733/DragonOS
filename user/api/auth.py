# 实现了用户注册API
from models.user import User

def register_user(username, password):
    return User(username, password)