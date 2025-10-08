from django.db import models

class Cliente(models.Model): 

    nome = models.CharField(max_length=50)
    conta = models.CharField(max_length=10, unique=True)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00) 
    email = models.EmailField(max_length=50, unique=True) 
    telefone = models.CharField(max_length=15)
    
    def __str__(self):
        return f"Conta {self.conta} - {self.nome}"
