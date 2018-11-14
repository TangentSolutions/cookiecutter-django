from django.contrib.auth import get_user_model, forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from common.forms.fields import LuhnField


User = get_user_model()


class UpdateUserDetailForm(ModelForm):
    """Form for users to update their information."""

    id_number = LuhnField(min_length=13)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'id_number')


class UserChangeForm(forms.UserChangeForm):
    """Custom form for the admin interface to update users."""

    id_number = LuhnField(min_length=13)

    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    """Custom form for the admin interface to create users."""

    error_message = forms.UserCreationForm.error_messages.update(
        {'duplicate_username': _('This username has already been taken.')}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self) -> str:
        """Validate the username to ensure it is unique."""

        username = self.cleaned_data['username']

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages['duplicate_username'])
