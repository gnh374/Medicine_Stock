# Create your tests here.
from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def setUp(self):
        Item.objects.create(name = "Bodrex", amount =5, description="Recommended for the treatment of most painful and febrile conditions, for example, headache including migraine, backache, toothache, colds and influenza, sore throat, rheumatic pain and dysmenorrhoea.")
        Item.objects.create(name = "Neozep Forte", amount =10, description="a medicine to relieve flu symptoms such as fever, headache, nasal congestion and sneezing.")

    def test_items_can_created(self):
        bodrex = Item.objects.get(name= "Bodrex")
        neozep_forte = Item.objects.get(name = "Neozep Forte")
        self.assertEqual(bodrex.amount, 5)
        self.assertEqual(neozep_forte.name, "Neozep Forte")