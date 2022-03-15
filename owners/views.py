import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        try : 
            data = json.loads(request.body)
            Owner.objects.create(
                name = data['name'],
                email = data['email'],
                age = data['age']
            )
        except KeyError :
            return JsonResponse({'Message' : 'Key error'}, status=400)
        return JsonResponse({'Message' : 'Success'}, status=200)
    
    def get(self, request):
        owners = Owner.objects.all()
        results = []
        
        for owner in owners :
            dogs = owner.dog_set.all()
            results_dogs = []
            
            for dog in dogs :
                results_dogs.append(
                    {
                        'name' : dog.name,
                        'age' : dog.age,
                    }
                )
            results.append(
                {
                    'name' : owner.name,
                    'email' : owner.email,
                    'age' : owner.age,
                    'dogs' : results_dogs
                }
            )
        return JsonResponse({'results' : results}, status = 200)    
                
    
    
    
    
class DogView(View):
    def post(self, request):
        try :
            data = json.loads(request.body)
            Dog.objects.create(
                owner = Owner.objects.get(name = data['owner']),
                name = data['name'],
                age = data['age']
            )
        except KeyError :
            return JsonResponse({'Message' : 'Key Error'}, status = 400)
        return JsonResponse({'Message' : 'Success'}, status = 201)
    
    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        
        for dog in dogs :
            results.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner_name' : dog.owner.name,
                }
            )
        return JsonResponse({'results' : results}, status=200)


