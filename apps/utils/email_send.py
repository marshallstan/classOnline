# __author__ = 'Marshall Stan'

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from classOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    value = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        value += chars[random.randint(0, length)]
    return value


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = 'ClassOnline 在线激活链接'
        email_body = '请点击下面的链接激活帐号: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = 'ClassOnline 密码重置链接'
        email_body = '请点击下面的链接重置密码: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == 'update_email':
        email_title = 'ClassOnline邮箱修改验证码'
        email_body = '你的邮箱验证码为: {0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
