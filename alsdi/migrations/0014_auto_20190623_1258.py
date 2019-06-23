# Generated by Django 2.2 on 2019-06-23 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0013_auto_20190623_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='page',
        ),
        migrations.AddField(
            model_name='article',
            name='section',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='alsdi.Section'),
            preserve_default=False,
        ),
    ]