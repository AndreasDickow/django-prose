# Generated by Django 4.1.5 on 2023-01-27 13:26

from django.db import migrations
import prose.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="excerpt",
            field=prose.fields.RichTextField(blank=True),
        ),
    ]
