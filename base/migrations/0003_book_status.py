# Generated by Django 3.0.6 on 2020-07-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable')], max_length=200, null=True),
        ),
    ]