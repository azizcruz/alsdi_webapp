# Generated by Django 2.2 on 2019-04-28 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0009_auto_20190428_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='page',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='alsdi.Page'),
        ),
        migrations.AddField(
            model_name='section',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]