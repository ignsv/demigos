from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import Avg


class Pair(models.Model):
    name = models.CharField(_('Pair name'), max_length=255, help_text=_('Maximum length is 255 symbols'))

    class Meta:
        verbose_name = _('Pair')
        verbose_name_plural = _('Pairs')

    def __str__(self):
        return self.name

    @property
    def average_volume(self):
        return self.records.aggregate(average=Avg('volume'))['average']

    @property
    def last_volume(self):
        return self.records.last().volume if self.records.last() else None


class PairRecord(models.Model):
    pair = models.ForeignKey(Pair, verbose_name=_('Pair'), on_delete=models.CASCADE, related_name='records')
    volume = models.FloatField(_('Crypto volume'))
    created = models.DateTimeField(_('TimeStamp'), auto_now_add=True)


    def __str__(self):
        return '{}_{}'.format(self.pair.name, self.volume)
