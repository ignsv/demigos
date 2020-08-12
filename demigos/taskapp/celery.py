# -*- coding: utf-8 -*-

import os

from celery import Celery

from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery('demigos')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'recalculate-every-10-seconds': {
        'task': 'demigos.crypto.tasks.recalculate_pair_volume',
        'schedule': 10.0,
    },
}

app.conf.broker_url = 'redis://redis:6379/1'