# Generated by Django 4.1.11 on 2023-09-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserEmail', models.EmailField(max_length=320, unique=True, verbose_name='email')),
                ('UserPasswordHash', models.CharField(max_length=256, verbose_name='pass')),
            ],
        ),
    ]
