# Generated by Django 2.0.2 on 2018-03-01 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afrikaquiz', '0004_auto_20180301_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadership',
            name='end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
