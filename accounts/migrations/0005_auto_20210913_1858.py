# Generated by Django 3.2.7 on 2021-09-13 13:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0004_auto_20210913_1858"),
        ("tags", "0002_alter_tag_name"),
        ("accounts", "0004_auto_20210911_2203"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="favourite_tags",
            field=models.ManyToManyField(
                blank=True, related_name="favorited_by", to="tags.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="followers", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="saved_ideas",
            field=models.ManyToManyField(
                blank=True, related_name="saved_by", to="ideas.Idea"
            ),
        ),
    ]
