from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

# Tee ennustus
results = model("näidispilt2.jpg") #https://www.teenvogue.com/story/nokia-cell-phones-android-2017
annotated_frame = results[0].plot()

# 1. Loo aken ja määra, et selle suurust saab muuta
cv2.namedWindow("YOLO Tuvastus", cv2.WINDOW_NORMAL)

# 2. Määra akna suurus (laius, kõrgus pikslites - nt 800x600)
cv2.resizeWindow("YOLO Tuvastus", 800, 600)

# 3. Näita pilti samas aknas
cv2.imshow("YOLO Tuvastus", annotated_frame)

# Oota klahvivajutust
cv2.waitKey(0)
cv2.destroyAllWindows()