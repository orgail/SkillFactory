# Generated by Django 3.2.3 on 2021-05-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_rating',
            field=models.IntegerField(default=0),
        ),
    ]
