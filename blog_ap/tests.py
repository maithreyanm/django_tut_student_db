from django.test import TestCase

# Create your tests here.


import unittest
from datetime import datetime


class UserTests(unittest.TestCase):

    def test_user(self):
        request = {'POST':{'name':'maithreyan', 'age':25, 'email_1':'maithreyan@gmail.cpm',
                           'email_2':'reyan@gmail.com'}}
        from blog_ap.services import DataSync
        response = DataSync.save_data(request)