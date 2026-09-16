from django.db import models

# Create your models here.

class Livro(models.Model):
    TIPO_ACERVO_CHOICES = (
        ('Fisico', 'Físico'),
        ('Digital', 'Digital'),
    )
    CATEGORIA_CHOICES = (
        ('000', 'Generalidades e Informação'),
        ('100', 'Filosofia e Psicologia'),
        ('200', 'Religião e Teologia'),
        ('300', 'Ciências Sociais e Direito'),
        ('400', 'Linguística e Idiomas'),
        ('500', 'Ciências Puras'),
        ('600', 'Ciências Aplicadas'),
        ('700', 'Artes e Recreação'),
        ('800', 'Literatura'),
        ('900', 'História e Geografia'),
    )
    
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    tipo_acervo = models.CharField(max_length=10, choices=TIPO_ACERVO_CHOICES, default='Fisico')
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES, default='000')

    def __str__(self):
        return self.titulo