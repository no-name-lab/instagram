# Generated by Django 5.1.4 on 2024-12-21 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_postlike_unique_together_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentlike',
            name='like',
        ),
    ]
