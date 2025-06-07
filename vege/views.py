from django.shortcuts import render,redirect
from .models import Recepie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

# Create your views here.
@login_required(login_url='/login/')
def recepies(request):
 if request.method == 'POST':
    data = request.POST
    receipe_name = data.get('receipe_name')
    receipe_description = data.get('receipe_description')
    receipe_image = request.FILES.get('receipe_image')

    print(f"Recipe Name: {receipe_name}")
    print(f"Recipe Description: {receipe_description}")
    print(f"Recipe Image: {receipe_image}") 

    Recepie.objects.create(
        name=receipe_name,
        description=receipe_description,
        image=receipe_image
    )

    return redirect('recepies')
 
 queryset = Recepie.objects.all()


 search_query = request.GET.get('search', '')
 if search_query:
        queryset = queryset.filter(name__icontains=search_query)


 context = {
    'recepies': queryset
 } 
 return render(request, 'recepies.html', context)

def update_recepie(request, id):
   queryset = Recepie.objects.get(id=id)

   if request.method == 'POST':
         data = request.POST
         receipe_name = data.get('receipe_name')
         receipe_description = data.get('receipe_description')
         receipe_image = request.FILES.get('receipe_image')
   
         print(f"Updating Recipe ID: {id}")
         print(f"New Recipe Name: {receipe_name}")
         print(f"New Recipe Description: {receipe_description}")
         print(f"New Recipe Image: {receipe_image}")
   
         queryset.name = receipe_name
         queryset.description = receipe_description
         if receipe_image:
            queryset.image = receipe_image
         queryset.save()
   
         return redirect('recepies')

   return render(request, 'update_recepies.html', {'recepie': queryset})

def delete_recepie(request, id):
    print(f"Deleting recipe with ID: {id}")
    queryset = Recepie.objects.get(id=id)
    queryset.delete()

    return redirect('recepies')

def login_page(request):
      if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
         return render(request, 'login.html', {'error': 'Username does not exist.'})

      
        user = authenticate(username=username, password=password)

        if user is None:
          return render(request, 'login.html', {'error': 'Invalid credentials.'})
        else:
         login(request, user)
         return redirect('/recepies/')

      return render(request, 'login.html')

def logout_page(request):
        logout(request)
        return redirect('/login/')

    

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (first_name and last_name and username and password):
            return render(request, 'register.html', {'error': 'All fields are required.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})


        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return render(request, 'register.html', {'success': 'Username registered.'})

        # return redirect('login')

    return render(request, 'register.html')