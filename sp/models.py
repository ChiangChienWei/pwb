from django.db import models
from django.utils.translation import pgettext_lazy
from django.utils.translation import ugettext_lazy as _


class Intro(models.Model):

    name = models.CharField(_('姓名'), max_length=255, default=_('江健瑋'))
    name_en = models.CharField(_('姓名（英）'), max_length=255, default='willchiang')
    school = models.CharField(_('學校'), max_length=255)
    introduction = models.TextField(_('簡介'), blank=True)

    class Meta:
        verbose_name = pgettext_lazy('intro', '個人簡介')
        verbose_name_plural = pgettext_lazy('intro', '個人簡介')

    def __str__(self):
        return self.name
