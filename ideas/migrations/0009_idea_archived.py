# Generated by Django 3.2.8 on 2021-10-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0008_alter_idea_milestones"),
    ]

    operations = [
        migrations.AddField(
            model_name="idea",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
