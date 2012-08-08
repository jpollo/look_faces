#
import sys
import os
import Image
import cv


def detectObject(pic_file):
    img = Image.open(pic_file)
    if 900 not in img.size:
        img.thumbnail((900, 900), Image.ANTIALIAS)
        img.save('/tmp/face.jpg', 'JPEG')
    image = cv.LoadImage("/tmp/face.jpg")
    detect(image, img.size)
    #displayObject(image)



def detect(image, size):
    grayscale = cv.CreateImage(size, 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    cascade = cv.Load('haarcascade_frontalface_default.xml')
    faces = cv.HaarDetectObjects(grayscale, cascade, cv.CreateMemStorage())
    if faces:
        print 'Found faces'
        for (x,y,w,h),n in faces:
            cv.Rectangle(image, (x,y), (x+w, y+h), cv.CV_RGB(0,255,0), 2, 8, 0)
            cv.SaveImage( 'face1.jpg', image)
    else:
        print "Faces not detected. Maybe change some parameters to test again."



def displayObject(image):
    cv.NamedWindow("face", 1)
    cv.ShowImage("face", image)
    cv.WaitKey(0)
    cv.DestroyWindow("face")

def main(): 
    # Format & size
    detectObject(sys.argv[1])

if __name__ == "__main__":
    main()

