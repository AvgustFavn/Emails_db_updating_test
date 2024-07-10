from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser, Group, Permission, PermissionsMixin
from django.db import models
from django.utils import timezone

class EmailCredentialsUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

class EmailCredentialsTest(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('email address', unique=True)
    password = models.CharField('password', max_length=255)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    objects = EmailCredentialsUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email

# class EmailCredentialsTest(AbstractUser):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     groups = models.ManyToManyField(
#         Group,
#         related_name='email_credentials_groups',  # add this line
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='email_credentials_user_permissions',  # add this line
#     )
#
#     def __str__(self):
#         return self.email
#
#
class EmailMessageTest(models.Model):
    credentials = models.ForeignKey(EmailCredentialsTest, on_delete=models.CASCADE, related_name='messages_credentials')
    subject = models.CharField(max_length=255)
    sent_date = models.DateTimeField()
    received_date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    attachments = models.TextField(blank=True)

    def __str__(self):
        return self.subject