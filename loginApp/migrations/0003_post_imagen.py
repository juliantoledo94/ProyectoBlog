# Generated by Django 4.0.1 on 2022-01-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0002_rename_contet_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]