import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,50)
    videocaptureobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videocaptureobject.read()
        imagename="img"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        start_time=time.time
        result=False
    return imagename
    print("SNAPSHOT TAKEN!!")

    videocaptureobject.release()
    cv2.destoryAllWindows()

def upload_file(imagename):
    access_token="sl.BFXjLi50fisOBlxgv2FRjEe2_SdPFHQNuhuEw7pDgzblM7aQyo8Y5yuoxlVDvh7zgwHXFbZStOaIfUt60G5g08t0d6z1DPDPjJMjvstYsfsEWHV2Ttc9hRCx_Iiupzx0ZLgWvmmwF7av"
    file=imagename
    file_from=file
    file_to="/saachee/"+(imagename)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("FILE UPLOADED")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()
