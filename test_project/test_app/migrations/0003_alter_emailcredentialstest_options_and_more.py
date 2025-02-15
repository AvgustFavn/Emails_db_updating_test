# Generated by Django 4.2.14 on 2024-07-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('test_app', '0002_emailcredentialstest_emailmessagetest_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailcredentialstest',
            options={},
        ),
        migrations.AlterModelManagers(
            name='emailcredentialstest',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='emailcredentialstest',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='emailcredentialstest',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='emailcredentialstest',
            name='username',
        ),
        migrations.AlterField(
            model_name='emailcredentialstest',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='emailcredentialstest',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='emailcredentialstest',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='emailcredentialstest',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
        migrations.AlterField(
            model_name='emailcredentialstest',
            name='password',
            field=models.CharField(max_length=255, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='emailcredentialstest',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
