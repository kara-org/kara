from django.db import models
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.db.models import Q


class UsuarioManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('É necessário um Email')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    nome_completo = models.CharField("Nome completo", max_length=255, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(auto_now_add=True)
    usuario_api = models.BooleanField(default=False)
    cpf = models.CharField("CPF", max_length=20, blank=True, null=True)
    foto = models.ImageField("Foto", upload_to= "foto", blank=True, null=True)
    vinculo_ong = models.BooleanField(default=False, blank=True, null=True)
    endereco = models.ForeignKey("Endereco", on_delete=models.DO_NOTHING, blank=True, null=True)

    def save(self, *args, **kwargs):
        return super(Usuario, self).save(*args, **kwargs)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['']
    class Meta:
        verbose_name = 'Usuário'

    def get_full_name(self):
        return '%s <%s>' % (self.nome_completo, self.email)

    def get_short_name(self):
        return self.nome_completo

    def _str_(self):
        return '{nome} - {email}'.format(nome=self.nome_completo, email=self.email)

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def is_active(self):
        return self.ativo

class Endereco(models.Model):
    logradouro = models.TextField("Logradouro")
    bairro = models.CharField("Bairro", max_length=30)
    cidade = models.CharField("Cidade", max_length=30)
    estado = models.CharField("Estado", max_length=30)
    numero = models.IntegerField("Número")
    principal = models.BooleanField("Principal?")
    desabilitado = models.BooleanField(default=False, blank=True, null=True)

    def save(self):
        if self.principal == True:
            query = Endereco.objects.filter(principal=True)
            if query.exists:
                for elemento in query:
                    elemento.principal = False
                    elemento.save()
        super(Endereco, self).save()
            

    def __str__(self):
        return self.bairro + " "+ self.cidade

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class Telefone(models.Model):
    usuario = models.ForeignKey("Usuario", related_name="telefone", on_delete=models.DO_NOTHING, blank=True, null=True)
    numero = models.IntegerField("Número")
    whatsapp = models.BooleanField("Principal?")
    desabilitado = models.BooleanField(default=False, blank=True, null=True)

    def save(self):
        super(Telefone, self).save()
            

    class Meta:
        
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"
        
class UsuarioPertenceOng(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.DO_NOTHING)
    ong = models.OneToOneField("Ong", on_delete=models.DO_NOTHING)
    data_inicio = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "UsuarioPertenceOng"
        verbose_name_plural = "UsuarioPertenceOng"
        
class Ong(models.Model):
    cnpj = models.CharField("CPF", max_length=20, blank=True, null=True)
    historia = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    ultimo_login = models.DateTimeField(auto_now_add=True)
    
class Status(models.Model):
    codigo_status = models.IntegerField("Código status")
    mensagem = models.CharField("Mensagem", max_length=255)
    
class Demanda(models.Model):
    ong = models.OneToOneField("Ong", on_delete=models.DO_NOTHING)
    produto = models.CharField("Produto", max_length=255)
    quantidade_esperada = models.CharField("Quantidade", max_length=20)
    quantidade_alcancada = models.CharField("Quantidade alcançada", max_length=20)
    unidade = models.CharField("Unidade", max_length=5)
    data_inicio = models.DateField("Data inicial")
    data_fim = models.DateField("Data fim")
    sem_limite = models.BooleanField(default=True)
    status = models.ForeignKey("Status", on_delete=models.DO_NOTHING)


class Doacao(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.DO_NOTHING)
    ong = models.OneToOneField("Ong", on_delete=models.DO_NOTHING)    
    demanda = models.OneToOneField("Demanda", on_delete=models.DO_NOTHING) 
    quantidade_reservada = models.CharField("Quantidade reservada", max_length=20)
    data_agendamento = models.DateField("Data agendamento")
    status = models.ForeignKey("Status", on_delete=models.DO_NOTHING)


     
