# Generated by Django 5.0.4 on 2024-04-19 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_preview_alter_blog_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='preview',
            field=models.ImageField(blank=True, default='0', null=True, upload_to='', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.BooleanField(blank=True, default='True', null=True, verbose_name='опубликовано'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='просмотры'),
        ),
    ]
