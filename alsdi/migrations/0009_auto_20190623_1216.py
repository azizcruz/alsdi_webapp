# Generated by Django 2.2 on 2019-06-23 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0008_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-date_created',), 'verbose_name': 'اخر الاخبار'},
        ),
    ]
