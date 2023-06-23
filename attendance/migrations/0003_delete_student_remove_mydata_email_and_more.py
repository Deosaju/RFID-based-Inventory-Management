# Generated by Django 4.1.9 on 2023-06-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_mydata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='mydata',
            name='email',
        ),
        migrations.RemoveField(
            model_name='mydata',
            name='message',
        ),
        migrations.AddField(
            model_name='mydata',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mydata',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='mydata',
            name='serial',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
