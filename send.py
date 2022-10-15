import random
import sys
import time

import numpy as np
from requests import Session
import cv2

requests_module = Session()

worker_id = sys.argv[1]

url = 'http://localhost:8020/api/app/frame'

while True:
    print(worker_id, 'Getting image...')
    r1 = requests_module.get(url)
    image = r1.json().get('image')
    id = r1.json().get('id')
    print(worker_id, f'sent: {id}')
    time.sleep(1)
    print(worker_id, 'Sending image...')
    r2 = requests_module.post(url, data={
        'id': id,
        # 'image': jpeg,
        # "stones": [{
        #     "x": random.randint(1, 1000),
        #     "y": random.randint(1, 1000),
        #     "height": random.randint(1, 1000),
        #     "width": random.randint(1, 1000)
        # } for x in range(random.randint(0, 15))]
    })
    print(worker_id, 'sent.')
