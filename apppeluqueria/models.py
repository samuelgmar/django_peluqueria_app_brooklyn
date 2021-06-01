
from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class cliente(models.Model):
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE,related_name='cliente')
    phone = models.CharField(max_length=17,null=False) 
    direcciones = models.ForeignKey('direccion', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.usuario.username

class trabajador(models.Model):
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE,related_name='trabajador')
    phone = models.CharField(max_length=17,null=False) 
    direcciones = models.ForeignKey('direccion', on_delete=models.SET_NULL, null=True,blank=True)
    imagen = models.ImageField(blank=True, null=True,default='img_avatar.png')

    def __str__(self):
        return self.usuario.username

class jefe(models.Model):
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE,related_name='jefe')
    phone = models.CharField(max_length=17,null=False) 
    direcciones = models.ForeignKey('direccion', on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.usuario.username

class direccion(models.Model):
    perfil = models.ForeignKey('cliente', on_delete=models.SET_NULL, null=True)
    pais_CHOICES = [('Afg','Afganistán'),
('Alb', 'Albania'),
('Ale', 'Alemania'),
('And', 'Andorra'),
('Ang', 'Angola'),
('Ant', 'Antigua y Barbuda'),
('Ara', 'Arabia Saudita'),
('Arg', 'Argelia'),
('Arge', 'Argentina'),
('Arm', 'Armenia'),
('Aus', 'Australia'),
('Aust', 'Austria'),
('Aze', 'Azerbaiyán'),
('Bah', 'Bahamas'),
('Ban', 'Bangladés'),
('Barb', 'Barbados'),
('Bar', 'Baréin'),
('Bel', 'Bélgica'),
('Beli', 'Belice'),
('Ben', 'Benín'),
('Bie', 'Bielorrusia'),
('Bir', 'Birmania'),
('Bol', 'Bolivia'),
('Bos', 'Bosnia y Herzegovina'),
('Bot', 'Botsuana'),
('Bra', 'Brasil'),
('Bru', 'Brunéi'),
('Bul', 'Bulgaria'),
('Bur', 'Burkina Faso'),
('Buru', 'Burundi'),
('But', 'Bután'),
('Cab', 'Cabo Verde'),
('Camb', 'Camboya'),
('Cam', 'Camerún'),
('Can', 'Canadá'),
('Cat', 'Catar'),
('Cha', 'Chad'),
('Chi', 'Chile'),
('Chin', 'China'),
('Chip', 'Chipre'),
('Ciu', 'Ciudad del Vaticano'),
('Col', 'Colombia'),
('Com', 'Comoras'),
('Cor-n', 'Corea del Norte'),
('Cor-s', 'Corea del Sur'),
('Cos-mar', 'Costa de Marfil'),
('Cost', 'Costa Rica'),
('Cro', 'Croacia'),
('Cub', 'Cuba'),
('Din', 'Dinamarca'),
('Dom', 'Dominica'),
('Ecu', 'Ecuador'),
('Egi', 'Egipto'),
('El ', 'El Salvador'),
('Emi', 'Emiratos Árabes Unidos'),
('Eri', 'Eritrea'),
('Esl-ia', 'Eslovaquia'),
('Esl-nia', 'Eslovenia'),
('Esp', 'España'),
('Est-uni', 'Estados Unidos'),
('Est', 'Estonia'),
('Eti', 'Etiopía'),
('Fil', 'Filipinas'),
('Fin', 'Finlandia'),
('Fiy', 'Fiyi'),
('Fra', 'Francia'),
('Gab', 'Gabón'),
('Gam', 'Gambia'),
('Geo', 'Georgia'),
('Gha', 'Ghana'),
('Gra', 'Granada'),
('Gre', 'Grecia'),
('Gua', 'Guatemala'),
('Guy', 'Guyana'),
('Gui', 'Guinea'),
('Gui-ecu', 'Guinea ecuatorial'),
('Gui-bi', 'Guinea-Bisáu'),
('Hai', 'Haití'),
('Hon', 'Honduras'),
('Hun', 'Hungría'),
('Ind', 'India'),
('Ind', 'Indonesia'),
('Ira', 'Irak'),
('Irá', 'Irán'),
('Irl', 'Irlanda'),
('Isl', 'Islandia'),
('Isl', 'Islas Marshall'),
('Isl', 'Islas Salomón'),
('Isr', 'Israel'),
('Ita', 'Italia'),
('Jam', 'Jamaica'),
('Jap', 'Japón'),
('Jor', 'Jordania'),
('Kaz', 'Kazajistán'),
('Ken', 'Kenia'),
('Kir', 'Kirguistán'),
('Kir', 'Kiribati'),
('Kuw', 'Kuwait'),
('Lao', 'Laos'),
('Les', 'Lesoto'),
('Let', 'Letonia'),
('Líb', 'Líbano'),
('Lib', 'Liberia'),
('Lib', 'Libia'),
('Lie', 'Liechtenstein'),
('Lit', 'Lituania'),
('Lux', 'Luxemburgo'),
('Mad', 'Madagascar'),
('Mal', 'Malasia'),
('Mal', 'Malaui'),
('Mal', 'Maldivas'),
('Mal', 'Malí'),
('Mal', 'Malta'),
('Mar', 'Marruecos'),
('Mau', 'Mauricio'),
('Mau', 'Mauritania'),
('Méx', 'México'),
('Mic', 'Micronesia'),
('Mol', 'Moldavia'),
('Món', 'Mónaco'),
('Mon', 'Mongolia'),
('Mon', 'Montenegro'),
('Moz', 'Mozambique'),
('Nam', 'Namibia'),
('Nau', 'Nauru'),
('Nep', 'Nepal'),
('Nic', 'Nicaragua'),
('Níg', 'Níger'),
('Nig', 'Nigeria'),
('Nor', 'Noruega'),
('Nue', 'Nueva Zelanda'),
('Omá', 'Omán'),
('Paí', 'Países Bajos'),
('Pak', 'Pakistán'),
('Pal', 'Palaos'),
('Pan', 'Panamá'),
('Pap', 'Papúa Nueva Guinea'),
('Par', 'Paraguay'),
('Per', 'Perú'),
('Pol', 'Polonia'),
('Por', 'Portugal'),
('Rei', 'Reino Unido'),
('Rep', 'República Centroafricana'),
('Rep', 'República Checa'),
('Rep', 'República de Macedonia'),
('Rep', 'República del Congo'),
('Rep', 'República Democrática del Congo'),
('Rep', 'República Dominicana'),
('Rep', 'República Sudafricana'),
('Rua', 'Ruanda'),
('Rum', 'Rumanía'),
('Rus', 'Rusia'),
('Sam', 'Samoa'),
('San', 'San Cristóbal y Nieves'),
('San', 'San Marino'),
('San', 'San Vicente y las Granadinas'),
('San', 'Santa Lucía'),
('San', 'Santo Tomé y Príncipe'),
('Sen', 'Senegal'),
('Ser', 'Serbia'),
('Sey', 'Seychelles'),
('Sie', 'Sierra Leona'),
('Sin', 'Singapur'),
('Sir', 'Siria'),
('Som', 'Somalia'),
('Sri', 'Sri Lanka'),
('Sua', 'Suazilandia'),
('Sud', 'Sudán'),
('Sud', 'Sudán del Sur'),
('Sue', 'Suecia'),
('Sui', 'Suiza'),
('Sur', 'Surinam'),
('Tai', 'Tailandia'),
('Tan', 'Tanzania'),
('Tay', 'Tayikistán'),
('Tim', 'Timor Oriental'),
('Tog', 'Togo'),
('Ton', 'Tonga'),
('Tri', 'Trinidad y Tobago'),
('Tún', 'Túnez'),
('Tur', 'Turkmenistán'),
('Tur', 'Turquía'),
('Tuv', 'Tuvalu'),
('Ucr', 'Ucrania'),
('Uga', 'Uganda'),
('Uru', 'Uruguay'),
('Uzb', 'Uzbekistán'),
('Van', 'Vanuatu'),
('Ven', 'Venezuela'),
('Vie', 'Vietnam'),
('Yem', 'Yemen'),
('Yib', 'Yibuti'),
('Zam', 'Zambia'),
('Zim', 'Zimbabue')]
    pais = models.CharField(max_length=40,choices=pais_CHOICES,null=False)
    nombre_completo = models.CharField(max_length=40,help_text='Introduca su nombre y apellidos',null=False)
    direccion1 = models.CharField(max_length=40,help_text='Línea 1 de la dirección',null=False)
    direccion2 = models.CharField(max_length=40,help_text='Línea 2 de la dirección',null=True)
    ciudad = models.CharField(max_length=40,help_text='Introduca su ciudad',null=False)
    provincia = models.CharField(max_length=40,help_text='Introduca su provincia/región',null=False)
    codigo_postal = models.CharField(max_length=7,help_text='Introduca su codigo postal',null=False)
    notas = models.TextField(max_length=500,help_text='Añadir instrucciones de entrega',null=True)

    
    def __str__(self):
        return 'Dirección de '+self.perfil.usuario.username + ' (' + str(self.id) + ')'

class galeria(models.Model):
    nombre_foto = models.CharField(max_length=100)
    imagen = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nombre_foto

class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.nombre_categoria

class servicio(models.Model):
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    categoria = models.ForeignKey('categoria', on_delete=models.SET_NULL, null=True)
    duracion = models.IntegerField()

    def __str__(self):
        return self.nombre_servicio

class reserva(models.Model):
    servicio = models.ForeignKey('servicio', on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey('cliente', on_delete=models.SET_NULL, null=True)
    fechaTrabajador = models.OneToOneField('fechaTrabajador', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.servicio)+' '+str(self.cliente)+' '+str(self.fechaTrabajador)

class hora(models.Model):
    hora = models.TimeField(null=False)

    class Meta:
        ordering = ['hora']

    def __str__(self):
        return str(self.hora)

class fecha(models.Model):   
    dia = models.DateField(null=True)
    hora = models.ForeignKey('hora',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.dia)+' '+str(self.hora)

class fechaTrabajador(models.Model):
    fecha = models.ForeignKey('fecha', on_delete=models.SET_NULL, null=True)
    peluquero = models.ForeignKey('trabajador', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.peluquero)+' '+str(self.fecha)