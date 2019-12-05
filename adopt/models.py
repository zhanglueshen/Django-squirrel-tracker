
from django.db import models

from django.utils.translation import gettext as _


class Pet(models.Model):
    name=models.CharField(
            help_text=_('Name of Pet'),
            max_length=100,
    )

    species=models.CharField(
            help_text=_('Species of animal'),
            max_length=100,
    )
    birth_date=models.DateField(
            help_text=_('Birth Date'),
    )

    MALE='Male'
    FEMALE='Female'
    OTHER='other'

    SEX_CHOICES=(
            (MALE,'Male'),
            (FEMALE,'Female'),
            (OTHER,'other'),
    )

    sex=models.CharField(
            help_text=_('Sex of pet'),
            max_length=16,
            choices=SEX_CHOICES,
            default=OTHER,
    )

    def _str_(self):
        return self.name
