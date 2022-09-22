# Generated by Django 4.1 on 2022-09-21 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_curso', models.CharField(max_length=100, verbose_name='Nombre del Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=20, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=20, verbose_name='Apellidos')),
                ('nombre_completo', models.CharField(blank=True, max_length=40, verbose_name='Nombre Completo')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tema', models.CharField(max_length=100, verbose_name='Nombre Tema')),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prueba', models.CharField(max_length=100, verbose_name='Nombre Prueba')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pruebas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=100, verbose_name='Pregunta')),
                ('prueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.prueba')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tema')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EstudiantePreguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcto', models.BooleanField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.estudiante')),
                ('preguntas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.preguntas')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='preguntas',
            field=models.ManyToManyField(blank=True, through='base.EstudiantePreguntas', to='base.preguntas'),
        ),
    ]