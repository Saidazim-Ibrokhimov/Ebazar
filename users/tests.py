from django.test import TestCase
from django.urls import reverse
from .models import CustomeUser

# Create your tests here.

class SignUpTestCase(TestCase):
    def test_sign_up_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name':'Saidazim',
                'last_name':'Ibroximov',
                'username':'saidazim',
                'email':'boy@gmail.com',
                'password1':'somepass',
                'password2':'somepass',
            }
            )
        
        user = CustomeUser.objects.get(username='saidazim')

        self.assertEqual(user.username, 'saidazim')
        self.assertEqual(user.email, 'boy@gmail.com')
        self.assertEqual(user.first_name, 'Saidazim')
        self.assertEqual(user.last_name, 'Ibroximov')
        self.assertTrue(user.check_password('somepass'))
        self.assertTemplateUsed('signup.html')
        self.assertEqual(response.url, reverse('login'))
        
        response = self.client.get(reverse('users:profile', kwargs={'username':user.username}))
        self.assertEqual(response.status_code, 200)

    def test_update_profile(self):
        user = CustomeUser.objects.create(username='saidazim', email='email@gmail.com', first_name='Saidazim')
        user.set_password('somepass')
        user.save()

        self.client.login(username='saidazim', password='somepass')

        response = self.client.post(
            reverse('users:update-profile'),
            data = {
                "first_name":"SaidazimBoy",
                "last_name":"Ibroximov",
                'email':'boy@gmail.com',
                'tg_username':'bu',
                'phone_number':'+998933459690'
            }
        )
        print(response.status_code)
        print(response.url)
        user.refresh_from_db()

        self.assertEqual(user.username, 'saidazim')
        # self.assertEqual(user.first_name, 'SaidazimBoy')
        self.assertEqual(user.email, 'boy@gmail.com')
        self.assertEqual(user.last_name, 'Ibroximov')
        self.assertEqual(user.tg_username, 'bu')
        self.assertEqual(user.phone_number, '+998933459690')
        self.assertEqual(user.phone_number, reverse('users:profile', kwargs={'username':user.username}))




        self.assertEqual