# Generated by Django 3.2.4 on 2021-09-14 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electroApp', '0008_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='user_cart',
        ),
    ]
