# Generated by Django 3.0.4 on 2020-07-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20200701_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=200),
        ),
    ]
