# Generated by Django 4.0.2 on 2022-04-29 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Name')),
                ('anons', models.CharField(max_length=250, verbose_name='Anons')),
                ('full_text', models.TextField(verbose_name='Statya')),
            ],
        ),
        migrations.CreateModel(
            name='Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Мақала',
                'verbose_name_plural': 'Мақалалар',
                'ordering': ['title', 'content'],
            },
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('number', models.IntegerField(validators=[django.core.validators.MinValueValidator(10000), django.core.validators.MaxValueValidator(100000000000)])),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=10000)),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='MenPrize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullnames', models.CharField(max_length=50)),
                ('medaltype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mvideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcountry', models.CharField(max_length=50)),
                ('mtext', models.TextField(max_length=5000)),
                ('msportsmen', models.CharField(max_length=50)),
                ('mcaption', models.CharField(max_length=100)),
                ('mvideo', models.FileField(upload_to='video/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Women',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=10000)),
                ('text', models.CharField(max_length=10000)),
            ],
        ),
    ]
