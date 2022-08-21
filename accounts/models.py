from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext as _

# Create your models here.

# class User(AbstractUser):
#     '''Extiende el Usuario'''

class ManejadorUsuario(BaseUserManager):
    def create_user(self, correo, password=None):
        if not correo:
            raise ValueError('Usuarios deben tener un correo electronico valido.')
        usuario = self.model(
            correo=self.normalize_email(correo),
        )

        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_staffuser(self, correo, password):
        usuario = self.create_user(
            correo,
            password=password,
        )
        usuario.staff = True
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, correo, password):
        usuario = self.create_user(
            correo,
            password=password,
        )
        usuario.staff = True
        usuario.admin = True
        usuario.save(using=self._db)
        return usuario

class User(AbstractUser):
    correo = models.EmailField(verbose_name='correo electrónico', max_length=100, unique=True)
    nombre =models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    active = models.BooleanField(_('Activo'), default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = ('usuarios')
    
    def get_full_name(self):
        return self.nombre + ' ' + self.apellido

    def get_short_name(self):
        return self.nombre

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
        return self.nombre + ' ' + self.apellido + ' ' + self.correo




    # name = models.CharField(max_length=25, null=False)
    # lastname = models.CharField(max_length=25, null=False)
    # password = models.
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # active = models.TextField(default=True)
    # slug = models.SlugField(max_length=255, unique=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    # image = models.ImageField(upload_to='images/<str:user>', blank=True, null=True)
    # def __str__(self):
    #     return self.name

