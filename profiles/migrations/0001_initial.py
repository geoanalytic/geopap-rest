# Generated by Django 2.0.3 on 2018-04-10 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basemap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='', max_length=100)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
                ('size', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Otherfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='', max_length=100)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField()),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('color', models.CharField(default='#FBC02D', max_length=30)),
                ('active', models.BooleanField(default=False)),
                ('sdcardPath', models.CharField(default='MAINSTORAGE', max_length=100)),
                ('mapView', models.CharField(default='52.02025604248047,-115.70208740234375,10.0', max_length=100)),
                ('basemaps', models.ManyToManyField(to='profiles.Basemap')),
                ('otherfiles', models.ManyToManyField(to='profiles.Otherfiles')),
            ],
            options={
                'ordering': ('modifieddate', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='', max_length=100)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
                ('uploadurl', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spatialdbs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='', max_length=100)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
                ('size', models.IntegerField(blank=True)),
                ('uploadurl', models.URLField(blank=True)),
                ('visible', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, default='', max_length=100)),
                ('modifieddate', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='spatialdbs',
            field=models.ManyToManyField(to='profiles.Spatialdbs'),
        ),
        migrations.AddField(
            model_name='profile',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Tag'),
        ),
    ]