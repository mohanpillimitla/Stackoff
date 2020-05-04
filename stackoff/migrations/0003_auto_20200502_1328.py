# Generated by Django 3.0.2 on 2020-05-02 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoff', '0002_auto_20200502_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionmodel',
            old_name='question',
            new_name='title',
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='query',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]