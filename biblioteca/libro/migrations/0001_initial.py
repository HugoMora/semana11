# Generated by Django 2.2.6 on 2019-10-26 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('precio_por_dia', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LibroCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Categoria')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='AlquilerDetalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_alquiler', models.DateField(auto_now_add=True)),
                ('cantidad_dias', models.IntegerField()),
                ('id_alquiler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Alquiler')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Libro')),
                ('id_tarifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Tarifa')),
            ],
        ),
        migrations.AddField(
            model_name='alquiler',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Persona'),
        ),
    ]
