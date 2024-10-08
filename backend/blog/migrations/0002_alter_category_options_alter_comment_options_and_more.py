# Generated by Django 5.1 on 2024-09-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '   Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': '  Posts'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': ' Tags'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='articles/'),
        ),
    ]
