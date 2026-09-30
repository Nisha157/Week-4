from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json


@csrf_exempt
def task_list(request):

    if request.method == "GET":
        tasks = Task.objects.all()

        data = [
            {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "created_at": task.created_at,
            }
            for task in tasks
        ]

        return JsonResponse({
            "status": "success",
            "data": data
        })

    elif request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            name=data["name"],
            description=data["description"],
            status=data.get("status", "Pending")
        )

        return JsonResponse({
            "status": "success",
            "message": "Task created successfully",
            "data": {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status,
                "created_at": task.created_at,
            }
        }, status=201)

    return JsonResponse({
        "status": "error",
        "message": "Method not allowed"
    }, status=405)