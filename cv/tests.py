from django.test import TestCase
from django.urls import resolve
from cv.views import cv_list
from django.template.loader import render_to_string
from .forms import CVForm
from django.contrib.auth.models import User
# Create your tests here.
class CVPageTest(TestCase):
    def test_cv_list_template_is_used(self):
        response = self.client.get('http://0.0.0.0:8000/cv/')
        self.assertTemplateUsed(response, 'cv/cv_list.html')

    def test_cv_url_returns_correct_html(self):
        response = self.client.get('http://0.0.0.0:8000/cv/')
        html = response.content.decode('utf8')
        expected_html = render_to_string('cv/cv_list.html')
        self.assertEqual(html, expected_html)
