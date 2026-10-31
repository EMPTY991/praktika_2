import cv2

# 1. Pildi laadimine
img = cv2.imread('imagetest.jpg')

if img is None:
    print("Pilti ei leitud.")
else:
    # 2. Teisendamine halltoonidesse
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Pildi kuvamine
    cv2.imshow('Originaal', img) # Kuvame originaalpildi
    cv2.imshow('Halltoonid', gray_img) # Kuvame halltoonides pildi

    # Oota klahvivajutust ja sulgeb aknad
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 4. Pildi salvestamine
    cv2.imwrite('hall_pilt.jpg', gray_img)


