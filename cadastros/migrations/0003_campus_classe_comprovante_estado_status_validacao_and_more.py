# Generated by Django 4.1.7 on 2023-02-19 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastros', '0002_alter_atividade_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=150, verbose_name='endereço')),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('nivel', models.IntegerField(verbose_name='nível')),
                ('descricao', models.CharField(blank=True, max_length=150, null=True, verbose_name='descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Comprovante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data', models.DateField()),
                ('data_final', models.DateField(blank=True, help_text='Informar apenas se o comprovante for relativo a um período.', null=True)),
                ('arquivo', models.FileField(upload_to='pdf/')),
                ('atividade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150, verbose_name='descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Validacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validado_em', models.DateTimeField(auto_now_add=True)),
                ('quantitade', models.DecimalField(decimal_places=2, max_digits=5)),
                ('justificativa', models.TextField(max_length=255)),
                ('comprovante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.comprovante')),
                ('validado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Situacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movimentado_em', models.DateField(auto_now_add=True)),
                ('detalhes', models.CharField(blank=True, max_length=255, null=True)),
                ('movimentado_por', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.status')),
            ],
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('siape', models.CharField(max_length=10)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.campus')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='Progressao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('observacao', models.CharField(max_length=255, verbose_name='observação')),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.classe', verbose_name='classe pretendida')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comprovante',
            name='progressao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.progressao', verbose_name='progressão'),
        ),
        migrations.AddField(
            model_name='comprovante',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.estado')),
            ],
        ),
    ]
