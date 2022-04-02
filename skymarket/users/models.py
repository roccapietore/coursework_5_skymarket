from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.managers import UserManager, UserRole


class User(AbstractBaseUser):
    first_name = models.CharField(
        verbose_name="name", max_length=50, help_text="Max length 50 characters"
    )
    last_name = models.CharField(
        verbose_name="surname", max_length=100, help_text="Max length 100 characters"
    )
    phone = PhoneNumberField()
    email = models.EmailField(verbose_name="email", unique=True)
    role = models.CharField(
        max_length=20, choices=UserRole.choices, default=UserRole.USER
    )
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_user(self):
        return self.role == UserRole.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("id",)


