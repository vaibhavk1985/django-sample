from django_messages.forms import ComposeForm
from django_messages.models import Message
from django.utils import timezone
from custom_messages.fields import CommaSeparatedUserField
from django.utils.translation import ugettext_lazy as _


class CustomComposeForm(ComposeForm):
    """
    A simple default form for private messages.
    """
    recipient = CommaSeparatedUserField(label=_(u"Recipient"))

    def __init__(self, *args, **kwargs):
        super(CustomComposeForm, self).__init__(*args, **kwargs)
        # self.fields['recipient'].help_text = "sadsad"
        self.fields['recipient'].widget.attrs.update(
            {'placeholder': 'Please enter username'})
