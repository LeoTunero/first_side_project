# Generated by Django 4.0.dev20210713082503 on 2021-08-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(default='Honda', max_length=20)),
                ('car_model', models.TextField(default='EK9')),
                ('last_modify_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Essay', 'verbose_name_plural': 'Essays'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
