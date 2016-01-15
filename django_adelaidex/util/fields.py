from django.db import models
from django.db.models import BooleanField


# http://bitofpixels.com/blog/unique-on-charfield-when-blanktrue/
class NullableCharField(models.CharField):
    description = "CharField that stores NULL but returns ''"

    def to_python(self, value):
        return value or ''
    def get_prep_value(self, value):
        return value or None

'''
Description:

    Ensures that only one instance has a True value for this field.

Usage:
    class ExampleModel(models.Model):
        unique_bool = UniqueBooleanField()

    # Handle deletion of the sole True instance by setting objects.first() to True.
    signals.post_delete.connect(UniqueBooleanField.post_delete, sender=ExampleModel)
'''
class UniqueBooleanField(BooleanField):
    def __init__(self, *args, **kwargs):
        if not 'default' in kwargs:
            kwargs['default'] = False
        super(UniqueBooleanField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        objects = model_instance.__class__.objects.exclude(id=model_instance.id)

        # If True then set all others as False
        if getattr(model_instance, self.attname):
            objects.update(**{self.attname: False})

        # If no other objects have been saved, then set as True
        elif not objects.count():
            setattr(model_instance, self.attname, True)

        # If no other objects are True, then set the first one to True
        elif not objects.filter(**{self.attname: True}):
            first = objects.first()
            setattr(first, self.attname, True)
            first.save()

        return getattr(model_instance, self.attname)


    @staticmethod
    def post_delete(sender, instance=None, **kwargs):
        if instance:
            for field in instance.__class__._meta.local_fields:
                if type(field) is UniqueBooleanField:
                    setattr(instance, field.attname, False)
                    field.pre_save(instance, False)
