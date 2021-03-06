# Generated by Django 3.0.8 on 2020-08-11 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Maximum length is 255 symbols', max_length=255, verbose_name='Pair name')),
            ],
            options={
                'verbose_name': 'Pair',
                'verbose_name_plural': 'Pairs',
            },
        ),
        migrations.CreateModel(
            name='PairRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField(verbose_name='Crypto volume')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='TimeStamp')),
                ('pair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='crypto.Pair', verbose_name='Pair')),
            ],
        ),
    ]
