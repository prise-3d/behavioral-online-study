# Generated by Django 3.2.12 on 2022-02-07 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='progresses',
        ),
        migrations.RemoveField(
            model_name='session',
            name='progresses',
        ),
        migrations.AddField(
            model_name='sessionprogress',
            name='participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='progresses', to='expe.participant'),
        ),
        migrations.AddField(
            model_name='sessionprogress',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='progresses', to='expe.session'),
        ),
    ]
