# Generated by Django 3.0.2 on 2020-05-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmodel',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='views',
        ),
        migrations.RemoveField(
            model_name='questionmodel',
            name='vote_counnt',
        ),
        migrations.AddField(
            model_name='questionmodel',
            name='link',
            field=models.CharField(default='api.stackoverflow.com', max_length=200),
            preserve_default=False,
        ),
    ]
