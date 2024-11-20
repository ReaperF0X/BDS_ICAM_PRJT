from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle utilisateur personnalisé
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=191)
    is_active = models.BooleanField(default=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    def __str__(self):
        return self.username


class Discipline(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=191)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)  # Relier une discipline
    date = models.DateField()
    time = models.TimeField()
    max_participants = models.PositiveIntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)  # Description facultative
    illustration = models.ImageField(upload_to='event_illustrations/', blank=True, null=True)
    def __str__(self):
        return self.title

# Modèle pour les inscriptions aux événements
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)




    

   

    
