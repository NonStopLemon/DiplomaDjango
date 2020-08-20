from .models import Fingers
from django.shortcuts import render
from .points import checkFinger
from .toTuple import toTuple
from .matches import matchingPoint
from django.http import HttpResponse
from django.core.files.storage import default_storage


def upload(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        file_name = default_storage.save(file.name, file)
        d = checkFinger(default_storage.open(file_name))
        f = Fingers(hash_finger=d.decode('utf-8'))
        f.save()
        default_storage.delete(file_name)

        return HttpResponse(f.hash_finger)

    return render(request, 'upload.html')


def comparison(request):
    if request.method == 'POST':
        r = Fingers.objects.get(
            user_id=request.POST['user_id'])

        r = r.hash_finger
        toTuple(bytes(r, encoding='utf8'))
        file = request.FILES['myfile']
        file_name = default_storage.save(file.name, file)
        v = checkFinger(default_storage.open(file_name))

        result = matchingPoint(toTuple(r), toTuple(v))
        default_storage.delete(file_name)
        return HttpResponse((result[0]/result[1])*100)
    return render(request, 'comparison.html')
