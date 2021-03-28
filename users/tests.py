# Django
from django.test import TestCase

# Python
from PIL import Image
import tempfile
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from users.models import User


class UserTestCase(TestCase):

    def setUp(self):
        user = User(
            email='amtzran_login_test@gmail.com',
            name='Alberto Martínez',
            phone='4491231230',
            gender='Masculino',
            username='testingLogin'
        )
        user.set_password('eCmcUX&K&jJB')
        user.save()
        self.user = user

    def test_signup_user(self):
        """Check if we can create an user"""

        image = Image.new('RGB', (100, 100))

        tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)

        client = APIClient()
        response = client.post(
            '/users/signup/', {
                'email': 'amtzran_test@gmail.com',
                'password': 'zzlGL^J*!0v2',
                'password_confirmation': 'zzlGL^J*!0v2',
                'name': 'Alberto Dev',
                'phone': '4491234567',
                'username': 'testingDev',
                'photo': tmp_file,
                'gender': 'Masculino'
            },
            format='multipart'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {"username": "testingDev", "name": "Alberto Dev", "phone": "4491234567",
                          "email": "amtzran_test@gmail.com", "gender": "Masculino"})

    def test_login_user(self):
        client = APIClient()
        response = client.post(
            '/users/login/', {
                'email': 'amtzran_login_test@gmail.com',
                'password': 'eCmcUX&K&jJB',
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        result = json.loads(response.content)
        self.assertIn('access_token', result)

    def test_update_user(self):
        test_user_update = {
            'name': 'Alberto Martínez',
            'email': 'amtzran_login_test@gmail.com',
            'gender': 'Femenino',
            'phone': '4491231200',
            'username': 'testingLogin'
        }

        client = APIClient()
        response = client.put(
            f'/users/{self.user.pk}/',
            test_user_update,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        if 'pk' in result:
            del result['pk']

        self.assertEqual(result, test_user_update)

    def test_delete_user(self):
        client = APIClient()
        response = client.delete(
            f'/users/{self.user.pk}/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        user_exists = User.objects.filter(pk=self.user.pk)
        self.assertFalse(user_exists)

    def test_get_user(self):

        client = APIClient()

        User.objects.create(
            email='amtzran_login_test3@gmail.com',
            name='Alberto Martínez3',
            phone='4491231239',
            gender='Masculino',
            username='testingLogin3'
        )

        User.objects.create(
            email='amtzran_login_test2@gmail.com',
            name='Alberto Martínez2',
            phone='4491231231',
            gender='Femenino',
            username='testingLogin2'
        )

        response = client.get('/users/')

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(result['count'], 3)

        for user in result['results']:
            self.assertIn('email', user)
            self.assertIn('name', user)
            self.assertIn('phone', user)
            self.assertIn('gender', user)
            break
