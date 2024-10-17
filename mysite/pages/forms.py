from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='お名前',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"お名前",
            }
        )
    )
    mail = forms.EmailField(
        label='メールアドレス',
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder":"メールアドレス",
            }
        )
    )
    subject = forms.CharField(
        label='件名',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"件名",
            }
        )
    )
    message = forms.CharField(
        label='メッセージ',
        max_length=50,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder":"本文",
            }
        )
    )
    
    
    