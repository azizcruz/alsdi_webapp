# Generated by Django 2.2 on 2019-06-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0019_article_is_new_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
