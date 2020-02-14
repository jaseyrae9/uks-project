# Generated by Django 3.0.2 on 2020-02-14 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('state', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed')], default='OP', max_length=2)),
                ('create_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uks_app.Event')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uks_app.event',),
        ),
        migrations.CreateModel(
            name='IssueChange',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uks_app.Event')),
                ('state', models.CharField(choices=[('OP', 'Open'), ('CL', 'Closed')], default='OP', max_length=2)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uks_app.event',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ObservedProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('git_repo', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('public', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True, max_length=200)),
                ('issue', models.ManyToManyField(related_name='milestones', to='uks_app.Issue')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.ObservedProject')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('issue', models.ManyToManyField(related_name='labels', to='uks_app.Issue')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.ObservedProject'),
        ),
        migrations.AddField(
            model_name='event',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.Issue'),
        ),
        migrations.AddField(
            model_name='event',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_uks_app.event_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CodeChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=400)),
                ('date_time', models.DateTimeField()),
                ('github_username', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.ObservedProject')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsibleUserChange',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uks_app.Event')),
                ('responsibleUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uks_app.event',),
        ),
        migrations.CreateModel(
            name='MilestoneChange',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uks_app.Event')),
                ('add', models.BooleanField()),
                ('checkpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.Milestone')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uks_app.event',),
        ),
        migrations.CreateModel(
            name='CommentChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newComment', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.Comment')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='CodeChangeEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='uks_app.Event')),
                ('closing_event', models.BooleanField(default=False)),
                ('code_change', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uks_app.CodeChange')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('uks_app.event',),
        ),
    ]
