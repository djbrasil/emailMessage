from django.shortcuts import render, redirect 
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect 
from .forms import ContatoForm 
 
# funcao contato
def contato(request):
    form = ContatoForm(request.POST or None) 
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail() 
            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {'form': form}
    return render(request, 'contato.html', context)