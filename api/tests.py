from django.test import TestCase

from .models import Curso
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User

class CursoTestCase(TestCase):
    """Esta clase define la testsuite para el Curso."""

    def setUp(self):
        """Definición de variables generales."""
        self.sigla = "ICF121"
        self.nombre="Introducción a la Ingeniería Civil Informática"
        self.creditos=6
        self.curso = Curso(sigla=self.sigla,nombre=self.nombre,creditos=self.creditos)

    def test_creacion_de_curso(self):
        """Test de creación de un curso"""
        old_count = Curso.objects.count()
        self.curso.save()
        new_count = Curso.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Esta clase define la testsuite para la API REST."""
    def setUp(self):
        """Definición de variables generales"""
        self.user=User.objects.create_superuser('servidor', 'api@test.com', "Secret.123")
        c = Client()
        response = c.post('/api/login/', {'username': 'servidor', 'password': 'Secret.123'})
        self.token = response.json()["token"]
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        curso_data = {'sigla': 'ICF121','nombre':'Introducción a la Ingeniería Civil Informática', 'creditos':6}
        self.response_setup = self.client.post(
            reverse('create'),
            curso_data,
            format="json")

    def test_api_creacion_de_cursos(self):
        """Test creación de curso a través de la API."""
        self.assertEqual(self.response_setup.status_code, status.HTTP_201_CREATED)

    def test_api_obtener_curso(self):
        """Test de obtención de curso a través de la API."""
        curso = Curso.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': curso.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, curso)

    def test_api_actualizar_curso(self):
        """Test de actualización de curso a través de la API."""
        curso = Curso.objects.get()
        actualizacion_curso = {'nombre': 'Introduccion a la Ingenieria Civil Informatica'}
        res = self.client.patch(
            reverse('details', kwargs={'pk': curso.id}),
            actualizacion_curso, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_borrar_curso(self):
        """Test borrado de curso a través de la API."""
        curso = Curso.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': curso.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)