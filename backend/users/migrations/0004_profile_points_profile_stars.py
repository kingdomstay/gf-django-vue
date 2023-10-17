# Generated by Django 4.2.6 on 2023-10-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_delete_visitor_alter_profile_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="points",
            field=models.SmallIntegerField(default=1, verbose_name="Баллы"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="stars",
            field=models.SmallIntegerField(default=1, verbose_name="Звездочки"),
            preserve_default=False,
        ),
    ]
