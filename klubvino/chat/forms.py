from django import forms

from chat.models import ChatLog

class ChatForm(forms.ModelForm):

    class Meta:
        model = ChatLog
        fields = ('message', )

        widgets = {
            'message': forms.Textarea(),
        }
