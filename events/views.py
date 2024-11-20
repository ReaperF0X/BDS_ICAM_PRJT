


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, EventForm
from .models import Event, Registration, Discipline
from django.db.models import Q
from .forms import ProfileForm
from .models import User





def home(request):
    query = request.GET.get('q', '')  # Récupère la valeur de la barre de recherche
    discipline_filter = request.GET.get('discipline')  # Récupère la valeur du filtre par discipline

    # Récupère tous les événements
    events = Event.objects.all()

    # Applique la recherche
    if query:
        events = events.filter(
            Q(title__icontains=query) | Q(discipline__name__icontains=query)
        )

    # Applique le filtre par discipline
    if discipline_filter:
        events = events.filter(discipline__id=discipline_filter)

    # Récupère toutes les disciplines pour le filtre
    disciplines = Discipline.objects.all()

    return render(request, 'home.html', {
        'events': events,
        'disciplines': disciplines,
        'query': query,
        'discipline_filter': discipline_filter,
    })



# Inscription utilisateur
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Connexion utilisateur
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(request, 'login.html')

# Déconnexion utilisateur
def user_logout(request):
    logout(request)
    return redirect('home')

# Création d'un événement
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form})

# Modification d'un événement
@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.creator:
        return redirect('home')
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})

# Suppression d'un événement
@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user == event.creator:
        event.delete()
    return redirect('home')

# Inscription à un événement
@login_required
def register_to_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.registrations.count() < event.max_participants:
        Registration.objects.get_or_create(event=event, participant=request.user)
    return redirect('home')

# Liste des participants
@login_required
def view_participants(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participants = event.registrations.all()
    return render(request, 'view_participants.html', {'event': event, 'participants': participants})

# Connexion utilisateur
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Nom d\'utilisateur ou mot de passe incorrect.'})
    return render(request, 'login.html')




@login_required
def view_participants(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Récupère les inscriptions liées à cet événement
    participants = Registration.objects.filter(event=event)
    return render(request, 'view_participants.html', {'event': event, 'participants': participants})


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

#def view_profile(request, user_id):
#    user = get_object_or_404(User, id=user_id)
#    return render(request, 'view_profile.html', {'profile_user': user})

@login_required
def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Récupérer les événements créés par cet utilisateur
    user_events = Event.objects.filter(creator=user)
    
    return render(request, 'view_profile.html', {'profile_user': user, 'user_events': user_events,})
