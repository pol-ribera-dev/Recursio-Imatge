import cv2
cap = cv2.VideoCapture(0)
png = 'imatge.png'
img = cv2.imread(png)

height, width = img.shape[:2]

video = cv2.VideoWriter('db0.wmv',cv2.VideoWriter_fourcc(*'mp4v'),2,(width,height))

def girar(startx, starty, endx, endy):
    a = -1
    first = 0
    for i in range(starty, endy+1):
        a = a + 1
        if a >= (endy-starty)/2 and first == 0:
            if endy-starty == endx - startx:
                first = 1
            elif endy-starty < endx - startx:
                first = 2
            else:
                first = 0
        for j in range(a+startx+first, endx+1):
            guardat = img[starty-i+endy, startx-j+endx]
            g, gu , gua = guardat[0], guardat[1], guardat[2]
            img[starty-i+endy, startx-j+endx]= img[i, j]
            img[i, j] = [g, gu, gua]
 
def div (startx, starty, endx, endy):
    if endx - startx <= 0 or endy - starty <= 0: #canviar els valors per conseguir mes o menys recursio
        return
    girar(startx, starty, endx, endy)
    div(startx, starty, int((endx+startx)/2), int((endy+starty)/2))
    div(int((endx+startx)/2)+1, starty, endx, int((endy+starty)/2))
    div(startx, int((endy+starty)/2)+1, int((endx+startx)/2), endy)
    div(int((endx+startx)/2)+1, int((endy+starty)/2)+1, endx, endy)
    return



div(0,0, img.shape[0]-1, img.shape[1]-1)


cv2.imshow('title', img)

print(img.shape[1])

cv2.waitKey(0)

cv2.imwrite('imatge.png',img)

cv2.destroyAllWindows()