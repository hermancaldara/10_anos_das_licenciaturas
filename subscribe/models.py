# coding: utf-8

from django.db import models


PEOPLE_CHOICES = (
    ('professor', 'Professor'),
    ('aluno', 'Aluno'),
    ('outro', 'Outro'),
)

POSTER_CHOICES = (
    ('sim', 'Sim'),
    ('nao', 'Não'),
)


class Entry(models.Model):
    name = models.CharField(max_length=100)
    people_type = models.CharField(max_length=100, choices=PEOPLE_CHOICES)
    other_choice = models.CharField(max_length=100, blank=True, null=True) 
    operation_area = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    poster_presentation = models.CharField(max_length=100, choices=POSTER_CHOICES)
    poster_title = models.CharField(max_length=100, blank=True, null=True)
    poster_autors = models.CharField(max_length=100, blank=True, null=True)
    poster_leader = models.CharField(max_length=100, blank=True, null=True)
    poster_institution = models.CharField(max_length=100, blank=True, null=True)
    poster_abstract = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return '%s (%s)' % (self.name, self.cpf)

