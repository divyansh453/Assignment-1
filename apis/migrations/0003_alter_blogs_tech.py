# Generated by Django 4.1.2 on 2023-05-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_rename_community_questions_blogs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='tech',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
