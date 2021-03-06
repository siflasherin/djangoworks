# Generated by Django 3.2.8 on 2021-11-01 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('date_order', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('orderplaced', 'oredrplaced'), ('dispatch', 'dispatch'), ('intransit', 'intransit'), ('delivered', 'delivered'), ('order_cancelled', 'order_cancelled')], default='orderplaced', max_length=120)),
                ('expected_delivery_date', models.DateField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
        ),
    ]
