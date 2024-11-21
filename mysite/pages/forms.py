from django import forms
from django.core.mail import EmailMessage
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(
        label='お名前',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "お名前",
            }
        )
    )
    email = forms.EmailField(
        label='メールアドレス',
        max_length=50,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "メールアドレス",
            }
        )
    )
    subject = forms.CharField(
        label='件名',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "件名",
            }
        )
    )
    message = forms.CharField(
        label='メッセージ',
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "本文",
            }
        )
    )
    
    def send_email(self):
        # ユーザー入力値の取得
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        # --- メール内容の設定 ---

        # 件名
        subject = '[お問い合わせ]{}'.format(subject)

        # 本文
        body = (
            'Taishiのホームページにてお問い合わせがありました。\n\n'
            '送信者: {}\n'.format(name) +
            'メールアドレス:\n' + 
            '{}\n'.format(email) +
            'メッセージ\n' + 
            '{}'.format(message)
        )

        # 送信元メールアドレス (設定から取得)
        from_email = settings.DEFAULT_FROM_EMAIL

        # 送信先メールアドレス (設定から取得)
        to_list = [settings.EMAIL_HOST_USER]
        cc_list = [settings.EMAIL_HOST_USER]

        # メール送信処理
        try:
            msg = EmailMessage(subject=subject, body=body, from_email=from_email, to=to_list, cc=cc_list)
            msg.send()
        except Exception as e:
            print(f"メール送信エラー: {e}") 
            raise forms.ValidationError(f"メール送信中にエラーが発生しました: {e}")
