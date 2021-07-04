# Generated by Django 3.0.4 on 2021-06-27 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anatomy', '0003_auto_20210623_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=10)),
                ('sequenceid', models.CharField(max_length=20)),
                ('sequencefeature', models.IntegerField()),
                ('dnaseqlength', models.IntegerField()),
                ('mrnasequencelength', models.IntegerField()),
                ('proteinSequenceLength', models.IntegerField()),
                ('L', models.IntegerField()),
                ('S', models.IntegerField()),
                ('T', models.IntegerField()),
                ('C', models.IntegerField()),
                ('F', models.IntegerField()),
                ('R', models.IntegerField()),
                ('V', models.IntegerField()),
                ('Y', models.IntegerField()),
                ('N', models.IntegerField()),
                ('I', models.IntegerField()),
                ('K', models.IntegerField()),
                ('G', models.IntegerField()),
                ('A', models.IntegerField()),
                ('Q', models.IntegerField()),
                ('P', models.IntegerField()),
                ('D', models.IntegerField()),
                ('E', models.IntegerField()),
                ('W', models.IntegerField()),
                ('M', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anatomy.SequenceTest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
