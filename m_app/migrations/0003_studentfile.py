# Generated by Django 5.0.6 on 2024-05-26 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m_app', '0002_studsignup'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emial', models.EmailField(max_length=50)),
                ('certificate', models.FileField(upload_to='')),
            ],
        ),
    ]
