from django.test import TestCase

# Create your tests here.
from .models import *


class YourTest(TestCase):
    
    def test_something(self):
        post = Db()
        self.assertEqual(post.get_title(), "MyName")

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1+1,2)



    def test_something_that_will_pass(self):
        self.assertTrue(True)

        
    # @classmethod
    # def test_setUpTestData(cls):
    #     Db.objects.create(title='Big', content='Bob')

   

    # def test_first_name_label(self):
    #     a=Db.objects.get(id=1)
    #     field_label = a._meta.get_field('title').verbose_name
    #     self.assertEquals(field_label,'title')