import cv2
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse
from django.conf import settings
import os
import io
import json
import base64
from PIL import Image
import numpy
from face_reg.core import Face
from numpy import ndarray


def index(request: WSGIRequest):
    return render(request, 'index.html', locals())


def face(request: WSGIRequest):
    if request.method == 'POST':
        img_path = os.path.join(settings.BASE_DIR, 'static', 'img')

        msg = json.loads(request.body.decode('utf-8'))
        img_base64_str = msg.get('img')[len('data:image/jpg:base64,'):]
        img_data = base64.b64decode(img_base64_str)

        with open(os.path.join(img_path, '123.png'), 'wb') as f:
            f.write(img_data)

        image = io.BytesIO(img_data)
        img = numpy.array(Image.open(image))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        img: ndarray

        return JsonResponse(Face().parse_face(img))
    else:
        return JsonResponse({
            'status': 400,
            'message': None
        })
