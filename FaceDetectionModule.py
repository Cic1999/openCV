"""
Face Detection Module
By: Computer Vision Zone
Website: https://www.computervision.zone/
"""

import cv2
import mediapipe as mp
import cvzone


class FaceDetector:
    """
    Find faces in realtime using the light weight model provided in the mediapipe
    library.
    """

    def __init__(self, minDetectionCon=0.5,model_selection=0):
        """
        :param minDetectionCon: Minimum Detection Confidence Threshold
        """

        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon,model_selection)

    def findFaces(self, img, draw=True):
        """
        Find faces in an image and return the bbox info
        :param img: Image to find the faces in.
        :param draw: Flag to draw the output on the image.
        :return: Image with or without drawings.
                 Bounding Box list.
        """

        heartimg = cv2.imread('./image/heart.jpg',cv2.IMREAD_UNCHANGED)
        heartimg = cv2.resize(heartimg, (0,0),None,1,1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                #print(detection)
                bboxC = detection.location_data.relative_bounding_box
                point = detection.location_data.relative_keypoints[0]
                ih, iw, ic = img.shape
                ah ,aw, ac = heartimg.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)
                print(point)
                px = int(point.x * iw)
                py = int(point.y * ih) 
                bboxInfo = {"id": id, "bbox": bbox, "score": detection.score, "center": (px, py)}
                bboxs.append(bboxInfo)
                if draw:
                    img = cv2.rectangle(img, bbox, (155, 70, 135), 2)
                    #cv2.circle(img,(px,py),2,(0,255,255),2,-1)
                    cv2.circle(img,(px,py),10,(0,255,255),2,-1)
                    cv2.putText(img, f'{int(detection.score[0] * 10000)/100}%',
                                (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                                2, (0, 0, 255), 2)
                    img = cvzone.overlayPNG(img,heartimg,[px-15,py-15])
        return img, bboxs


def main():
    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)

        if bboxs:
            # bboxInfo - "id","bbox","score","center"
            center = bboxs[0]["center"]
            #cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break






if __name__ == "__main__":
    main()