# Generated by Django 4.1.3 on 2022-11-20 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_user_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default-pp.png', null=True, upload_to='images/'),
        ),
    ]