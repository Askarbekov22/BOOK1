# Generated by Django 4.0.1 on 2022-02-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_users', '0002_alter_customuser_gender_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.IntegerField(choices=[(3, 'CLIENT'), (1, 'ADMIN'), (2, 'VIPClient')], default=3, verbose_name='Тип Пользователя'),
        ),
    ]
