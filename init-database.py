"""
数据库初始化脚本。
用于快速部署到新环境中。
"""

from app import db, model

# 初始化数据库模型
model.initialize()

# 创建数据库的表结构。
# 若已存在同名表，可能会出现失败问题。
db.create_all()
