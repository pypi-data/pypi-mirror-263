# -*- coding: utf-8 -*-
"""
@Time : 2024/1/23 14:25
@Author : TJF

"""
from sweetest.log import logger
class DB:

    def __init__(self, arg):
        self.connect = ''
        self.cursor = ''
        self.db = ''

        try:
            # 如果参数中的'type'属性值为'mongodb'
            if arg['type'].lower() == 'mongodb':
                # 导入pymongo库
                import pymongo
                # 获取参数中的'host'属性值，如果存在则弹出，否则使用默认值'localhost:27017'
                host = arg.pop('host') if arg.get('host') else 'localhost:27017'
                # 如果host包含逗号，表示有多个主机，将其拆分成列表，否则保持为单个主机字符串
                host = host.split(',') if ',' in host else host
                # 获取参数中的'port'属性值，如果存在则弹出，否则使用默认值27017，并将其转换为整数类型
                port = int(arg.pop('port')) if arg.get('port') else 27017
                # 如果参数中有'user'属性值，则将其赋值给'username'属性，并弹出'user'
                if arg.get('user'):
                    arg['username'] = arg.pop('user')
                # 创建MongoDB连接，使用给定的主机、端口和其他参数
                self.connect = pymongo.MongoClient(host=host, port=port, **arg)
                # 检查MongoDB服务器信息以确保连接成功
                self.connect.server_info()
                # 使用连接对象和给定的数据库名称创建数据库对象，并赋值给self.db
                self.db = self.connect[arg['dbname']]
                # 返回，结束函数
                return

            # 如果参数中的'type'属性值为'mysql'
            if arg['type'].lower() == 'mysql':
                # 导入pymysql库
                import pymysql as mysql
                # 使用给定的主机、端口、用户名、密码、数据库和字符集等参数创建MySQL连接对象
                self.connect = mysql.connect(
                    host=arg['host'], port=int(arg['port']), user=arg['user'], password=arg['password'],
                    database=arg['dbname'], charset=arg.get('charset', 'utf8'))
                # 创建MySQL游标对象
                self.cursor = self.connect.cursor()
                # 执行MySQL查询语句，获取MySQL版本信息的SQL语句
                sql = 'select version()'

            # 如果参数中的'type'属性值为'oracle'
            elif arg['type'].lower() == 'oracle':
                # 导入os和cx_Oracle库
                import os
                import cx_Oracle as oracle
                # 解决Oracle查询出的数据中文输出问题，设置环境变量NLS_LANG
                os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
                # 使用给定的用户名、密码、主机、SID等参数创建Oracle连接对象
                self.connect = oracle.connect(
                    arg['user'] + '/' + arg['password'] + '@' + arg['host'] + '/' + arg['sid'])
                # 创建Oracle游标对象
                self.cursor = self.connect.cursor()
                # 执行Oracle查询版本信息的SQL语句
                sql = 'select * from v$version'

            # 如果参数中的'type'属性值为'sqlserver'
            elif arg['type'].lower() == 'sqlserver':
                # 导入pymssql库
                import pymssql as sqlserver
                # 使用给定的主机、端口、用户名、密码、数据库和字符集等参数创建SQL Server连接对象
                self.connect = sqlserver.connect(
                    host=arg['host'], port=arg['port'], user=arg['user'], password=arg['password'],
                    database=arg['dbname'], charset=arg.get('charset', 'utf8'))
                # 创建SQL Server游标对象
                self.cursor = self.connect.cursor()
                # 执行SQL Server查询版本信息的SQL语句
                sql = 'select @@version'

            # 执行查询语句并获取结果的第一行
            self.cursor.execute(sql)
            self.cursor.fetchone()

        # 异常处理
        except:
            # 记录日志，指明连接失败的数据库类型
            logger.exception('*** %s connect is failure ***' % arg['type'])
            # 抛出异常
            raise

    # 定义一个方法，用于执行并获取查询结果的第一行数据
    def fetchone(self, sql):
        try:
            # 执行SQL查询语句
            self.cursor.execute(sql)
            # 获取查询结果的第一行数据
            data = self.cursor.fetchone()
            # 提交事务
            self.connect.commit()
            # 返回获取到的数据
            return data
        except:
            # 记录日志，指明Fetchone方法执行失败
            logger.exception('*** Fetchone failure ***')
            # 抛出异常
            raise

    # 定义一个方法，用于执行并获取查询结果的所有数据
    def fetchall(self, sql):
        try:
            # 执行SQL查询语句
            self.cursor.execute(sql)
            # 获取查询结果的所有数据
            data = self.cursor.fetchall()
            # 提交事务
            self.connect.commit()
            # 返回获取到的数据
            return data
        except:
            # 记录日志，指明Fetchall方法执行失败
            logger.exception('*** Fetchall failure ***')
            # 抛出异常
            raise

    # 定义一个方法，用于执行SQL语句（例如，插入、更新、删除等），并提交事务
    def execute(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交事务
            self.connect.commit()
        except:
            # 记录日志，指明Execute方法执行失败
            logger.exception('*** Execute failure ***')
            # 抛出异常
            raise

    # 定义一个方法，用于执行MongoDB的查询操作
    def mongo(self, collection, sql):
        try:
            # 构造MongoDB查询命令
            cmd = 'self.db[\'' + collection + '\'].' + sql
            # 使用eval执行MongoDB查询命令
            result = eval(cmd)
            # 根据查询命令的类型返回相应结果
            if sql.startswith('find_one'):
                return result
            elif sql.startswith('find'):
                for d in result:
                    return d
            elif 'count' in sql:
                return {'count': result}
            else:
                return {}
        except:
            # 记录日志，指明Mongo方法执行失败
            logger.exception('*** Execute failure ***')
            # 抛出异常
            raise

    # 定义析构方法，在对象销毁时关闭数据库连接
    def __del__(self):
        self.connect.close()
