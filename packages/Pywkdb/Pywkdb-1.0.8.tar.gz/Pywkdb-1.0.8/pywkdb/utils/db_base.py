#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import pandas as pd
from pywkdb.utils.db_conn import DbConn

logger = logging.getLogger('DbBase')


class DbBase(DbConn):

    def insert(self, sql: str, params=None):
        """
        插入一条记录
        :param sql:     sql代码
        :param params:  传递参数
        :return:        主键ID
        """
        cur = None
        conn = None
        insert_id = None
        try:
            conn = self._get_conn()
            cur = self._execute(conn, sql, params)
            try:
                insert_id = conn.insert_id()
            except:
                try:
                    insert_id = cur.lastrowid
                except:
                    logging.error('无法获取id')
            if self.get_auto_commit():
                DbBase.commit(conn)
            return insert_id
        except Exception as e:
            DbBase.rollback(conn)
            logger.error(e)
            raise e
        finally:
            self.close_all(cur, conn)

    def update(self, sql: str, params=None):
        """
        更新数据库
        :param sql:     sql代码
        :param params:  传递参数
        :return:        操作影响记录数
        """
        cur = None
        conn = None
        try:
            conn = self._get_conn()
            cur = self._execute(conn, sql, params)
            if self._auto_commit:
                DbBase.commit(conn)
            return cur.rowcount
        except Exception as e:
            DbBase.rollback(conn)
            logger.error("update_error:{}".format(e))
            raise e
        finally:
            self.close_all(cur, conn)

    def fetchmany(self, fetch_number, sql: str, params=None):
        """
        获取指定数据量，根据游标向下获取
        :param fetch_number:    数据条数
        :param sql:             sql代码
        :param params:          传递参数
        :return:                记录集
        """
        cur = None
        conn = None
        try:
            conn = self._get_conn()
            cur = self._execute(conn, sql, params)
            return cur.fetchmany(fetch_number)
        finally:
            self.close_all(cur, conn)

    def select(self, sql: str, params=None) -> (tuple, list):
        """
        用来查询表数据
        :return: 返回数据和表头
        """
        cur = None
        conn = None
        try:
            conn = self._get_conn()
            cur = self._execute(conn, sql, params)
            col = cur.description
            results = cur.fetchall()
            # 执行结果转化为dataframe
            headers = []
            for i in range(len(col)):
                headers.append(col[i][0])
            return results, headers
        finally:
            self.close_all(cur, conn)

    def select_frame_data(self, sql: str, params=None) -> pd.DataFrame:
        """
        查询结果返回DataFrame格式。
        example
        df = self.select_frame_data()
        for index, row in df.iterrows():
            print(index,row)
        :return: 返回DataRame格式数据
        """
        result, headers = self.select(sql, params)
        return pd.DataFrame(list(result), columns=headers)

    def select_data(self, sql: str, params=None) -> list:
        """
        查询结果返回List
        :param sql:
        :param params:
        :return:
        """
        results, headers = self.select(sql, params)
        items = []
        for result in results:
            item = {}
            i = 0
            for header in headers:
                item[header] = result[i]
                i += 1
            items.append(item)
        return items
