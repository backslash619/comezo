# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-02 17:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_text', models.CharField(max_length=255)),
                ('correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('q_text', models.TextField(max_length=1000)),
                ('hint', models.CharField(blank=True, default='', max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ques_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(choices=[(1, 'Math'), (5, 'English'), (3, 'Physics'), (4, 'Biology'), (2, 'Chemistry')])),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='questions',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='API.Tags'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_question', to='API.Questions'),
        ),
    ]