import json
import os

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from developXapp.forms import CashAmount
from developXapp.views import MainPage


# clear console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class AccessMainPage(TestCase):
    cls()

    def setUp(self):
        self.user_client = Client()

    def test_main_page_access(self):
        response = self.user_client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 200)

    # form to be valid for all numbers and null
    def test_main_page_form(self):
        form = CashAmount(data={"cashamount": ""})
        self.assertTrue(form.is_valid())
        form = CashAmount(data={"cashamount": "111"})
        self.assertTrue(form.is_valid())
        form = CashAmount(data={"cashamount": "111.22"})
        self.assertTrue(form.is_valid())
        form = CashAmount(data={"cashamount": "-111.22"})
        self.assertTrue(form.is_valid())
        form = CashAmount(data={"cashamount": "0"})
        self.assertTrue(form.is_valid())

    def test_post(self):
        response = self.user_client.post("/", data={"cashamount": "200"})
        self.assertEqual(response.status_code, 200)

    def test_notes_delivery_function(self):
        self.assertEqual(MainPage.notes_delivery(200), [100, 100])
        self.assertEqual(MainPage.notes_delivery(20), [20])
        self.assertEqual(MainPage.notes_delivery(580), [100, 100, 100, 100, 100, 50, 20, 10])
        self.assertEqual(MainPage.notes_delivery(10), [10])
        self.assertEqual(MainPage.notes_delivery(160), [100, 50, 10])
        self.assertEqual(MainPage.notes_delivery(160), [100, 50, 10])
        self.assertEqual(str(MainPage.notes_delivery(-20)), 'InvalidArgumentException')
        self.assertEqual(str(MainPage.notes_delivery(-20.33)), 'InvalidArgumentException')
        self.assertEqual(str(MainPage.notes_delivery(1.44)), 'NoteUnavailableException')
        self.assertEqual(str(MainPage.notes_delivery(133)), 'NoteUnavailableException')


class TestApi(TestCase):
    def setUp(self):
        self.user_client = Client()

    def test_api(self):
        response = self.user_client.get(reverse('notes_api'))
        self.assertEqual(response.status_code, 200)

        response = self.user_client.get("/api?amount=170")
        result = json.loads(response.content)
        self.assertEqual(result, {"notes": "[100, 50, 20]"})

        response = self.user_client.get("/api?amount=10")
        result = json.loads(response.content)
        self.assertEqual(result, {"notes": "[10]"})

        response = self.user_client.get("/api?amount=-10")
        result = json.loads(response.content)
        self.assertEqual(result, {"notes": "InvalidArgumentException"})

        response = self.user_client.get("/api?amount=12.22")
        result = json.loads(response.content)
        self.assertEqual(result, {"notes": "NoteUnavailableException"})


# run tests => python3 manage.py test
