# coding: utf-8

from django.db import models


PEOPLE_CHOICES = (
    ('professor', 'Professor'),
    ('aluno', 'Aluno'),
    ('outro', 'Outro'),
)

POSTER_CHOICES = (
    ('nao', 'Não'),
    ('sim', 'Sim'),
)


class Entry(models.Model):
  
    class Meta:
        verbose_name = 'Inscrição'    
        verbose_name_plural = 'Inscrições'
    
    name = models.CharField(max_length=100, verbose_name="Nome")
    people_type = models.CharField(
        max_length=100,
        choices=PEOPLE_CHOICES,
        verbose_name="Status",
        default=None,
    )
    other_choice = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="Outro",
    ) 
    operation_area = models.CharField(
        max_length=100, verbose_name="Área de Atuação"
    )
    institution = models.CharField(max_length=100, verbose_name="Instituição")
    email = models.EmailField(
        max_length=100,
        verbose_name="Email",
        unique=True
    )
    adress = models.CharField(max_length=100, verbose_name="Endereço")
    phone = models.CharField(
        max_length=12)
    mobile = models.CharField(
        max_length=12,)
    cpf = models.CharField(
        max_length=14,
        unique=True,
    )
    rg = models.CharField(max_length=100, verbose_name="RG")
    poster_presentation = models.CharField(
        max_length=100,
        choices=POSTER_CHOICES,
        default='nao',
        verbose_name="Apresentação de Pôsteres",
        help_text="Submissão de pôsteres até dia 27 de maio"
    )
    poster_title = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Título do Trabalho"
    )
    poster_autors = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Autores"
    )
    poster_leader = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Orientador"
    )
    poster_institution = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Instituição"
    )
    poster_abstract = models.TextField(
      blank=True, null=True, verbose_name="Resumo"
    )
    
    def __unicode__(self):
        return '%s - (%s)' % (self.name, self.cpf)

