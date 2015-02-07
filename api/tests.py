# coding=utf-8

from django.core.management import call_command
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class ApiTest(APITestCase):
    def setUp(self):
        """Setup test http client"""
        self.client = APIClient()
        self.city = {'city': 'Guangzhou'}
        # load fixtures
        call_command('loaddata', 'dumpdata.json', verbosity=0)

    def test_air_condition(self):
        """Test hourly pm2.5 api"""
        url = reverse('api:pm25-list', kwargs=self.city)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Guangzhou', response.content)

    def test_air_average(self):
        """Test pm2.5 average api"""
        url = reverse('api:pm25-avg-list', kwargs=self.city)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Guangzhou', response.content)
        self.assertIn('from_time', response.content)
        self.assertIn('to_time', response.content)
