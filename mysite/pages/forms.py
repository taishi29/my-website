from django import forms
from django.core.mail import EmailMessage

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

        # 送信元メールアドレス
        from_email = 'taishi03929@gmail.com'

        # 送信先メールアドレス
        to_list = ['taishi03929@gmail.com']

        # CCリスト
        cc_list = ['taishi03929@gmail.com']

        # メール送信処理
        msg = EmailMessage(subject=subject, body=body, from_email=from_email, to=to_list, cc=cc_list)
        msg.send()
