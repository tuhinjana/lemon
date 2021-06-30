from django.db import models
import uuid


# Create your models here.
class SideChoices:
    SIDE = [("B", 'buy'), ("S", 'sell')]


class AccountModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    name = models.CharField(blank=False, max_length=50, null=False, verbose_name="Name of Account")
    """
    @property
    def _uuid(self):
        return str(self.uuid)
    """

class OrdersModel(models.Model):
    account = models.ForeignKey(AccountModel, on_delete=models.CASCADE, related_name='orders')

    isin = models.CharField(max_length=12, blank=True, verbose_name='Isin string')
    limit_price = models.DecimalField(decimal_places=3, max_digits=20, null=True, blank=True,
                                      verbose_name='Price of single stock')
    side = models.CharField(max_length=1, choices=SideChoices.SIDE)
    valid_until = models.DateTimeField(blank=False, verbose_name='Date of valid until')
    quantity = models.IntegerField(default=1, blank=False, null=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    @property
    def account_uuid(self):
        return str(self.account.uuid)
