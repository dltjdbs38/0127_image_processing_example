import cv2
import time

def onMouse(event, x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:#더블클릭시
        param[0] = cv2.circle(param[0],(x,y),50,(255,0,0),5)

if __name__=='__main__':
    img = cv2.imread('./Lenna.png', cv2.IMREAD_COLOR)
    cv2.namedWindow('My Image', cv2.WINDOW_AUTOSIZE) # 창을 열어서 이미지 보기
    # param = [img]
    # cv2.setMouseCallback('My Image', onMouse, param) #윈도우이름, 콜백함수
    # # time.sleep(5000) #5초
    # while True:
    #     key = cv2.waitKey(1000) # 창죽지말도록 키보드입력 받으면 종료됨 
    #     if key == ord('q'): #q를 누르면 종료해라
    #         break
    #     elif key ==ord('g'): # gray로 이미지를 변환해라
    #         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #     cv2.imshow('My Image', img) # 이미지보기

    roi = cv2.selectROI('My Image', img) # ROI = 관심가는 부분만 지정
    print(roi)