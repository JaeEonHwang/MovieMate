# Generated by Django 4.2.4 on 2023-11-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_imagepaths_movie_alter_imagepaths_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='imdb_id',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='imdb_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
