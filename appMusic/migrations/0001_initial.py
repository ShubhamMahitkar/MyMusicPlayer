# Generated by Django 2.2.12 on 2020-05-06 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('album_images', models.ImageField(upload_to='album_images/')),
            ],
        ),
        migrations.CreateModel(
            name='MusicModel',
            fields=[
                ('songid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('artist', models.CharField(max_length=30)),
                ('song_image', models.ImageField(upload_to='songs_images/')),
                ('song', models.FileField(upload_to='songs/')),
                ('album_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMusic.MovieModel')),
            ],
        ),
    ]