from django.test import TestCase
from django.urls import reverse
from cliente.models import CustomUser

#Prueba 1
# Este caso de prueba verifica si un usuario autenticado puede acceder a la página de "Mi cuenta" (índice).
class IndexPageTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_access_index_page_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('cliente:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cliente/index.html')


#Prueba 2
# Este caso de prueba verifica si un usuario puede modificar sus datos correctamente en la página de "Mi cuenta".
class IndexPageTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_modify_client_data(self):
        data = {
            'nombre': 'NuevoNombre',
            'apellido': 'NuevoApellido',
            'email': 'nuevoemail@example.com',
            'telefono': '123456789',
            'fecha_nacimiento': '1990-01-01',
            'contrasena': 'nuevacontrasena',
        }
        response = self.client.post(reverse('cliente:index'), data)
        self.assertEqual(response.status_code, 302)  
        updated_user = CustomUser.objects.get(username='testuser')
        self.assertEqual(updated_user.nombre, 'NuevoNombre')
        self.assertEqual(updated_user.apellido, 'NuevoApellido')



#Prueba 3
# Este caso de prueba verifica si un usuario no autenticado es redirigido correctamente a la página de registro al intentar acceder a la página de "Mi cuenta".
class IndexPageTestCase(TestCase):
    def test_access_index_page_unauthenticated(self):
        response = self.client.get(reverse('cliente:index'))
        self.assertEqual(response.status_code, 302)  # Verifica que se redirija
        self.assertRedirects(response, reverse('core:register'))  # Verifica la redirección correcta
