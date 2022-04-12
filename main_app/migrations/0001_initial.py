# Generated by Django 4.0.4 on 2022-04-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.IntegerField(default=0)),
                ('title', models.CharField(default='', max_length=255)),
                ('price_without_disc', models.IntegerField(default=0)),
                ('price_with_disc', models.IntegerField(default=0)),
                ('brand', models.CharField(default='', max_length=255)),
                ('provider', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
