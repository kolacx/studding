# Generated by Django 3.1.7 on 2021-04-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0003_auto_20210409_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drfmodel',
            name='age',
            field=models.IntegerField(),
        ),
    ]
