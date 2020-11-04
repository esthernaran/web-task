<<<<<<< HEAD
# Generated by Django 3.1.2 on 2020-11-03 19:07
=======
# Generated by Django 3.1.1 on 2020-11-03 19:07
>>>>>>> 7ab73a46d0d831151dd543f7e678e405a017ee87

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_task_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id_document', models.AutoField(primary_key=True, serialize=False)),
                ('document_name', models.CharField(max_length=200)),
                ('archive', models.FileField(upload_to='task/docs')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todo.task')),
            ],
        ),
    ]
