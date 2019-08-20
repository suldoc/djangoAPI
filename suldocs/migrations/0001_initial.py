# Generated by Django 2.0.13 on 2019-08-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suldoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('stars_taste', models.IntegerField()),
                ('stars_costvalue', models.IntegerField()),
                ('img_path', models.CharField(max_length=1000)),
            ],
        ),
    ]
