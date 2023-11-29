import cv2

imagem1 = cv2.imread('monga(2).jpg')
imagem2 = cv2.imread('monga(4).jpg')

imagem2 = cv2.resize(imagem2, (imagem1.shape[1], imagem1.shape[0]))

alfa = 0.01  

while alfa <= 1.0:
    imagem_final = cv2.addWeighted(imagem1, alfa, imagem2, 1 - alfa, 0)
    cv2.imshow('Imagem Final', imagem_final)
    cv2.waitKey(100) 
    alfa += 0.01


cv2.destroyAllWindows()
