from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _


class ForcaSeguranca(models.Model):
    """
    Modelo para representar as forças de segurança.
    """

    class TipoForcaSeguranca(models.TextChoices):
        BOMBEIRO = "Bombeiro", _("Bombeiro")
        POLICIA_CIVIL = "PC", _("Polícia Civil")
        POLICIA_MILITAR = "PM", _("Polícia Militar")
        POLICIA_RODOVIARIA_FEDERAL = "PRF", _("Polícia Rodoviária Federal")
        GUARDA_CIVIL_METROPOLITANA = "GCM", _("Guarda Civil Metropolitana")
        FORCAS_ARMADAS = "FA", _("Forças Armadas")
        POLICIA_FEDERAL = "PF", _("Polícia Federal")
        POLICIA_CIENTIFICA = "PCientífica", _("Polícia Científica")
        AGENTES_CARCEIROS = "AgenteCarcereiro", _("Agentes Carcerários")
        POLICIA_TURISMO = "PolíciaTurismo", _("Polícia de Turismo")

    nome = models.CharField(_("Nome da Força de Segurança"), max_length=255)
    descricao = models.TextField(_("Descrição"), blank=True, null=True)
    tipo = models.CharField(
        max_length=20,
        choices=TipoForcaSeguranca.choices,
        default=TipoForcaSeguranca.POLICIA_CIVIL,
        verbose_name=_("Tipo de Força de Segurança"),
    )

    def __str__(self):
        return f"{self.nome} - {self.get_tipo_display()}"


class User(AbstractUser):
    """
    Modelo de usuário customizado para MenteSegura.
    Se adicionar campos que precisam ser preenchidos no cadastro do usuário,
    verifique os formulários SignupForm e SocialSignupForms.
    """

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(_("Nome do Usuário"), max_length=255, blank=True, null=True)
    cpf = models.CharField(_("CPF"), max_length=14, unique=True, null=True, blank=True)
    email = models.EmailField(_("E-mail"), unique=True)
    data_de_cadastro = models.DateTimeField(
        _("Data de Cadastro"), default=now, editable=False
    )

    forca_seguranca = models.ForeignKey(
        ForcaSeguranca,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="usuarios",
        verbose_name=_("Força de Segurança"),
    )
