import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库URI链接信息格式化函数
def get_db_url(dbinfo):

    # 未获取到数据库时,设置默认值
    ENGINE = dbinfo.get("ENGINE") or "mysql"
    DRIVER = dbinfo.get("DRIVER") or "pymysql"
    USER = dbinfo.get("USER") or "root"
    PASSWORD = dbinfo.get("PASSWORD") or "root"
    HOST = dbinfo.get("HOST") or "localhost"
    PORT = dbinfo.get("PORT") or "3306"
    NAME = dbinfo.get("NAME") or "flaskexample"

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)

class Config(object):
    '''配置参数信息 - 使用类的方式'''

    DEBUG = False  # 是否开启Debug模式,关闭
    TESTING = False  # 是否开启测试模式,关闭
    SECRET_KEY = 'a1s2d3f4g5h6j7k8l9'

    # 数据库
    # SQLAlchemy配置参数: 设置链接数据库的URL
    # SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/ihome"
    # SQLAlchemy配置参数: 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy配置参数: 数据库查询时显示原始SQL语句(程序调试的时候可以使用)
    # SQLALCHEMY_ECHO = True

    # redis数据库信息 - 缓存
    # REDIS_HOST = '127.0.0.1'
    # REDIS_PORT = 6379

    # flask-session配置 - session
    # SESSION_TYPE = 'redis'  # session的存储方式
    # SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # redis的链接实例对象
    # SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏加密处理
    # PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期,单位秒


class DevelopConfig(Config):
    '''开发环境的配置信息'''
    DEBUG = True  # 开启Debug模式
    DATABASE = {
        "ENGINE": "mysql",  # 数据库
        "DRIVER": "pymysql",  # 数据库驱动
        "USER": "root",  # 用户名
        "PASSWORD": "root",  # 密码
        "HOST": "localhost",  # 主机IP
        "PORT": "3306",  # 端口号
        "NAME": "flaskexample",  # 数据库名称
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


class TestingConfig(Config):
    '''测试环境的配置信息'''
    TESTING = True  # 开启测试模式
    DATABASE = {
        "ENGINE": "mysql",  # 数据库
        "DRIVER": "pymysql",  # 数据库驱动
        "USER": "root",  # 用户名
        "PASSWORD": "root",  # 密码
        "HOST": "localhost",  # 主机IP
        "PORT": "3306",  # 端口号
        "NAME": "flaskexample",  # 数据库名称
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


class StagingConfig(Config):
    '''演示环境的配置信息'''
    DATABASE = {
        "ENGINE": "mysql",  # 数据库
        "DRIVER": "pymysql",  # 数据库驱动
        "USER": "root",  # 用户名
        "PASSWORD": "root",  # 密码
        "HOST": "localhost",  # 主机IP
        "PORT": "3306",  # 端口号
        "NAME": "flaskexample",  # 数据库名称
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


class ProductConfig(Config):
    '''生产环境的配置信息'''
    DATABASE = {
        "ENGINE": "mysql",  # 数据库
        "DRIVER": "pymysql",  # 数据库驱动
        "USER": "root",  # 用户名
        "PASSWORD": "root",  # 密码
        "HOST": "localhost",  # 主机IP
        "PORT": "3306",  # 端口号
        "NAME": "flaskexample",  # 数据库名称
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)


# 配置模式与类之间的映射关系
envs= {
    'develop': DevelopConfig,  # 开发环境
    'testing': TestingConfig,  # 测试环境
    'staging': StagingConfig,  # 演示环境
    'product': ProductConfig,  # 生产环境

    'default': DevelopConfig,  # 默认环境
}





