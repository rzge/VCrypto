# Generated by Django 4.2.1 on 2023-07-06 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_friends_delete_friendlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bitcoin_address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
