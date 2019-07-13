# Generated by Django 2.1.2 on 2019-07-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0021_auto_20190627_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_num', models.CharField(max_length=50)),
                ('project_subject', models.CharField(max_length=50)),
                ('project_type', models.CharField(max_length=50)),
                ('project_quotation', models.CharField(max_length=50)),
                ('level', models.CharField(blank=True, max_length=50, null=True)),
                ('date_sent', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'المواعيد',
                'verbose_name_plural': 'المواعيد',
                'ordering': ('-date_sent',),
            },
        ),
    ]
