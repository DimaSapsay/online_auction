# Generated by Django 3.0.3 on 2020-02-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_check',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
