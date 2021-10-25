# Generated by Django 3.2.8 on 2021-10-25 16:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tags", "0001_initial"),
        ("ideas", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("discussions", "0002_remove_discussioncomment_upvotes"),
    ]

    operations = [
        migrations.RenameField(
            model_name="discussion",
            old_name="user",
            new_name="owner",
        ),
        migrations.RenameField(
            model_name="discussion",
            old_name="name",
            new_name="title",
        ),
        migrations.RemoveField(
            model_name="discussioncomment",
            name="user",
        ),
        migrations.AddField(
            model_name="discussion",
            name="idea",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discussions",
                to="ideas.idea",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="discussioncomment",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="discussion_comments",
                to="accounts.user",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="discussion",
            name="tags",
            field=models.ManyToManyField(
                blank=True, related_name="discussion_tags", to="tags.Tag"
            ),
        ),
        migrations.AlterField(
            model_name="discussioncomment",
            name="discussion",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="discussions.discussion",
            ),
        ),
    ]
