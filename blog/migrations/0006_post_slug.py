# Generated by Django 4.1.1 on 2022-09-13 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_post_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
