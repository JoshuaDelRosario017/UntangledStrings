# Generated by Django 4.1.3 on 2022-12-29 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untangled', '0005_alter_blogs_blog_pubdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='blog_pubdate',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 2, 42, 31, 317223, tzinfo=datetime.timezone.utc)),
        ),
    ]
