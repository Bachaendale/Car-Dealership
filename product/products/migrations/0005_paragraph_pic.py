# Generated by Django 5.0.1 on 2024-02-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_text_here_paragraph_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]