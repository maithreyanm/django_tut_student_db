# Generated by Django 3.1.4 on 2021-01-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_ap', '0006_auto_20210106_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_1', models.EmailField(max_length=254)),
                ('email_2', models.EmailField(max_length=254)),
            ],
        ),
    ]
