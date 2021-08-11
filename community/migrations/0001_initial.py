# Generated by Django 3.2.5 on 2021-08-11 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('postId', models.CharField(max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpertRe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postId', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('likes_user', models.ManyToManyField(blank=True, default=0, related_name='likes_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publicSetting', models.CharField(max_length=50)),
                ('password_Post', models.CharField(blank=True, max_length=10, null=True)),
                ('age_tag', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='community/')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('hits', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('password_Post', models.CharField(blank=True, max_length=10, null=True)),
                ('age_tag', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='community/')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('hits', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
