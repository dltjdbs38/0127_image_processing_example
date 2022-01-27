import cv2

if __name__=='__main__':
    color_img = cv2.imread('./Lenna.png', cv2.IMREAD_COLOR)
    # gray_img = cv2.imread('./Lenna.png', cv2.IMREAD_GRAYSCALE)
    # if cv2.imwrite('./Lenna.jpg', gray_img):
    #     print('저장완료')
    # else:
    #     print('저장실패')
    # print(color_img.shape)
    # print(gray_img.shape)

    # convert
    # gray_img = cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)
    # cv2.imwrite('./Converted_to_gray.jpg', gray_img)

    # resize
    # resized_img = cv2.resize(color_img, (128,128))
    # cv2.imwrite('./Resized_img.jpg', resized_img)
    # print(resized_img)

    # crop : img는 행렬로 표현되므로 indexing을 해주면 된다.
    cropped_img = color_img[0:color_img.shape[0]//2, 0:color_img.shape[1]//2]
    print(cropped_img.shape)
    cv2.imwrite('Cropped_img.jpg', cropped_img)
    # img는 numpy.ndarray로 타입으로 행렬처럼 다뤄집니다.
    # 각 화소의 접근하기 위해서는 img[i, j]로 인덱싱을 하면 됩니다.