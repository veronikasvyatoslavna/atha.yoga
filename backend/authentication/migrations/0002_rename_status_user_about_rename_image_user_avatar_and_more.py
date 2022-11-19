# Generated by Django 4.1.3 on 2022-11-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="status",
            new_name="about",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="image",
            new_name="avatar",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_instructor",
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
