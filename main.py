import json
from os.path import abspath
from ibm_watson import VisualRecognitionV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('TeQ9kVngJNw2JuJAvzhxZkac6xE4ILBd5QeLWjsRotVR')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)

service = VisualRecognitionV3(
    '2018-03-19',
    authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')

for i in range(1,8):
    with open('/Users/liaoyuexiang/Desktop/tests/image'+str(i)+'.png', 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file=images_file,
            threshold='0.6',
            owners=["me"]).get_result()
        print(classes['images'][0]['classifiers'][0]['classes'][0]['class'])
