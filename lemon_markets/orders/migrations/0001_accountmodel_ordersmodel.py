# Generated by Django 2.2.4 on 2021-06-21 17:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    operations = [
        migrations.CreateModel(
            name='AccountModel',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name of Account')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isin', models.CharField(blank=True, max_length=12, verbose_name='Isin string')),
                ('limit_price', models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True, verbose_name='Price of single stock')),
                ('side', models.CharField(choices=[('B', 'buy'), ('S', 'sell')], max_length=1)),
                ('valid_until', models.DateTimeField(verbose_name='Date of valid until')),
                ('quantity', models.IntegerField(default=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.AccountModel')),
            ],
        ),
    ]
