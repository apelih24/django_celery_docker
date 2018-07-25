from __future__ import absolute_import, unicode_literals
import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from celery import shared_task, current_task, task
import json
from polls.models import IcoList


@shared_task
def create_random_user_accounts(total_user):
    for i in range(total_user):
        username = 'user_%s' % get_random_string(5, string.ascii_letters)
        email = '%s@example.com' % username
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
        print('{} created'.format(username))
        current_task.update_state(state='PROGRESS',
                                  meta={'current': i, 'total': total_user,
                                        'percent': int((float(i) / total_user) * 100)})
    return {'current': total_user, 'total': total_user, 'percent': 100}


@shared_task
def get_for_django():
    with open('/home/alex/PycharmProjects/scrapy_ico-list/ico_list') as f:
        data = json.load(f)
    for currency in data:
        row = IcoList.objects.get(name=currency['name'])
        if row:
            row.ico_scale = currency['ico_scale']
            row.total = currency['total']
            row.save()
        else:
            IcoList.objects.create(name=data['name'], ico_scale=data['ico_scale'], total=data['total'])
