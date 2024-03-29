# Generated by Django 2.2.4 on 2019-09-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suldocs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('affiliation', models.CharField(blank=True, max_length=128)),
                ('iam_key', models.CharField(blank=True, max_length=128)),
                ('iam_value', models.CharField(blank=True, max_length=128)),
                ('is_valid', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
