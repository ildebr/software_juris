# Generated by Django 3.2.5 on 2021-10-29 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juris', '0002_auto_20211029_0236_squashed_0003_alter_proceeding_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legalrecord',
            name='end_date',
            field=models.DateField(blank=True, verbose_name='fecha de conclusión'),
        ),
    ]
