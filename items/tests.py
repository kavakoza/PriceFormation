from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User
from django.urls import reverse


class ItemTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(email='test@test.com')
        user.set_password('test')
        user.save()

        token_url = reverse('users:token_obtain_pair')
        resp_token = self.client.post(
            path=token_url, data={'email': 'test@test.com', 'password': 'test'})
        token = resp_token.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.client.post(
            reverse('items:item_create'), {'name': 'Test', 'price': 5, 'final_price': 6.5})

    def test_create_item(self):
        """ Test item creation """
        item_create_url = reverse('items:item_create')
        item_data = {'name': 'Test1', 'price': 15.50, 'final_price': 20.15}
        response = self.client.post(item_create_url, item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_list(self):
        """ Test items list """
        url = reverse('items:items_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json().get('results')), 1)

    def test_item_retrieve(self):
        """ Test item details """
        list_response = self.client.get(reverse('items:items_list'))

        pk = list_response.json()['results'][0]['id']
        url = reverse('items:item_detail', kwargs={'pk': pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_item_delete(self):
        """ Test item deletion """
        list_response = self.client.get(reverse('items:items_list'))

        pk = list_response.json()['results'][0]['id']
        url = reverse('items:item_delete', kwargs={'pk': pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
