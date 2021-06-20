import pymysql
import time

import config


def write_new_user(chat_id, name, surname, username):
    connect = pymysql.connect(
        host=config.host,
        user=config.user,
        passwd=config.passwd,
        db=config.db,
        charset=config.charset
    )
    try:
        with connect.cursor() as cursor:
            sql_insert = "INSERT INTO `users` (`chat_id`, `name`, `surname`, `username`, `date`) VALUES (%s, %s, %s, %s, %s)"
            time_now = time.strftime('%d-%m-%Y %H:%M:%S')
            cursor.execute(sql_insert, (chat_id, name, surname, username, time_now))
            connect.commit()
    finally:
        connect.close()


def write_message(chat_id, username, message):
    connect = pymysql.connect(
        host=config.host,
        user=config.user,
        passwd=config.passwd,
        db=config.db,
        charset=config.charset
    )
    try:
        with connect.cursor() as cursor:
            sql_insert = "INSERT INTO `messages` (`chat_id`, `username`, `message`, `date`) VALUES (%s, %s, %s, %s)"
            time_now = time.strftime('%d-%m-%Y %H:%M:%S')
            cursor.execute(sql_insert, (chat_id, username, message, time_now))
            connect.commit()
    finally:
        connect.close()
