from django.test import TestCase
from django.urls import resolve
from cv.views import cv_list
# Create your tests here.
class CVPageTest(TestCase):
    def test_cv_url_resolves_to_cv_list_view(self):
        found = resolve('cv/')
        self.assertEquals(found.func, cv_list)
