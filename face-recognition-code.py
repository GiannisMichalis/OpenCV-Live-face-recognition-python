import cv2
import numpy as np
import os
from tkinter import *

root = Tk()
root.title("Face Recognition with OpenCV")
root.configure(background="#4A4A70")
root.geometry("2023x2023")

Label1 = Label(root, text="Welcome to Face Recogntition", bg='#4A4A70', fg="#FFFFF8", font='Times 23')
Label1.pack(pady=20, padx=100, anchor=W)
Label2 = Label(root, text="Let's get started!!!", font="Times 17", bg="#4A4A70", fg="#FFFFF8")
Label2.pack(pady=40, padx=30, anchor=W)



def start():
    subjects = ["", "Basilis Swkos", "Xristina Gewrgiou", "Giannis Michalis", "Stratis Siwros"]

    def detect_face(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('opencv-files\\lbpcascade_frontalface.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
        if (len(faces)) == 0:
            return None, None
        (x, y, w, h) = faces[0]
        return gray[y:y+w, x:x+h], faces[0]

    def prepare_training_data(data_folder_path):
        dirs = os.listdir(data_folder_path)
        faces = []
        labels = []
        for dir_name in dirs:
            if not dir_name.startswith("s"):
                continue
            label = int(dir_name.replace('s', ''))
            subject_dir_path = data_folder_path + "/" + dir_name
            subject_images_names = os.listdir(subject_dir_path)
            for image_name in subject_images_names:
                if image_name.startswith('.'):
                    continue
                image_path = subject_dir_path + "/" + image_name
                image = cv2.imread(image_path)
                cv2.imshow("Training on images...", image)
                cv2.waitKey(100)
                face, rect = detect_face(image)
                if face is not None:
                    faces.append(face)
                    labels.append(label)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        return faces, labels

    print("Preparing data...")
    faces, labels = prepare_training_data("training-data")
    print("Data prepared")
    print("Total faces: ", (len(faces)))
    print("Total labels: ", (len(labels)))

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(labels))

    def draw_rectangle_and_text(img, rect, text, x, y):
        (x, y, w, h) = rect
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    def predict(test_img):
        if test_img is None:
            return
        img = test_img.copy()
        face, rect = detect_face(img)
        label_text = "Unknown"
        if face is not None:
            label, confidence = face_recognizer.predict(face)
            if confidence > 50:
                label_text = subjects[label]
            else:
                label_text = "Unknown"
            draw_rectangle_and_text(img, rect, label_text, rect[0], rect[1]-5)
        return img
    def myCamera():
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame = predict(frame)
            cv2.imshow("Recognizing Face", frame)
            if cv2.waitKey(1) == ord('x'):
                break
        cap.release()
        cv2.destroyAllWindows()
    myCamera()

start_button= Button(root, text="Click Here to Start",font="Times 27",command=start )
start_button.pack(pady=1, padx=30, anchor=W)
root.mainloop()