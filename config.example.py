"""
Flask 应用程序的配置文件。
* 可通过 `app.config[]` 在程序中引用这些配置。
"""

# 开发环境选项
DEBUG = True
LISTEN_HOST_DEV = r'0.0.0.0'
LISTEN_PORT_DEV = 8316

# 生产环境选项
LISTEN_HOST_PRODUCTION = r'0.0.0.0'
LISTEN_PORT_PRODUCTION = 8080

# Session
SECRET_KEY = r'xsa2D3^242H&*h(125a#Y(4865@##?RT'

# SQLAlchemy 数据库配置
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = r"sqlite:///../data/database.db"

# Scheduler
SCHEDULER_API_ENABLED = True

# 提供邮件服务
MAIL_ACCOUNT = ""
MAIL_PASSWORD = ""
MAIL_HOST = ""
MAIL_SSL = False

# 管理员邮箱
ADMIN_MAIL = ""
