from django.shortcuts import render, redirect, get_object_or_404
from cliente.models import Cliente, Pais
from cliente.forms import ClienteForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required



def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    paises = Pais.objects.all()
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente:cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente/cliente_detail.html', {'form': form, 'cliente': cliente, 'paises': paises})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'clientes': clientes})


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('cliente:mi_cuenta')  # Redirige a la página del cliente después del inicio de sesión

@login_required
def mi_cuenta(request):
    cliente = request.user
    context = {
        'cliente': cliente,
    }
    return render(request, 'cliente/mi_cuenta.html', context)
