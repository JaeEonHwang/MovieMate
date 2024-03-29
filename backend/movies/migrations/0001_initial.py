# Generated by Django 4.2.4 on 2023-11-18 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('name_en', models.CharField(max_length=20, unique=True)),
                ('name_ko', models.CharField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('imdb_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('adult', models.BooleanField()),
                ('homepage', models.CharField(blank=True, max_length=100)),
                ('overview', models.TextField(blank=True, default='')),
                ('popularity', models.FloatField(default=0)),
                ('release_date', models.CharField(max_length=20)),
                ('runtime', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('tagline', models.CharField(default='', max_length=200)),
                ('now_playing', models.BooleanField(default=False)),
                ('top_rated', models.BooleanField(default=False)),
                ('upcoming', models.BooleanField(default=False)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.genres')),
                ('related_movie', models.ManyToManyField(to='movies.movies')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('imdb_id', models.CharField(blank=True, max_length=20, unique=True)),
                ('birthday', models.CharField(blank=True, max_length=20)),
                ('name_en', models.CharField(max_length=100)),
                ('popularity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_en', models.CharField(max_length=20, unique=True)),
                ('department_ko', models.CharField(default=models.CharField(max_length=20, unique=True), max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('youtube_path', models.CharField(max_length=100)),
                ('official', models.BooleanField()),
                ('published_at', models.CharField(max_length=50)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='movies.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_path', models.CharField(default='https://media.istockphoto.com/id/1164822188/vector/male-avatar-profile-picture.jpg?s=612x612&w=0&k=20&c=KPsLgVIwEGdDvf4_kiynCXw96p_PhBjIGdU68qkpbuI=', max_length=100)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to='movies.people')),
            ],
        ),
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('movies', models.ManyToManyField(related_name='keywords', to='movies.movies')),
            ],
        ),
        migrations.CreateModel(
            name='ImagePaths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='movies.movies')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.imagetypes')),
            ],
        ),
        migrations.CreateModel(
            name='Credits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(blank=True, max_length=100)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='movies.movies')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='movies.people')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.roles')),
            ],
        ),
    ]
