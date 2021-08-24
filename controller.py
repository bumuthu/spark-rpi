from flask_restful import Resource

class Controller(Resource):

    def __init__(self):
        print('Controller got response...')

    def get(self):        
        detector = Detector()
        count = detector.detect()

        return {"count" : count}, 200