import os

def add_one(number):
    return number + 1

def add_two(number):
    return number + 2

def add_three(number):
    return number + 3

def add_four(number):
    return number + 4

def add_five(number):
    return number + 5

def test_env():
    return os.environ.get('ENV', 'development')

"""Modelo de zonas"""
from django.db import models


class Zona(models.Model):
    """Modelo de zonas"""
    class Meta:
        verbose_name_plural = "Zonas"
        verbose_name = "Zona"
        db_table = 'extranet_zona'
        managed = False

    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    fecha_moficacion = models.DateTimeField(auto_now=True, null=True)