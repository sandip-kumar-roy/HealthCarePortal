# Generated by Django 4.1.3 on 2023-01-07 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locate_city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='pics')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField(null=True)),
                ('occupation', models.TextField(null=True)),
                ('cost', models.IntegerField(null=True)),
                ('date1', models.CharField(max_length=50, null=True)),
                ('date2', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
