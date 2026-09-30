from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def task_api(request):

    if request.method == "GET":
        return JsonResponse({
            "method": "GET",
            "message": "Get tasks"
        })

    elif request.method == "POST":
        data = json.loads(request.body)

        return JsonResponse({
            "method": "POST",
            "message": "Task created",
            "data": data
        })

    elif request.method == "PUT":
        data = json.loads(request.body)

        return JsonResponse({
            "method": "PUT",
            "message": "Task updated",
            "data": data
        })

    elif request.method == "DELETE":
        return JsonResponse({
            "method": "DELETE",
            "message": "Task deleted"
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)


def api_test_page(request):
    return render(request, "tasks/api-test.html")