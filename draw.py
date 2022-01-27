import cv2

if __name__=='__main__':
    img = cv2.imread('./Lenna.png', cv2.IMREAD_COLOR)
    # line_img = cv2.line(img, (0,0), (img.shape[0], img.shape[1]), (255,0,0), 1, cv2.LINE_AA)
    
    # circle_img = cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 100, (0,255,0), 5)

    # target_img = cv2.rectangle(img, (100,100), (300,400), (0,0,255), 5)

    target_img = cv2.putText(img,'Hi Im Seoyoon',(100,100),cv2.FONT_HERSHEY_SIMPLEX,2.7,(128,0,128),5)
    cv2.imwrite('./Draw_text.jpg', target_img)
    print('hello')