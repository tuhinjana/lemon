from django.test import TestCase
from orders.models import AccountModel, OrdersModel
from uuid import uuid4
from orders.serializers import OrderSerializer
from unittest.mock import Mock


class SerializerTests(TestCase):
    UUID = str(uuid4())

    def setUp(self):
        AccountModel.objects.create(uuid=str(self.UUID), name='test account')

    def test_validate_account(self):
        account_obj = OrderSerializer.validate_account(self.UUID)
        self.assertIsNotNone(account_obj)
        self.assertEqual(str(account_obj.uuid), self.UUID)

    def test_serializer_create(self):
        request = Mock()
        payload_data = {
            "isin": "b9dbbdc6",
            "valid_until": "2021-07-26 10:19:20",
            "limit_price": 10.25,
            "side": "B"
        }
        request.data = payload_data
        account_obj = OrderSerializer.validate_account(self.UUID)

        serializer = OrderSerializer(data=request.data)
        self.assertTrue(serializer.is_valid())
        serializer.save(account=account_obj)
        new_obj = OrdersModel.objects.all().last()
        self.assertEqual(str(serializer.data.get("account")), str(new_obj.account.uuid))
