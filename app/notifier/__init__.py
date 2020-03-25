from app import app
from .notifier import Notifier


def get_notifier() -> Notifier:
    return Notifier(app.config["MAIL_HOST"],
                    app.config["MAIL_PORT"],
                    app.config["MAIL_ACCOUNT"],
                    app.config["MAIL_PASSWORD"],
                    app.config["MAIL_SSL"])


def alert(subject: str, content: str) -> None:
    alerter = get_notifier()
    alerter.send(app.config["ADMIN_MAIL"], subject, content)
    alerter.disconnect()
