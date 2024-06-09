from django.shortcuts import render, redirect, get_object_or_404
from cliente.models import Cliente, Pais
from cliente.forms import ClienteForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    paises = Pais.objects.all()
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/core/register/')
        
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_detail.html', {'form': form, 'cliente': cliente, 'paises': paises})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('cliente:index')  # Redirige a la página del cliente después del inicio de sesión

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    cliente = Cliente.objects.get(user=request.user)
    return render(request, 'cliente/index.html', {'cliente': cliente})
def index(request):
    try:
        cliente = request.user.cliente
        context = {
            'cliente': cliente,
            'user': request.user,
        }
        return render(request, 'cliente/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('core:register'))


def register(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST, request.FILES)
        if  cliente_form.is_valid():
            cliente.set_password(user_form.cleaned_data['password'])
            cliente.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            return redirect('login')
    else:
        cliente_form = ClienteForm()
    return render(request, 'core/register.html', {
        'cliente_form': cliente_form
    })


def crear_actualizar_cliente(request, cliente_id=None):
    if cliente_id:
        cliente = Cliente.objects.get(id=cliente_id)
    else:
        cliente = None

    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('ruta_de_redireccion')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'formulario_cliente.html', {'form': form, 'cliente': cliente})

def listar_paises(request):
    paises = Pais.objects.all()
    return render(request, 'lista_paises.html', {'paises': paises})


