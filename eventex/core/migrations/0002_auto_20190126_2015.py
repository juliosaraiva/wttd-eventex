# Generated by Django 2.1.5 on 2019-01-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'palestrante', 'verbose_name_plural': 'palestrantes'},
        ),
        migrations.AlterField(
            model_name='speaker',
            name='description',
            field=models.TextField(blank=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=255, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.URLField(verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='website',
            field=models.URLField(blank=True, verbose_name='website'),
        ),
    ]
