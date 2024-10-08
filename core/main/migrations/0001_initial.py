# Generated by Django 5.1 on 2024-08-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talked_time', models.PositiveIntegerField(verbose_name='MeetInfo talking time')),
                ('microphone_used', models.PositiveIntegerField(verbose_name='MeetInfo microfone used')),
                ('speaker_used', models.PositiveIntegerField(verbose_name='MeetInfo speaker used')),
                ('voice_sentiment', models.PositiveIntegerField(verbose_name='MeetInfo voice_sentiment')),
            ],
        ),
    ]
