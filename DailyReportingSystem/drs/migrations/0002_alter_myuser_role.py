# Generated by Django 3.2.9 on 2021-11-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('telecaller', 'telecaller'), ('counselor', 'telecaller')], default='telecaller', max_length=12),
        ),
    ]
