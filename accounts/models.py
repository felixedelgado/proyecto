from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _

# Create your models here.

# class User(AbstractUser):
#     '''Extiende el Usuario'''

class ManejadorUsuario(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Usuarios deben tener un correo electronico valido.')
        usuario = self.model(
            email=self.normalize_email(email),
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_staffuser(self, email, password):
        usuario = self.create_user(
            email,
            password=password,
        )
        usuario.staff = True
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email,
            password=password,
        )
        usuario.staff = True
        usuario.admin = True
        usuario.save(using=self._db)
        return usuario

class User(AbstractUser):
    email = models.EmailField(verbose_name='correo electrónico', max_length=100, unique=True)
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    active = models.BooleanField(_('Activo'), default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = ('usuarios')
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email
