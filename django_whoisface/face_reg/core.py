import os
import cv2
import time
import face_recognition as fr
from numpy import ndarray
from .db import ReadFaces
import numpy as np
from django.conf import settings


class Face:
    # members = ReadFaces().get_member_conf()

    # member_encoded_faces = [fr.face_encodings(
    #     cv2.imdecode(np.fromfile(os.path.join(settings.BASE_DIR, 'face_reg', item.get('main_pic')), dtype=np.uint8),
    #                  1))[0] for item in members]

    # def get_face(self, camera_index: int):
    #     pass

    # def parse_face(self, face_image: ndarray):
    #     start = time.time()
    #     face_locations = fr.face_locations(face_image)
    #     face_locations: list  # 返回一个列表，列表元素是元组，每个元组包含(top, right, bottom, left)

    #     if not face_locations:
    #         return []

    #     status = 400
    #     persons = []
    #     for face_location in face_locations:

    #         face_image_enc = fr.face_encodings(face_image)[0]

    #         res = fr.compare_faces(self.member_encoded_faces, face_image_enc)
    #         if any(res):
    #             status = 200
    #             person = self.members[res.index(True)]
    #         else:
    #             status = 404
    #             person = '陌生人'

    #         persons.append(person)

    #     end = time.time()
    #     print('speed time is {} 秒'.format(end - start))

    #     return {
    #         'status': status,
    #         'data': {
    #             'persons': persons
    #         },
    #         'time': end - start
    #     }
    pass
