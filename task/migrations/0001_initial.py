# Generated by Django 5.0.6 on 2024-06-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('completed', models.BooleanField()),
                ('published', models.DateField()),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
