# Generated by Django 4.1.3 on 2022-12-22 07:31

import ckeditor.fields
import datetime
from django.db import migrations, models
import untangled.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('blog_id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('blog_thumbnail', models.ImageField(default='/default.jpg', upload_to=untangled.models.image_path)),
                ('blog_title', models.CharField(max_length=200, verbose_name='Blog Title')),
                ('blog_description', models.CharField(default='', max_length=255, verbose_name='Blog Description')),
                ('blog_body', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Blog Body')),
                ('blog_pubdate', models.DateField(default=datetime.datetime(2022, 12, 22, 7, 31, 8, 479937, tzinfo=datetime.timezone.utc))),
                ('blog_author', models.CharField(default=False, max_length=100, verbose_name='Blog Author')),
                ('blog_userid', models.IntegerField(default=False, verbose_name='user id')),
                ('blog_category', models.CharField(default=False, max_length=50, verbose_name='Blog Category')),
            ],
            options={
                'ordering': ['blog_id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_categories', models.CharField(max_length=50, verbose_name='category')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
