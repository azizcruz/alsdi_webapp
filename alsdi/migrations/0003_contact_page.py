# Generated by Django 2.2 on 2019-06-02 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0002_page_page_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='page',
            field=models.ManyToManyField(blank=True, null=True, related_name='contact_us', to='alsdi.Page'),
        ),
    ]