from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to the Task Management API, "
    "please visit /api/tasks/ to take a look at what Gokul has done!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
