# Generated by Django 2.1.5 on 2019-01-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190129_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrante'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='start',
            field=models.TimeField(blank=True, null=True, verbose_name='início'),
        ),
    ]