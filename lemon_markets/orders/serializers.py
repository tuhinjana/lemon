
from rest_framework import serializers
from orders.models import OrdersModel, AccountModel, SideChoices


class OrderSerializer(serializers.ModelSerializer):
    isin = serializers.CharField(required=True, max_length=12)
    valid_until = serializers.DateTimeField(required=True,)
    quantity = serializers.IntegerField(default=1, required=False,)
    limit_price = serializers.DecimalField(required=True, decimal_places=3, max_digits=20,)
    side = serializers.ChoiceField(required=True, choices=SideChoices.SIDE)
    account = serializers.PrimaryKeyRelatedField( read_only=True)

    class Meta:
        model = OrdersModel
        fields = ('account', 'isin', 'limit_price', 'side', 'valid_until', 'quantity')

    def create(self, validated_data):
        return OrdersModel.objects.create(**validated_data)

    @staticmethod
    def validate_account(account_uuid):
        print(account_uuid)
        try:
            account_uuid = account_uuid.replace("-", "")
            return AccountModel.objects.filter(uuid__iexact=str(account_uuid)).get()
        except AccountModel.DoesNotExist as ex:
            raise ex
