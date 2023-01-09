# Generated by Django 4.1.3 on 2022-12-29 02:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('untangled', '0002_blogs_deleted_on_alter_blogs_blog_pubdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='blog_pubdate',
            field=models.DateField(default=datetime.datetime(2022, 12, 29, 2, 7, 9, 865701, tzinfo=datetime.timezone.utc)),
        ),
    ]
