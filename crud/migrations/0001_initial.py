# Generated by Django 4.2.2 on 2023-06-20 10:51

import crud.utils.set_foreign_null
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('login', models.CharField(blank=True, max_length=10, null=True)),
                ('user_type', models.CharField(choices=[('USER', 'USER'), ('SUDO', 'SUDO'), ('DEALER', 'DEALER')], max_length=20)),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'users',
                'ordering': ['username', 'id'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farm_id', models.CharField(max_length=30, unique=True)),
                ('farm_name', models.CharField(max_length=60)),
                ('farm_city', models.CharField(max_length=60)),
                ('farm_lat', models.FloatField()),
                ('farm_lng', models.FloatField()),
                ('dealer', models.ForeignKey(blank=True, null=True, on_delete=models.SET(crud.utils.set_foreign_null.get_sentinel_user), related_name='dealers_of_farm', to=settings.AUTH_USER_MODEL)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_of_farm', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(blank=True, related_name='users_of_farm', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fazenda',
                'verbose_name_plural': 'Fazendas',
                'db_table': 'farms',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pivots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pivot_num', models.IntegerField(unique=True)),
                ('pivot_id', models.CharField(max_length=60)),
                ('pivot_lng', models.FloatField()),
                ('pivot_lat', models.FloatField()),
                ('radio_id', models.IntegerField(unique=True)),
                ('pivot_start_angle', models.IntegerField()),
                ('pivot_end_angle', models.IntegerField()),
                ('pivot_is_gprs', models.BooleanField(default=False)),
                ('pivot_ip_gateway', models.CharField(blank=True, max_length=60, null=True)),
                ('farm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_of_pivot', to='crud.farm')),
            ],
            options={
                'verbose_name': 'Pivô',
                'verbose_name_plural': 'Pivôs',
                'db_table': 'pivots',
                'ordering': ['pivot_num'],
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_id', models.CharField(max_length=90)),
                ('power', models.BooleanField()),
                ('water', models.BooleanField()),
                ('connection', models.BooleanField()),
                ('pressure', models.BooleanField()),
                ('start_angle', models.IntegerField()),
                ('direction', models.CharField(choices=[('CLOCKWISE', 'CLOCKWISE'), ('ANTI_CLOCKWISE', 'ANTI_CLOCKWISE')], max_length=20)),
                ('timestamp', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=models.SET(crud.utils.set_foreign_null.get_sentinel_user), related_name='author_of_state', to='crud.pivots')),
                ('pivot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_of_state', to='crud.pivots')),
            ],
            options={
                'verbose_name': 'Estados do pivô',
                'verbose_name_plural': 'Estados dos pivôs',
                'db_table': 'states',
                'ordering': ['pivot_id', 'id'],
            },
        ),
        migrations.CreateModel(
            name='SchedulingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduling_id', models.CharField(blank=True, max_length=90, null=True)),
                ('is_stop', models.BooleanField(blank=True, null=True)),
                ('is_return', models.BooleanField(blank=True, null=True)),
                ('power', models.BooleanField()),
                ('water', models.BooleanField()),
                ('direction', models.CharField(choices=[('CLOCKWISE', 'CLOCKWISE'), ('ANTI_CLOCKWISE', 'ANTI_CLOCKWISE')], max_length=20)),
                ('start_date_of_module', models.CharField(max_length=255)),
                ('start_angle', models.IntegerField(blank=True, null=True)),
                ('percentimeter', models.IntegerField(blank=True, null=True)),
                ('start_timestamp', models.DateTimeField(blank=True, null=True)),
                ('end_timestamp', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=models.SET(crud.utils.set_foreign_null.get_sentinel_user), related_name='author_of_scheduling_hist', to=settings.AUTH_USER_MODEL)),
                ('pivot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_of_scheduling_hist', to='crud.pivots')),
            ],
            options={
                'verbose_name': 'Histórico de agendamento',
                'verbose_name_plural': 'Histórico dos agendamentos',
                'db_table': 'scheduling_historys',
                'ordering': ['pivot_id'],
            },
        ),
        migrations.CreateModel(
            name='RadioVariables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radio_variable_id', models.CharField(blank=True, max_length=90, null=True)),
                ('father', models.TextField(blank=True, null=True)),
                ('rssi', models.FloatField(blank=True, null=True)),
                ('noise', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField()),
                ('pivot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_of_radio_variable', to='crud.pivots')),
            ],
            options={
                'verbose_name': 'Sinais do Radio',
                'verbose_name_plural': 'Sinais dos Radios',
                'db_table': 'radio_variables',
                'ordering': ['pivot_id'],
            },
        ),
        migrations.CreateModel(
            name='LastState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angle', models.IntegerField()),
                ('state', models.CharField(max_length=60)),
                ('timestamp', models.DateTimeField()),
                ('farm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='farm_of_last_state', to='crud.farm')),
                ('pivot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pivot_of_last_state', to='crud.pivots')),
            ],
            options={
                'verbose_name': 'Último estado',
                'verbose_name_plural': 'Último estado',
                'db_table': 'last_state',
                'ordering': ['pivot_id'],
            },
        ),
        migrations.CreateModel(
            name='StateVariables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_variable_id', models.CharField(blank=True, max_length=90, null=True)),
                ('angle', models.IntegerField()),
                ('percentimeter', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_of_state_variable', to='crud.states')),
            ],
            options={
                'verbose_name': 'Variável do estado',
                'verbose_name_plural': 'Variáveis dos estados',
                'db_table': 'state_variables',
                'ordering': ['state_id'],
                'indexes': [models.Index(fields=['state_id'], name='state_varia_state_i_09b9f1_idx'), models.Index(fields=['state_id'], name='state_id_name_idx')],
            },
        ),
        migrations.AddIndex(
            model_name='states',
            index=models.Index(fields=['state_id', 'pivot_id'], name='states_state_i_86cf4d_idx'),
        ),
        migrations.AddIndex(
            model_name='states',
            index=models.Index(fields=['state_id'], name='state_name_idx'),
        ),
        migrations.AddIndex(
            model_name='schedulinghistory',
            index=models.Index(fields=['pivot_id', 'scheduling_id'], name='scheduling__pivot_i_461008_idx'),
        ),
        migrations.AddIndex(
            model_name='schedulinghistory',
            index=models.Index(fields=['pivot_id'], name='scheduling_idx'),
        ),
        migrations.AddIndex(
            model_name='radiovariables',
            index=models.Index(fields=['pivot_id'], name='radio_varia_pivot_i_33879c_idx'),
        ),
        migrations.AddIndex(
            model_name='radiovariables',
            index=models.Index(fields=['pivot_id'], name='radio_variable_idx'),
        ),
        migrations.AddIndex(
            model_name='pivots',
            index=models.Index(fields=['pivot_num', 'pivot_id'], name='pivots_pivot_n_fea3f6_idx'),
        ),
        migrations.AddIndex(
            model_name='pivots',
            index=models.Index(fields=['pivot_num'], name='pivot_num_idx'),
        ),
        migrations.AddIndex(
            model_name='laststate',
            index=models.Index(fields=['pivot_id', 'farm_id'], name='last_state_pivot_i_a6ba45_idx'),
        ),
        migrations.AddIndex(
            model_name='laststate',
            index=models.Index(fields=['pivot_id'], name='last_state_name_idx'),
        ),
        migrations.AddIndex(
            model_name='farm',
            index=models.Index(fields=['farm_name', 'farm_id'], name='farms_farm_na_cbf02b_idx'),
        ),
        migrations.AddIndex(
            model_name='farm',
            index=models.Index(fields=['farm_name'], name='farm_name_idx'),
        ),
        migrations.AddIndex(
            model_name='soiluser',
            index=models.Index(fields=['username'], name='users_usernam_baeb4b_idx'),
        ),
        migrations.AddIndex(
            model_name='soiluser',
            index=models.Index(fields=['username'], name='user_name_idx'),
        ),
    ]
