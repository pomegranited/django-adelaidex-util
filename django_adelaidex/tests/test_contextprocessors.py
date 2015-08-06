from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
from django.conf import settings


class AnalyticsContextTest(TestCase):

    def test_not_set(self):
        client = Client()
        response = client.get('/')
        self.assertFalse(response.context['ALLOW_ANALYTICS'])

    @override_settings(ALLOW_ANALYTICS=True)
    def test_allow_analytics(self):

        client = Client()
        response = client.get('/')
        self.assertTrue(response.context['ALLOW_ANALYTICS'])

    @override_settings(ALLOW_ANALYTICS=False)
    def test_disallow_analytics(self):

        client = Client()
        response = client.get('/')
        self.assertFalse(response.context['ALLOW_ANALYTICS'])
