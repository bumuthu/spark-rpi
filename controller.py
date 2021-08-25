from flask_restful import Resource
from detector import Detector
import json

class Controller(Resource):

    def __init__(self):
        print('Controller got response...')

    def get(self):        
        detector = Detector()
        count = detector.detect()
        img = detector.get_image()

        return json.dumps({"count" : count, "processed_img": img }), 200