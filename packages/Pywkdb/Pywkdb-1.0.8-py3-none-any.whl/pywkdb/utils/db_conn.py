#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import pandas as pd
import pymysql.connections

from .url_parse import UrlParse

logger = logging.getLogger('DbConn')


class DbConn(object):

    def __init__(self, url, with_tran=False, auto_commit=True):
        """
        初始化数据库
        :param url:  数据库连接
        :param with_tran: 是否自动打开数据库连接
        :param auto_commit:  是否自动提交事务默认自动提交
        """
        self._url = url
        self._with_tran = with_tran
        self._auto_commit = auto_commit
        self._conn = None
        if self._with_tran:
            logger.debug('默认打开数据')
            self._conn = self.connect()

    def __del__(self):
        """
        删除对象时，自动释放数据库连接
        :return:
        """
        logger.debug('del sqldb')
        if self._conn is not None:
            try:
                DbConn.close(self._conn)
            except Exception as e:
                logger.error("__del__:{}".format(e))

    def set_auto_commit(self, auto_commit):
        """
        设置是否自动提交事务
        :param auto_commit:
        """
        self._auto_commit = auto_commit

    def get_auto_commit(self):
        """
        获取事务状态
        :return:
        """
        return self._auto_commit

    def set_with_tran(self, with_tran):
        """
        自动打开数据库连接
        :param with_tran:
        :return:
        """
        self._with_tran = with_tran
        if self._with_tran:
            self._conn = self.connect()
        else:
            DbConn.close(self._conn)

    def _get_conn(self):
        if not self._with_tran:
            logger.debug('使用新的数据链接')
            return self.connect()
        else:
            logger.debug('使用默认数据链接')
            return self._conn

    def _close(self):
        DbConn.close(self._conn)

    def close_all(self, cur, conn):
        DbConn.close(cur)
        if not self._with_tran:
            DbConn.close(conn)

    def conn(self):
        return self._conn

    @staticmethod
    def commit(conn):
        try:
            logger.debug('提交回滚')
            conn.commit()
        except:
            pass

    @staticmethod
    def begin(conn):
        try:
            logger.debug('开始begin')
            conn.begin()
        except:
            pass

    @staticmethod
    def rollback(conn):
        try:
            logger.debug('事务回滚')
            conn.rollback()
        except:
            pass

    @staticmethod
    def close(conn):
        """
        关闭游标或数据库
        :param conn: 游标或数据库链接
        """
        if conn is not None:
            try:
                conn.close()
                del conn
            except Exception as e:
                logger.error("close:{}".format(e))

    @staticmethod
    def _execute(conn, sql: str, params=None):
        """
        内部方法，执行sql代码
        :param sql:     sql代码
        :param params:  传递参数
        :return:        游标值Cursor
        """
        cur = conn.cursor()
        logger.info(sql)
        logger.info(params)
        if params is None:
            cur.execute(sql)
        else:
            cur.execute(sql, params)
        return cur

    def connect(self, url_parse=None):
        """
        生成连接串
        :return:
        """
        raise RuntimeError('找不到对应的数据配置,目前支持mysql、mssql、sqlite 和 oracle')

    @staticmethod
    def _pymysql():
        try:
            import pymysql
            return pymysql
        except ImportError:
            raise RuntimeError('PyMySQL不存在，pip install PyMySQL')

    @staticmethod
    def _pymssql():
        try:
            import pymssql
            return pymssql
        except ImportError:
            raise RuntimeError('pymssql不存在，pip install pymssql')

    @staticmethod
    def _cxoracle():
        try:
            import cx_Oracle
            return cx_Oracle
        except ImportError:
            raise RuntimeError('cx_Oracle不存在，pip install cx_Oracle')

    @staticmethod
    def _sqlite3():
        try:
            import sqlite3
            return sqlite3
        except ImportError:
            raise RuntimeError('SqliteDb不存在')
