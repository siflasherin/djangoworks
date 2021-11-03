# Generated by Django 3.2.8 on 2021-11-02 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('orderplaced', 'orderplaced'), ('dispatch', 'dispatch'), ('intransit', 'intransit'), ('delivered', 'delivered'), ('order_cancelled', 'order_cancelled')], default='orderplaced', max_length=100)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobile.cart')),
            ],
        ),
    ]
