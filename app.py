from flask import Flask, render_template, request
import cv2
import numpy as np
from keras.models import load_model
from scipy.spatial import distance
import requests
from io import BytesIO
import base64

app = Flask(__name__)

# Load the ML model
model = load_model('masknet2.h5')
face_model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mask_label = {0: 'MASK', 1: 'NO MASK'}
dist_label = {0: (0, 255, 0), 1: (255, 0, 0)}

MIN_DISTANCE = 230

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the URL input by the user
        image_url = request.form['image_url']
        
        # Send a GET request to fetch the image
        response = requests.get(image_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Get the image data
            image_data = response.content
            
            # Load the image using OpenCV
            nparr = np.frombuffer(image_data, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Convert the image to grayscale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces in the image
            faces = face_model.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            if len(faces) >= 1:
                label = [0 for i in range(len(faces))]
                for i in range(len(faces)-1):
                    for j in range(i+1, len(faces)):
                        dist = distance.euclidean(faces[i][:2],faces[j][:2])
                        if dist < MIN_DISTANCE:
                            label[i] = 1
                            label[j] = 1
                
                new_img = img.copy() # Colored output image
                for i in range(len(faces)):
                    (x, y, w, h) = faces[i]
                    crop = new_img[y:y+h, x:x+w]
                    crop = cv2.resize(crop, (128, 128))
                    crop = np.reshape(crop, [1, 128, 128, 3])/255.0
                    mask_result = model.predict(crop)
                    cv2.putText(new_img, mask_label[mask_result.argmax()], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, dist_label[label[i]], 2)
                    cv2.rectangle(new_img, (x, y), (x+w, y+h), dist_label[label[i]], 1)
                
                # Encode the image data as base64
                _, img_encoded = cv2.imencode('.png', new_img)
                image_base64 = base64.b64encode(img_encoded).decode('utf-8')
                
                # Render the template with the base64 encoded image
                return render_template('index.html', image_base64=image_base64)
            else:
                error_message = "No faces detected"
                return render_template('index.html', error_message=error_message)
        else:
            error_message = f"Error: Unable to fetch image. Status code: {response.status_code}"
            return render_template('index.html', error_message=error_message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
