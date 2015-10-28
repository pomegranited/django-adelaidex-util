from django_adelaidex.util.fields import UniqueBooleanField
from django.db import models
from django.db.models import signals


class UniqueBooleanTestModel(models.Model):
    unique_bool = UniqueBooleanField()

signals.post_delete.connect(UniqueBooleanField.post_delete, sender=UniqueBooleanTestModel)


class UniqueBooleanTestModel2(models.Model):
    unique_bool1 = UniqueBooleanField()
    unique_bool2 = UniqueBooleanField()

signals.post_delete.connect(UniqueBooleanField.post_delete, sender=UniqueBooleanTestModel2)
