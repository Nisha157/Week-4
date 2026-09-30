from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json


@csrf_exempt
def task_api(request):

    if request.method == "GET":
        tasks = Task.objects.all().values(
            "id",
            "name",
            "description",
            "status",
            "created_at"
        )

        return JsonResponse({
            "status": "success",
            "data": list(tasks)
        })


    elif request.method == "POST":
        data = json.loads(request.body)

        task = Task.objects.create(
            name=data.get("name"),
            description=data.get("description", ""),
            status=data.get("status", "Pending")
        )

        return JsonResponse({
            "status": "success",
            "message": "Task created successfully",
            "data": {
                "id": task.id,
                "name": task.name,
                "description": task.description,
                "status": task.status
            }
        })


    elif request.method == "PUT":
        data = json.loads(request.body)
        task_id = data.get("id")

        try:
            task = Task.objects.get(id=task_id)

            task.name = data.get("name", task.name)
            task.description = data.get(
                "description",
                task.description
            )
            task.status = data.get(
                "status",
                task.status
            )

            task.save()

            return JsonResponse({
                "status": "success",
                "message": "Task updated successfully"
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Task not found"
            }, status=404)


    elif request.method == "DELETE":
        data = json.loads(request.body)
        task_id = data.get("id")

        try:
            task = Task.objects.get(id=task_id)
            task.delete()

            return JsonResponse({
                "status": "success",
                "message": "Task deleted successfully"
            })

        except Task.DoesNotExist:
            return JsonResponse({
                "status": "error",
                "message": "Task not found"
            }, status=404)


    return JsonResponse({
        "status": "error",
        "message": "Method not allowed"
    }, status=405)