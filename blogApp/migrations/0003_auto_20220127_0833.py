# Generated by Django 3.1.13 on 2022-01-27 03:03

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20220126_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body_upload',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
