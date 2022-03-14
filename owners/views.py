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
        return JsonResponse({'Message' : 'Success'}, status=201)
    
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
        