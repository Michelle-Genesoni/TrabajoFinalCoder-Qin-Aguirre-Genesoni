import random
import string

from django.test import TestCase
from apponline.models import Carteras, Zapatos, Accesorios, Camperas
class CarterasTestCase(TestCase):

    def test_creacion_Carteras(self):
            #Test 1: Comprobar puedo crear una cartera con nombre/codigo conformado por letras random
            lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            print(lista_letras_nombre)
            lista_letras_codigo = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            lista_stock_codigo = [random.choice(str(12) + str(5)) for  _ in range(10)]
            nombre_prueba = "".join(lista_letras_nombre)
            codigo_prueba = "".join(lista_letras_codigo)
            stock_prueba = "".join(lista_stock_codigo)
            print(nombre_prueba)
            print(codigo_prueba)
            print(stock_prueba)
            Carteras_1 = Carteras.objects.create(nombre=nombre_prueba,codigo=codigo_prueba,stock=stock_prueba)

            self.assertIsNotNone(Carteras_1.id)
            self.assertEqual(Carteras_1.nombre, nombre_prueba)
            self.assertEqual(Carteras_1.codigo, codigo_prueba)
            self.assertEqual(Carteras_1.stock, stock_prueba)
            print(Carteras_1.nombre)

    def test_creacion_Zapatos(self):
            #Test 1: Comprobar puedo crear una Zapatos con nombre/codigo conformado por letras random
            lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            print(lista_letras_nombre)
            lista_letras_codigo = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            lista_stock_codigo = [random.choice(str(12) + str(5)) for  _ in range(10)]
            nombre_prueba = "".join(lista_letras_nombre)
            codigo_prueba = "".join(lista_letras_codigo)
            stock_prueba = "".join(lista_stock_codigo)
            print(nombre_prueba)
            print(codigo_prueba)
            print(stock_prueba)
            Zapatos_1 = Zapatos.objects.create(nombre=nombre_prueba,codigo=codigo_prueba,stock=stock_prueba)

            self.assertIsNotNone(Zapatos_1.id)
            self.assertEqual(Zapatos_1.nombre, nombre_prueba)
            self.assertEqual(Zapatos_1.codigo, codigo_prueba)
            self.assertEqual(Zapatos_1.stock, stock_prueba)
            print(Zapatos_1.nombre)

    def test_creacion_Accesorios(self):
            #Test 1: Comprobar puedo crear una cartera con nombre/codigo conformado por letras random
            lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            print(lista_letras_nombre)
            lista_letras_codigo = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            lista_stock_codigo = [random.choice(str(12) + str(5)) for  _ in range(10)]
            nombre_prueba = "".join(lista_letras_nombre)
            codigo_prueba = "".join(lista_letras_codigo)
            stock_prueba = "".join(lista_stock_codigo)
            print(nombre_prueba)
            print(codigo_prueba)
            print(stock_prueba)
            Accesorios_1 = Accesorios.objects.create(nombre=nombre_prueba,codigo=codigo_prueba,stock=stock_prueba)

            self.assertIsNotNone(Accesorios_1.id)
            self.assertEqual(Accesorios_1.nombre, nombre_prueba)
            self.assertEqual(Accesorios_1.codigo, codigo_prueba)
            self.assertEqual(Accesorios_1.stock, stock_prueba)
            print(Accesorios_1.nombre)

    def test_creacion_Camperas(self):
            #Test 1: Comprobar puedo crear una cartera con nombre/codigo conformado por letras random
            lista_letras_nombre = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            print(lista_letras_nombre)
            lista_letras_codigo = [random.choice(string.ascii_letters + string.digits) for  _ in range(20)]
            lista_stock_codigo = [random.choice(str(12) + str(5)) for  _ in range(10)]
            nombre_prueba = "".join(lista_letras_nombre)
            codigo_prueba = "".join(lista_letras_codigo)
            stock_prueba = "".join(lista_stock_codigo)
            print(nombre_prueba)
            print(codigo_prueba)
            print(stock_prueba)
            Camperas_1 = Camperas.objects.create(nombre=nombre_prueba,codigo=codigo_prueba,stock=stock_prueba)

            self.assertIsNotNone(Camperas_1.id)
            self.assertEqual(Camperas_1.nombre, nombre_prueba)
            self.assertEqual(Camperas_1.codigo, codigo_prueba)
            self.assertEqual(Camperas_1.stock, stock_prueba)
            print(Camperas_1.nombre)
