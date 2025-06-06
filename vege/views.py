from django.shortcuts import render,redirect
from .models import Recepie

# Create your views here.
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
