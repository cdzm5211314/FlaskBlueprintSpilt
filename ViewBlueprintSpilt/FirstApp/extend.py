### 第三方库初始化
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

# ORM映射
def init_extend(app):

    # 数据库ORM映射初始化
    db.init_app(app=app)
    # 数据库迁移初始化
    migrate.init_app(app, db)




