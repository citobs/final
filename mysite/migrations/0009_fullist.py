# Generated by Django 4.1.3 on 2022-12-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='fullist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emot', models.CharField(max_length=300, null=True)),
                ('sea', models.CharField(max_length=300, null=True)),
                ('first', models.CharField(max_length=300, null=True)),
                ('second', models.CharField(max_length=300, null=True)),
                ('third', models.CharField(max_length=300, null=True)),
                ('cr_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('fourth', models.CharField(max_length=300, null=True)),
                ('fifth', models.CharField(max_length=300, null=True)),
                ('wea', models.CharField(max_length=300, null=True)),
            ],
        ),
    ]
