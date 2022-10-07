import cv2

# Membaca gambar
img = cv2.imread('Photos/cat.jpg')

# Menampilkan gambar
cv2.imshow('kucing', img)

# Menyimpan gambar
cv2.imwrite('save_kucing.jpg', img)

# Menunda windows terdestroy
cv2.waitKey(0)
# Mendestroy windows
cv2.destroyAllWindows()
