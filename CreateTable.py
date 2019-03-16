#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author:  Analyst1981@gmail.com
# @date:    2019-02-27
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='toor', db='spiders', charset='utf8')

cursor = db.cursor()
try:
    cursor.execute('DROP TABLE IF EXISTS ProxyComment')
except:
    print('表ProxyComment不存在！，直接创建')

else:
    print('原表已删除！')
finally:
    pass

sql = """CREATE TABLE ProxyComment(
          IP VARCHAR(1024) NOT NULL PRIMARY KEY COMMENT 'IP地址',
          PORT INT NOT NULL COMMENT '端口',
          TYPE VARCHAR(1024) NULL NULL COMMENT '地址协议',
          SCORE INT DEFAULT NULL COMMENT '使用值',
          createtime DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '添加时间'
          )ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='代理表';"""
try:
    cursor.execute(sql)
    db.commit()
    print('已提交')
except:
    print('发生错误,数据回滚')
    db.rollback()

db.close()
print('数据库已关闭')
# id INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '自增 id',
