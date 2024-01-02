import cv2

# Load an image
def get_image(path):
  # Read the image
  img = cv2.imread(path, 0)

  # resize the image 
  # img = cv2.resize(img, (400, 400))
  img = cv2.resize(img, (0, 0), fx=.5, fy=.5) 

  # Rotate image
  cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
  return img

cv2.imshow('image', get_image('./assets/Oladapo AYODEJI.JPG'))
cv2.waitKey(0)
cv2.destroyAllWindows()

