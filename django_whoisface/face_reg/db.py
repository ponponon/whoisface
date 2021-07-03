import os
import json
from shutil import copyfile
import cv2
from prettyprinter import pprint


class ReadFaces:
    CONF_FILE_NAME = 'test.json'

    CONF_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')

    @classmethod
    def loadconf(cls) -> dict:
        """
        加载配置文件，配置文件是一个json文件
        配置文件的格式如下所示:
        {
          "version": "0.1",
          "project_name": "face_recognition",
          "members": [
            {
              "nid": 1,
              "name": "jike",
              "main_pic": "models/jike/main.jpg",
              "more_pic": null
            },
            {
              "nid": 2,
              "name": "joe",
              "main_pic": "models/joe/main.jpg",
              "more_pic": null
            }
          ]
        }

        :return: 返回反序列化之后的data
        """
        filename = os.path.join(cls.CONF_FILE_PATH, cls.CONF_FILE_NAME)

        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    @classmethod
    def get_member_conf(cls) -> list:
        """
        从配置信息中获取所有成员信息
        格式如下所示:
        [
            {
              "nid": 1,
              "name": "jike",
              "main_pic": "models/jike/main.jpg",
              "more_pic": null
            },
            {
              "nid": 2,
              "name": "joe",
              "main_pic": "models/joe/main.jpg",
              "more_pic": null
            }
          ]
        :return: 返回一个列表，包含所有成员信息
        """
        data = cls.loadconf()
        members = data.get('members')
        return members
