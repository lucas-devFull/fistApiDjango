# Generated by Django 3.0.6 on 2020-06-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200603_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefone',
            name='telefone',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
