from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import base64

app = Flask(__name__)

# Directory to store images
IMAGE_FOLDER = os.path.join('static', 'images')
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    image_data = data['image']
    image_data = image_data.replace('data:image/png;base64,', '')
    image_data = base64.b64decode(image_data)
    image_name = os.path.join(IMAGE_FOLDER, f'image_{len(os.listdir(IMAGE_FOLDER)) + 1}.png')
    
    with open(image_name, 'wb') as f:
        f.write(image_data)
    
    return jsonify({'message': 'Image uploaded successfully'})

@app.route('/gallery')
def gallery():
    images = os.listdir(IMAGE_FOLDER)
    image_urls = [os.path.join('static', 'images', img) for img in images]
    return render_template('gallery.html', images=image_urls)

if __name__ == '__main__':
    app.run(debug=True)
