# Generated by Django 3.2.12 on 2022-02-05 17:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EndPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('javascripts', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/js/classical.js', 'experiment/js/classical.js')], max_length=26, null=True)),
                ('styles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=31, null=True)),
                ('content', models.JSONField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('template', models.CharField(choices=[('pages/end/classical_end.html', 'pages/end/classical_end.html')], help_text='You can add templates into: pages/end/classical_end.html', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExamplePage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('javascripts', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/js/classical.js', 'experiment/js/classical.js')], max_length=26, null=True)),
                ('styles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=31, null=True)),
                ('content', models.JSONField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('template', models.CharField(choices=[('pages/examples/classical_example.html', 'pages/examples/classical_example.html')], help_text='You can add templates into: pages/examples/classical_example.html', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('progress_choice', models.CharField(choices=[('default', 'default')], help_text='You can add progress classes into: expe/experiments', max_length=255)),
                ('estimated_duration', models.DurationField(default=datetime.timedelta(0), help_text='hh:mm:ss')),
                ('config', models.JSONField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, help_text='This field is not required and will be generated automatically when the object is saved based on the title of the experiment', max_length=255, unique=True)),
                ('description', models.TextField()),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('end_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='experiment', to='expe.endpage')),
                ('example_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='experiment', to='expe.examplepage')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ExperimentSession',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'Active'), (0, 'Inactive')], default=1, help_text='Session will be displayed but not accessible', null=True)),
                ('is_available', models.IntegerField(blank=True, choices=[(1, 'Available'), (0, 'Disabled')], default=1, help_text='Session will not be displayed if disabled', null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sessions', to='expe.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='InformationPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('javascripts', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/js/classical.js', 'experiment/js/classical.js')], max_length=26, null=True)),
                ('styles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=31, null=True)),
                ('content', models.JSONField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('template', models.CharField(choices=[('pages/information/classical_information.html', 'pages/information/classical_information.html')], help_text='You can add templates into: pages/information/classical_information.html', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('javascripts', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/js/classical.js', 'experiment/js/classical.js')], max_length=26, null=True)),
                ('styles', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('experiment/css/hide_sidebar.css', 'experiment/css/hide_sidebar.css')], max_length=31, null=True)),
                ('content', models.JSONField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('template', models.CharField(choices=[('pages/main/classical_main.html', 'pages/main/classical_main.html')], help_text='You can add templates into: pages/main/classical_main.html', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserExperiment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sessions', models.ManyToManyField(editable=False, related_name='users', to='expe.ExperimentSession')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='ExperimentStep',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('progress_id', models.PositiveIntegerField()),
                ('binary', models.BinaryField(blank=True, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('progress_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='steps', to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddField(
            model_name='experiment',
            name='information_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='experiment', to='expe.informationpage'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='main_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='experiment', to='expe.mainpage'),
        ),
        migrations.CreateModel(
            name='ClassicalExperimentProgress',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='progress', to='expe.experimentsession')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='progress', to='expe.userexperiment')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
