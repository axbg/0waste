import numpy as np
from PIL import Image

def get_color_by_type(waste_type):
    if(waste_type == "bag"):
        #bag - orange
        return (0, 165, 255)
    elif(waste_type == "bottle"):
        #bottle - red
        return (0, 0, 255)
    elif(waste_type == "cap"):
        #cap - blue
        return (255, 0, 0)
    elif(waste_type == "rope"):
        #rope - green
        return (50, 205, 50)
    else:
        #waste - yellow
        return (0, 255, 255)
            
def get_credentials():
    return ["849576898441", "IOD3355942584437440512"]

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def callVision(content):
    prediction_client = automl_v1beta1.PredictionServiceClient()
    [project_id, model_id] = get_credentials()
    name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
    payload = {'image': {'image_bytes': content }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    return request

def splashImage(img):
    content = img.read()

    image = Image.open(io.BytesIO(content))
    width, height = image.size
    
    processed_image = np.asarray(image)[:,:,::-1].copy()
    greyscale_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
    greyscale_image = cv2.cvtColor(greyscale_image, cv2.COLOR_GRAY2RGB)
    greyscale_image = increase_brightness(greyscale_image, 100)

    annotations = callVision(content)
    ct = 0
    for mark in annotations.payload:
        ct = ct + 1
        [upper, lower] = mark.image_object_detection.bounding_box.normalized_vertices
        start_point = (int(width * upper.x), int(height * upper.y))
        end_point = (int(width * lower.x), int(height * lower.y))
        color = get_color_by_type(mark.display_name)
        thickness = 10
        colored_cut = processed_image[int(height * upper.y):int(height * lower.y),  int(width * upper.x):int(width * lower.x)]
        greyscale_image[int(height * upper.y):int(height * lower.y),  int(width * upper.x):int(width * lower.x)] = colored_cut
        greyscale_image = cv2.rectangle(greyscale_image, start_point, end_point, color, thickness)

    retval, buffer = cv2.imencode('.jpg', greyscale_image)
    b64img = base64.b64encode(buffer)
    return [b64img, ct]
  