# Generated by Django 4.0.1 on 2022-06-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
        migrations.RemoveField(
            model_name='newsstory',
            name='image_url',
        ),
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.URLField(blank=True, help_text='(Copy Image Address)'),
        ),
    ]
