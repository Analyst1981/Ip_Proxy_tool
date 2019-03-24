#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  Analyst1981@gmail.com
# @date:    2019-3-16

# 数据库地址
MYSQL_HOST = '127.0.0.1'

# 端口
MYSQL_PORT = 3306
MYSQL_PASSWORD = 'toor'
MYSQL_USER='root'

MYSQL_DB='spiders'
MYSQL_TABLE='ProxyComment'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'http://www.baidu.com'

# API配置
API_HOST = '127.0.0.1'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 50