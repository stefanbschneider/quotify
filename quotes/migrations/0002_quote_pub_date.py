# Generated by Django 3.0.7 on 2020-06-15 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]