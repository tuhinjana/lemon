from django.test import TestCase
from django.urls import reverse
from orders.models import AccountModel
from uuid import uuid4


class ViewTests(TestCase):
    UUID = str(uuid4())

    def setUp(self):
        AccountModel.objects.create(uuid=str(self.UUID), name='test account')

    def test_post_create_order(self):
        payload_data = {
            "isin": "b9dbbdc6",
            "valid_until": "2021-07-26 10:19:20",
            "limit_price": 10.25,
            "side": "B"
        }
        account_obj = AccountModel.objects.all().first()
        print(account_obj.uuid)
        url = reverse("orders:create_order", kwargs={"account_uuid": str(account_obj.uuid)})
        print(url)
        response = self.client.post(reverse("orders:create_order", kwargs={"account_uuid": str(account_obj.uuid)}),
                                    data=payload_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json().get("isin"), payload_data["isin"])
