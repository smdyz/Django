# Generated by Django 5.0.4 on 2024-05-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_delete_users_alter_version_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, null=True, verbose_name='автор'),
        ),
    ]
