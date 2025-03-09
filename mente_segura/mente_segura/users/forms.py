from allauth.account.forms import SignupForm
from allauth.socialaccount.forms import SignupForm as SocialSignupForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .models import ForcaSeguranca, User


# Formulário de alteração do usuário no admin
class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):  # type: ignore[name-defined]
        model = User


# Formulário de criação do usuário no admin
class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Formulário para a criação de usuários na área administrativa.
    Para alterar o cadastro do usuário, veja UserSignupForm e UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):  # type: ignore[name-defined]
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")},
        }


# Formulário de cadastro de usuários no site (sem conta social)
class UserSignupForm(SignupForm):
    """
    Formulário que será renderizado na seção de cadastro de usuário.
    Os campos padrão serão adicionados automaticamente.
    Verifique UserSocialSignupForm para contas criadas via social.
    """

    # Campos personalizados
    name = forms.CharField(max_length=255, label=_("Nome"), required=False)
    cpf = forms.CharField(max_length=14, label=_("CPF"), required=False)
    forca_seguranca = forms.ModelChoiceField(
        queryset=ForcaSeguranca.objects.all(),
        label=_("Força de Segurança"),
        required=False,
        empty_label=_("Selecione a Força de Segurança"),
    )

    class Meta:
        model = User
        fields = ["username", "email", "name", "cpf", "forca_seguranca"]

    def save(self, request):
        """
        Sobrescrevendo o método `save` para garantir que os campos personalizados sejam salvos corretamente.
        """
        user = super().save(request)
        user.name = self.cleaned_data.get("name")
        user.cpf = self.cleaned_data.get("cpf")
        user.forca_seguranca = self.cleaned_data.get("forca_seguranca")
        user.data_de_cadastro = now()  # Definindo a data de cadastro automaticamente
        user.save()
        return user


# Formulário de cadastro de usuários que usam contas sociais
class UserSocialSignupForm(SocialSignupForm):
    """
    Renderiza o formulário quando o usuário se cadastrar utilizando contas sociais.
    Os campos padrão serão adicionados automaticamente.
    Veja UserSignupForm para cadastros normais.
    """

    # Campos personalizados
    name = forms.CharField(max_length=255, label=_("Nome"), required=False)
    cpf = forms.CharField(max_length=14, label=_("CPF"), required=False)
    forca_seguranca = forms.ModelChoiceField(
        queryset=ForcaSeguranca.objects.all(),
        label=_("Força de Segurança"),
        required=False,
        empty_label=_("Selecione a Força de Segurança"),
    )

    class Meta:
        model = User
        fields = ["username", "email", "name", "cpf", "forca_seguranca"]

    def save(self, request):
        """
        Sobrescrevendo o método `save` para garantir que os campos personalizados sejam salvos corretamente.
        """
        user = super().save(request)
        user.name = self.cleaned_data.get("name")
        user.cpf = self.cleaned_data.get("cpf")
        user.forca_seguranca = self.cleaned_data.get("forca_seguranca")
        user.data_de_cadastro = now()  # Definindo a data de cadastro automaticamente
        user.save()
        return user
