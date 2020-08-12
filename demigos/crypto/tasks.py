from demigos.taskapp.celery import app
from .handler import CryptoHandler
from .models import PairRecord, Pair


@app.task
def recalculate_pair_volume():
    handler = CryptoHandler()
    for pair in Pair.objects.all():
        PairRecord.objects.create(pair=pair, volume=handler.get_pair_current_value(*pair.name.split('-')))
        if pair.records.count() == 7:
            pair.records.first().delete()
