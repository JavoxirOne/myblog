# Generated by Django 4.1.1 on 2022-09-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Views'),
        ),
    ]
