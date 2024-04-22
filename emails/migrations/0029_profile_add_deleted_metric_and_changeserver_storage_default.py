# Generated by Django 2.2.24 on 2021-10-19 15:38

from django.db import migrations, models

import emails.models


class Migration(migrations.Migration):
    dependencies = [
        ("emails", "0028_copy_subdomain_to_registeredsubdomain"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="num_email_blocked_in_deleted_address",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile",
            name="num_email_forwarded_in_deleted_address",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="profile",
            name="num_email_spam_in_deleted_address",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="profile",
            name="server_storage",
            field=models.BooleanField(default=emails.models.default_server_storage),
        ),
    ]
