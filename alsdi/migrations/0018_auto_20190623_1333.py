# Generated by Django 2.2 on 2019-06-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alsdi', '0017_auto_20190623_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'البومات الصور', 'verbose_name_plural': 'البومات الصور'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'عناوين التواصل', 'verbose_name_plural': 'عنواين التواصل'},
        ),
        migrations.AlterModelOptions(
            name='imagesalbum',
            options={'verbose_name': 'صور الالبومات', 'verbose_name_plural': 'صور الالبومات'},
        ),
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'شعار الموقع', 'verbose_name_plural': 'شعار الموقع'},
        ),
        migrations.AlterModelOptions(
            name='navbarlinks',
            options={'ordering': ('weight',), 'verbose_name': 'روابط النافبار', 'verbose_name_plural': 'روابط النافبار'},
        ),
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name': 'الصفحات', 'verbose_name_plural': 'الصفحات'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-date_created',), 'verbose_name': 'المشاريع', 'verbose_name_plural': 'المشاريع'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('weight',), 'verbose_name': 'جزئية', 'verbose_name_plural': 'جزئية'},
        ),
        migrations.AlterModelOptions(
            name='sectionblock',
            options={'ordering': ('weight',), 'verbose_name': 'بلوكات الجزئية', 'verbose_name_plural': 'بلوكات الجزئية'},
        ),
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ('weight',), 'verbose_name': 'سلايد', 'verbose_name_plural': 'سلايد'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ('weight',), 'verbose_name': 'سلايدر', 'verbose_name_plural': 'سلايدر'},
        ),
    ]
