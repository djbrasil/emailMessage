from django import forms
from django.core.mail.message import EmailMessage 

# modelos do formulario de contato
class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # funcao que envia email EmailMessage
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'

        # EmailMessage é core mail do django
        mail = EmailMessage(
            subject='E-mail enviado django',
            body=conteudo,
            from_email='br.leticia@hotmail.com',
            to=['br.leticia@hotmail.com',],
            headers={'Reply-To': email}
        )
        mail.send()