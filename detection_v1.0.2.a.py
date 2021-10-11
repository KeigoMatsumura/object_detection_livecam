from imageai.Detection import ObjectDetection
import os
import pafy #youtube video capture
import cv2
import ambient
import urllib.request
import datetime


def detection(ambiID, ambiKey, videoURL, img_path):
    #determine the integrity of detection
    min_probability = 30
    
    #get captured time
    now_time = datetime.datetime.now().strftime(':%H-%M-%S:%m%d:%Y')

    exec_path = r'/home/keigo/sub-workspace/object_detection_simplified'

    video_pafy = pafy.new(videoURL)
    video_from_url = video_pafy.getbest().url
    cap = cv2.VideoCapture(video_from_url)
    ret, frame = cap.read()

    if not os.path.exists(img_path):
        os.mkdir(img_path)
    exec_path_neo = os.path.join(exec_path, img_path)
    file_name = img_path + now_time + '.jpg'
    c_name = 'CAP@' + file_name
    d_name = 'DET@' + file_name
    c_path = os.path.join(exec_path_neo, c_name)
    d_path = os.path.join(exec_path_neo, d_name)
    print(c_name, d_name)
    print(c_path, d_path)
    cv2.imwrite(c_path,frame)
    cap.release()
    

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(r'/home/keigo/sub-workspace/object_detection_simplified/models/resnet50_coco_best_v2.1.0.h5')
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=c_path, output_image_path=d_path, minimum_percentage_probability=min_probability)

    person = 0
    vehicle = 0
    bicycle = 0

    for eachObject in detections:
        #print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        person = person + (eachObject["name"]=="person")
        vehicle = vehicle + (eachObject["name"]=="car") + (eachObject["name"]=="bus")+ (eachObject["name"]=="truck")
        bicycle = bicycle + (eachObject["name"]=="bicycle")

    print("person:", person)
    print("vehicle:", vehicle)
    print("bicycle:", bicycle)

    #update ambient data
    am = ambient.Ambient(ambiID, ambiKey)
    r = am.send({'d1': person, 'd2': vehicle, 'd3': bicycle})

def main():
    #Shibuya-Scramble-Square
    detection(42462, "078af68a80f65911", "https://www.youtube.com/watch?v=HpdO5Kq3o7Y", "Shibuya")
    #NeyYork-Times-Square
    detection(42462, "078af68a80f65911", "https://www.youtube.com/watch?v=EHkMjfMw7oU", "Kabukicho")
    #osaka-Dotonbori
    detection(42462, "078af68a80f65911", "https://www.youtube.com/watch?v=Put1j7kemuI", "Dotonbori")
if __name__ == "__main__":
    main()