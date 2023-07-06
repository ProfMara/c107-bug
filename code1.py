import cv2
#criando uma lista de posições no eixo x
xs = []
ys = []
def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    #desenha o retângulo ao redor da caixa delimitadora
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,255),3,1)
    cv2.putText(img, "Rastreando...", (75,90), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,200,0), 2 )
    cx = x + int(w/2)
    cy = y + int(h/2)
    cv2.circle(img, (cx, cy), 2,(0, 255,0), 3)
    #add a pos do centro no eixo x na lista de posições X
    xs.append(cx)
    #add a pos Y
    ys.append(cy)

    #percorrer a lista para desenhar círculos
    for i in range(len(xs)-1):
        cv2.circle(img, (xs[i], ys[i]),2,(0,255,244),1 )

video = cv2.VideoCapture("ball.mp4")

tracker = cv2.TrackerCSRT_create()
#ler o primeiro quadro do video
returned, frame = video.read()
bbox = cv2.selectROI("", frame, False)
tracker.init(frame, bbox)

while True:

    ret, frame = video.read()
    success, bbox = tracker.update(frame)
    if success:
        drawBox(frame, bbox)
    else:
        cv2.putText(frame, "errou...", (75, 90), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,200,0), 2)
    if ret:
        cv2.imshow("video", frame)
    if cv2.waitKey(2)==32:
        break

video.release()
cv2.destroyAllWindows()