# Generated by Django 2.2 on 2019-06-08 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0006_auto_20190602_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='logo',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logo', to='alsdi.Page'),
        ),
    ]