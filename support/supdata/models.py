from django.db import models
from django.utils import timezone



# Create your models here.
class data(models.Model):
    #datos usuario
    fecha = models.DateTimeField(default=timezone.now)
    planta = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    activofijo = models.IntegerField()
    #datos tecnicos
    hostname = models.CharField(max_length=100)
    tipodeequipo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serialnumber = models.CharField(max_length=100)
    ipaddress = models.GenericIPAddressField()
    procesador = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    hdd = models.CharField(max_length=100)

    #agentes 
    epc = models.BooleanField(default=False)
    tenable = models.BooleanField(default=False)
    sophos = models.BooleanField(default=False)
    borrartemporales = models.BooleanField(default=False)
    encriptacionhdd = models.BooleanField(default=False)
    updates = models.BooleanField(default=False)
    #datosmtto
    limpinterna = models.BooleanField(default=False)
    limpexterna = models.BooleanField(default=False)
    limpteclado = models.BooleanField(default=False)
    limpram = models.BooleanField(default=False)
    limpventilador = models.BooleanField(default=False)
    limppasta = models.BooleanField(default=False)
    aplicacionpasta = models.BooleanField(default=False)
    limpiezadisipador = models.BooleanField(default=False)

    imgantes  = models.ImageField(upload_to='imagenesantes/')
    imgdespues = models.ImageField(upload_to='imagenesdespues/')

    tempcpu = models.CharField(max_length=100)
    imgtemp = models.ImageField(upload_to='tempcpu/')

   
    imgagent = models.ImageField(upload_to='tempcpu/')

    nombretech =  models.CharField(max_length=100)
    empresa =  models.CharField(max_length=100, default="Cissa, Intelred etc...") 
    comentarios = models.TextField(max_length=300)
    firma = models.ImageField(upload_to='firmas/', blank=True, null=True)




    def __str__(self):
        return self.hostname
    
   
