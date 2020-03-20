from app import app
from .notifier import Notifier

sender = Notifier(app.config["MAIL_HOST"],
                  app.config["MAIL_ACCOUNT"],
                  app.config["MAIL_PASSWORD"],
                  app.config["ADMIN_MAIL"])
