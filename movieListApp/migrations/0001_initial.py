# Generated by Django 3.2 on 2021-04-20 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=150)),
                ('release_year', models.DateField(blank=True, null=True)),
                ('director', models.CharField(max_length=150)),
                ('genre', models.CharField(max_length=150)),
            ],
        ),
    ]
