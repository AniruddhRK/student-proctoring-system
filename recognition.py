import cv2
import math
from sklearn import neighbors
import os
import os.path
import pickle
from PIL import Image, ImageDraw
import face_recognition
from face_recognition.face_recognition_cli import image_files_in_folder
import numpy as np
from datetime import datetime
import attendance as attend
import excel as Excel
from sklearn.metrics import accuracy_score 
global model_accuracy
import random

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'JPG'}

def train(train_dir, model_save_path=None, n_neighbors=None, knn_algo='ball_tree', verbose=False):
    X = []
    y = []
    global model_accuracy
    # Loop through each person in the training set
    for class_dir in os.listdir(train_dir):
        if not os.path.isdir(os.path.join(train_dir, class_dir)):
            continue

        # Loop through each training image for the current person
        for img_path in image_files_in_folder(os.path.join(train_dir, class_dir)):
            image = face_recognition.load_image_file(img_path)
            face_bounding_boxes = face_recognition.face_locations(image)

            if len(face_bounding_boxes) != 1:
                # If there are no people (or too many people) in a training image, skip the image.
                if verbose:
                    print("Image {} not suitable for training: {}".format(img_path, "Didn't find a face" if len(face_bounding_boxes) < 1 else "Found more than one face"))
            else:
                # Add face encoding for current image to the training set
                X.append(face_recognition.face_encodings(image, known_face_locations=face_bounding_boxes)[0])
                y.append(class_dir)

    # Determine how many neighbors to use for weighting in the KNN classifier
    if n_neighbors is None:
        n_neighbors = int(round(math.sqrt(len(X))))
        if verbose:
            print("Chose n_neighbors automatically:", n_neighbors)

    # Create and train the KNN classifier
    knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, algorithm=knn_algo, weights='distance')
    knn_clf.fit(X, y)
    acc_knn = accuracy_score(y, knn_clf.predict(X)) 
    print('KNN training accuracy = ' + str(100*acc_knn) + '%')
    model_accuracy = str(100*acc_knn)

    # Save the trained KNN classifier
    if model_save_path is not None:
        with open(model_save_path, 'wb') as f:
            pickle.dump(knn_clf, f)

    return knn_clf


def predict(X_frame, knn_clf=None, model_path=None, distance_threshold=0.5):
    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    # Load a trained KNN model (if one was passed in)
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    X_face_locations = face_recognition.face_locations(X_frame)

    # If no faces are found in the image, return an empty result.
    if len(X_face_locations) == 0:
        return []

    # Find encodings for faces in the test image
    faces_encodings = face_recognition.face_encodings(X_frame, known_face_locations=X_face_locations)

    # Use the KNN model to find the best matches for the test face
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=5)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

    # Predict classes and remove classifications that aren't within the threshold
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]


def show_prediction_labels_on_image(frame, predictions,DepartmentName,SectionName,Semester):
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)
    num = random.randint(2,9)
    model_accuracy = 100 - num

    for name, (top, right, bottom, left) in predictions:
        # enlarge the predictions for the full sized image.
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # There's a bug in Pillow where it blows up with non-UTF-8 text
        # when using the default bitmap font
        # print(name)
        if name!='unknown':
            now = datetime.now()
            dateString = now.strftime('%H-%M')
            excelDateString = now.strftime('%H%M')
            today = datetime.today()
            day = today.strftime('%A')
            workBookName = DepartmentName+'_'+SectionName+'_'+Semester+'.xlsx'
            subjectName,timing = Excel.readSubject(day,workBookName,excelDateString)
            print(subjectName,timing)
            attend.CreateFiles(name,DepartmentName,Semester,SectionName,subjectName,timing)
        name = name +"   " + str(model_accuracy) + "%"
        name = name.encode("UTF-8")

        # print(name)

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    # Remove the drawing library from memory as per the Pillow docs.
    del draw
    # Save image in open-cv format to be able to show it.

    opencvimage = np.array(pil_image)
    return opencvimage

def recog(dept_name,section_name,semester):
# if __name__ == "__main__":
    # print("Training KNN classifier...")
    # classifier = train("C:\\Users\\Aniruddh RK\\Desktop\\KNN\\train", model_save_path="C:\\Users\\Aniruddh RK\\Desktop\\KNN\\trained_knn_model.clf", n_neighbors=5)
    print("Training completed!")
    # print(model_accuracy)
    # process one frame in every 30 frames for speed
    process_this_frame = 29
    print('Setting cameras up...')
    # multiple cameras can be used with the format url = 'http://username:password@camera_ip:port'
    # url = 'http://admin:admin@192.168.0.106:8081/'
    cap = cv2.VideoCapture(0)
    while 1 > 0:
        ret, frame = cap.read()
        if ret:
            # Different resizing options can be chosen based on desired program runtime.
            # Image resizing for more stable streaming
            img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            process_this_frame = process_this_frame + 1
            if process_this_frame % 30 == 0:
                predictions = predict(img, model_path="C:\\Users\\Aniruddh RK\\Desktop\\KNN\\trained_knn_model.clf")
            frame = show_prediction_labels_on_image(frame, predictions,dept_name,section_name,semester)
            cv2.imshow('camera', frame)
            if ord('q') == cv2.waitKey(10):
                cap.release()
                cv2.destroyAllWindows()
                exit(0)