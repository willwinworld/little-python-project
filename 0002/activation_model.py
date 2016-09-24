#! python3
# -*- coding: utf-8 -*-

from peewee import *

mysql_db = MySQLDatabase('mydb',
                         user='root',
                         password='',
                         host='127.0.0.1',
                         charset='utf8mb4')
mysql_db.connect()


class BaseModel(Model):
    class Meta:
        database = mysql_db


class Activation(BaseModel):
    serial_number = IntegerField(null=False, primary_key=True, verbose_name='激活码序列号')
    activation_code = CharField(null=False, max_length=20, verbose_name='激活码内容')


if __name__ == '__main__':
    Activation.create_table()
