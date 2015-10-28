from django.test import TestCase
from django_adelaidex.util.fields import NullableCharField
from django_adelaidex.util.tests.models import UniqueBooleanTestModel, UniqueBooleanTestModel2


class NullableCharFieldTest(TestCase):
    def setUp(self):
        super(NullableCharFieldTest, self).setUp()
        self.ncf = NullableCharField()

    def test_to_python(self):
        self.assertEqual(self.ncf.to_python(None), '')
        self.assertEqual(self.ncf.to_python(''), '')
        self.assertEqual(self.ncf.to_python(0), '')
        self.assertEqual(self.ncf.to_python(1), 1)
        self.assertEqual(self.ncf.to_python('abc'), 'abc')

    def test_get_prep_value(self):
        self.assertEqual(self.ncf.get_prep_value(None), None)
        self.assertEqual(self.ncf.get_prep_value(''), None)
        self.assertEqual(self.ncf.get_prep_value(0), None)
        self.assertEqual(self.ncf.get_prep_value(1), 1)
        self.assertEqual(self.ncf.get_prep_value('abc'), 'abc')


class UniqueBooleanFieldTest(TestCase):

    def setUp(self):
        super(UniqueBooleanFieldTest, self).setUp()

        # Remove any previously-created instances
        UniqueBooleanTestModel.objects.all().delete()
        UniqueBooleanTestModel2.objects.all().delete()

    def test_create(self):
        # First instance is True
        instance1 = UniqueBooleanTestModel()
        self.assertFalse(instance1.unique_bool)
        instance1.save()
        self.assertTrue(instance1.unique_bool)

        # Second instance is False
        instance2 = UniqueBooleanTestModel()
        self.assertFalse(instance2.unique_bool)
        instance2.save()
        self.assertFalse(instance2.unique_bool)

        # First instance remains True
        instance1 = UniqueBooleanTestModel.objects.get(id=instance1.id)
        self.assertTrue(instance1.unique_bool)

    def test_set_true(self):
        # First instance is True
        instance1 = UniqueBooleanTestModel()
        self.assertFalse(instance1.unique_bool)
        instance1.save()
        self.assertTrue(instance1.unique_bool)

        # Second instance is set to True
        instance2 = UniqueBooleanTestModel()
        instance2.unique_bool = True
        self.assertTrue(instance2.unique_bool)
        instance2.save()
        self.assertTrue(instance2.unique_bool)

        # First instance becomes False
        instance1 = UniqueBooleanTestModel.objects.get(id=instance1.id)
        self.assertFalse(instance1.unique_bool)

    def test_set_false(self):
        # First instance is True
        instance1 = UniqueBooleanTestModel()
        self.assertFalse(instance1.unique_bool)
        instance1.save()
        self.assertTrue(instance1.unique_bool)

        # Second instance is set to False
        instance2 = UniqueBooleanTestModel()
        self.assertFalse(instance2.unique_bool)
        instance2.save()
        self.assertFalse(instance2.unique_bool)

        # First instance remains True
        instance1 = UniqueBooleanTestModel.objects.get(id=instance1.id)
        self.assertTrue(instance1.unique_bool)

        # First instance set to False
        instance1.unique_bool = False
        instance1.save()

        # First instance set to False
        instance1 = UniqueBooleanTestModel.objects.get(id=instance1.id)
        self.assertFalse(instance1.unique_bool)

        # Second instance becomes True
        instance2 = UniqueBooleanTestModel.objects.get(id=instance2.id)
        self.assertTrue(instance2.unique_bool)

    def test_delete_bool(self):
        # First instance is True
        instance1 = UniqueBooleanTestModel()
        self.assertFalse(instance1.unique_bool)
        instance1.save()
        self.assertTrue(instance1.unique_bool)

        # Second instance is set to True
        instance2 = UniqueBooleanTestModel()
        instance2.unique_bool = True
        self.assertTrue(instance2.unique_bool)
        instance2.save()
        self.assertTrue(instance2.unique_bool)

        # First instance becomes False
        instance1 = UniqueBooleanTestModel.objects.get(id=instance1.id)
        self.assertFalse(instance1.unique_bool)

        # Delete sole True instance
        instance2.delete()

        # First instance becomes True
        instance1 = UniqueBooleanTestModel.objects.get(id=instance1.id)
        self.assertTrue(instance1.unique_bool)

    def test_delete_multiple_bool(self):
        # First instance is True
        instance1 = UniqueBooleanTestModel2()
        self.assertFalse(instance1.unique_bool1)
        self.assertFalse(instance1.unique_bool2)
        instance1.save()
        self.assertTrue(instance1.unique_bool1)
        self.assertTrue(instance1.unique_bool2)

        # Second instance is set to True
        instance2 = UniqueBooleanTestModel2()
        instance2.unique_bool2 = True
        self.assertFalse(instance2.unique_bool1)
        self.assertTrue(instance2.unique_bool2)
        instance2.save()
        self.assertFalse(instance2.unique_bool1)
        self.assertTrue(instance2.unique_bool2)

        # First instance becomes False
        instance1 = UniqueBooleanTestModel2.objects.get(id=instance1.id)
        self.assertFalse(instance1.unique_bool2)
        self.assertTrue(instance1.unique_bool1)

        # Delete sole True instance
        instance2.delete()

        # First instance becomes True
        instance1 = UniqueBooleanTestModel2.objects.get(id=instance1.id)
        self.assertTrue(instance1.unique_bool1)
        self.assertTrue(instance1.unique_bool2)
