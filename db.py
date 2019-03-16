#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

from setting import MYSQL_HOST, MYSQL_PORT, MYSQL_PASSWORD, MYSQL_USER,MYSQL_DB,MYSQL_TABLE
from setting import MAX_SCORE, MIN_SCORE, INITIAL_SCORE
from random import choice
import re
import pymysql
class MysqlClient(object):
    def __init__(self ):
        """
        初始化数据库MYSQL_HOST,MYSQL_USER,MYSQL_PORT, MYSQL_PASSWORD,MYSQL_DB
        """
        self.conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER,port=MYSQL_PORT, password=MYSQL_PASSWORD,database=MYSQL_DB,charset='utf8mb4')
        self.cursor = self.conn.cursor()
     
   
    def add(self,proxy,score=INITIAL_SCORE):
        
        """
        添加代理，设置分数为最高
        :param proxy: 代理PROXY_IP,PROXY_PORT,PROXY_TYPE
        :param score: 分数
        :return: 添加结果
        """
        
        sql='INSERT INTO ProxyComment(IP,PORT,TYPE,SCORE) VALUES (%s,%s,%s,%s)'
            
        try:
            #print(type(proxy))
            #print(proxy)
            self.cursor.execute(sql,(proxy[0],proxy[1],proxy[2],score))
            self.conn.commit()
        except Exception as e :
            print(e.args)
            print('Failed')
            self.conn.rollback() 

    def random(self):
        """
        随机获取有效代理，首先尝试获取最高分数代理，如果不存在，按照排名获取，否则异常
        :return: 随机代理
        """
        sql='SELECT * FROM  ProxyComment WHERE SCORE ="100"'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            return result
        else:
            sql='SELECT * FROM ProxyComment ORDER BY SCORE DESC'
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if result:
                return result
            else:
                self.conn.rollback() 
                #raise PoolEmptyError
    def decrease(self,proxy):
        """
        代理值减一分，小于最小值则删除
        :param proxy: 代理proxy 
        :return: 修改后的代理分数
        """
        sql='SELECT SCORE FROM  ProxyComment WHERE IP=%s'
       
        self.cursor.execute(sql,(proxy[0]))
        score = self.cursor.fetchone()
        if (score[0] == None and score[0]==0):
            print('代理', proxy, '当前分数', score, '移除')
            sql='DELETE FROM ProxyComment WHERE IP=%s'
            self.cursor.execute(sql,(proxy[0]))
            self.conn.commit()
            return 
        elif score[0] > MIN_SCORE:
            print('代理', proxy, '当前分数', score, '减1')
            sql='update ProxyComment set SCORE=SCORE-1 where IP=%s'
            self.cursor.execute(sql,(proxy[0]))
            self.conn.commit()
            return 
        
            
        
    def exists(self,proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        sql='SELECT * FROM ProxyComment where IP=%s'
        self.cursor.execute(sql,(proxy[0]))
        result = self.cursor.fetchall()
        if result:
           return  True
        else:
           return  False
           
    
    def max_(self,proxy):
        """
        将代理设置为MAX_SCORE
        :param proxy: 代理
        :return: 设置结果
        """
        print('代理', proxy, '可用，设置为', MAX_SCORE)
        sql='update ProxyComment set SCORE= %s where IP=%s'
        #print(sql)
        self.cursor.execute(sql,(MAX_SCORE,proxy[0]))
        self.conn.commit()
        return 
    
    def count(self):
        """
        获取数量
        :return: 数量
        """
        sql='SELECT * FROM  ProxyComment'
        self.cursor.execute(sql)
        return  len(self.cursor.fetchall())
    
    def all(self):
        """
        获取全部代理
        :return: 全部代理列表
        """
        sql='SELECT * FROM  ProxyComment'
        
        self.cursor.execute(sql)
        return self.cursor.fetchall()
       
    
    def batch(self,start,stop):
        """
        批量获取
        select * from employee limit 3, 7; // 返回4-11行
        :param start: 开始索引
        :param stop: 结束索引
        :return: 代理列表
        """
        sql='SELECT * FROM  ProxyComment LIMIT %s,%s'
        #print(sql)
        self.cursor.execute(sql,(start,stop))
        #print(self.cursor.fetchall())
        #return len(self.cursor.fetchall())
        return self.cursor.fetchall()



    """
    def __del__(self):
        
        self.conn.close()
        self.cursor.close()
    """
"""
创建mysql对象：

mysql_test = Mysql('192.168.232.128','3306','root','123456','iceny')
      创建表t1：

mysql_test.exec('create table t1 (id int auto_increment primary key,timestamp TIMESTAMP)')
      image.png

      往t1插入一条数据：
       
        if not re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
            print('代理不符合规范', proxy, '丢弃')
            return
    

mysql_test.exec('insert into t1 (id,timestamp) value (NULL,CURRENT_TIMESTAMP)')
"""
   
    
    
    
    
if __name__ == '__main__':
    conn = MysqlClient()
    result = conn.batch(680,688)
    print(result)