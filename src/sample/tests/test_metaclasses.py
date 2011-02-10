import unittest
from django.db import models
from django.db.models.loading import get_model

class DynamicPythonClassTests(unittest.TestCase):

    def setUp(self):
        self.model_name = "SampleClass"
        self.model = type(self.model_name, (object,), {'__module__':__name__})

    def test_class_modification(self):
        self.model.something = "here"

    def test_class_modification_gone(self):
        self.assertFalse(getattr(self.model, 'something', None), "here")

    def test_normal_classes_are_not_cached(self):
        model_one = type(self.model_name, (object,), {'__module__':__name__})
        model_two = type(self.model_name, (object,), {'__module__':__name__})
        self.assertNotEqual(model_one, model_two)

class DynamicDjangoModelTests(unittest.TestCase):

    def setUp(self):
        self.model_name = "SampleModel"
        self.model = type(self.model_name, (models.Model,), {'__module__':__name__})

    def test_class_modification(self):
        self.model.something = "here"

    def test_class_modification_gone(self):
        self.assertFalse(getattr(self.model, 'something', None), "here")

    def test_django_caches_model_classes(self):
        model_one = type(self.model_name, (models.Model,), {'__module__':__name__})
        model_two = type(self.model_name, (models.Model,), {'__module__':__name__})

        self.assertEqual(model_one, model_two)

    def test_what_django_is_doing(self):
        """
        In Django's ModelBase class if get_model returns something, that is what will
        be used as the Model class, so calling type() (like in the setUp) will result
        in the same class object.
        """
        self.assertEqual(None, get_model(self.model._meta.app_label, self.model_name, False))
