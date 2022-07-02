import settings
import json
import os

secret = {'Django_key': settings.SECRET_KEY}
secret['MySQL_pwd'] = input('请输入 MySQL 密码:\n')

f = open(os.path.dirname(os.path.abspath(__file__)) + '/secret.json', 'w')
json.dump(secret, f)
