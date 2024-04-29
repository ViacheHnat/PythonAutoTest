"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    # log_message = f"Login event - Username: {username}, Status: {status}"
    if type(username) is str and type(status) is str:
        log_message = f"Login event - Username: {username}, Status: {status}"
    elif type(username) is not str and type(status) is str:
        log_message = f"Login event - Username: {username} - Wrong type, must be str, Status: {status}"
    elif type(username) is str and type(status) is not str:
        log_message = f"Login event - Username: {username}, Status: {status} - Wrong type, must be str"
    else:
        log_message = f"Login event - Username: {username} - Wrong type, must be str, Status: {status} - Wrong type, must be str"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


class TestLogingUser(unittest.TestCase):

    def test_user_name_str(self):
        log_event("Viacheslav", "success")

    def test_user_status_expired(self):
        log_event("Viacheslav", "expired")

    def test_user_status_success(self):
        log_event("Viacheslav", "success")

    def test_user_status_else(self):
        log_event("Viacheslav", "unknown status")

    def test_user_name_bool(self):
        log_event(True, "success")

    def test_user_status_bool(self):
        log_event("Viacheslav", False)

    def test_user_name_int(self):
        log_event(1245, "success")

    def test_user_name_and_status_int_format(self):
        log_event(12345, 123)

    def test_user_status_int_format(self):
        log_event("Viacheslav", 56)

    def test_missing_arguments(self):
        log_event(None,None)
