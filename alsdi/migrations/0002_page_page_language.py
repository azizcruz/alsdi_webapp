# Generated by Django 2.2 on 2019-06-02 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_language',
            field=models.CharField(default='ar', max_length=255),
            preserve_default=False,
        ),
    ]
