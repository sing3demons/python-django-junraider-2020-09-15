# Generated by Django 4.1.1 on 2022-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='special_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
