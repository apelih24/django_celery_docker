import json
from django.shortcuts import render
from celery.result import AsyncResult
from django.http import HttpResponse
from polls.forms import GenerateRandomUserForm
from polls.tasks import create_random_user_accounts, get_for_django
from .models import IcoList


def generate_random_user(request):
    if request.method == 'POST':
        form = GenerateRandomUserForm(request.POST)
        if form.is_valid():
            total_user = form.cleaned_data.get('total_user')
            task = create_random_user_accounts.delay(total_user)
            return HttpResponse(json.dumps({'task_id': task.id}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'task_id': None}), content_type='application/json')
    else:
        form = GenerateRandomUserForm
    return render(request, 'polls/index.html', {'form': form})


def get_task_info(request):
    task_id = request.GET.get('task_id', None)
    if task_id is not None:
        task = AsyncResult(task_id)
        data = {
            'state': task.state,
            'result': task.result,
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse('No job id given.')


def get_ico_list(request):
    data = IcoList.objects.all()
    return render(request, 'polls/ico-list.html', {'data': data})
