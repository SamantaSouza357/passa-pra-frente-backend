# Generated by Django 2.2.6 on 2019-10-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doador',
            name='confirmEmail',
            field=models.CharField(default='meupao@assado.com', max_length=255),
            preserve_default=False,
        ),
    ]