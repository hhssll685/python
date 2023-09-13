import turtle as t  #


t.shape('turtle')
t.speed(2)


# 선그리기
# t.forward(200)  # 200 픽셀 이동.

# 삼각형 그리기
# t.forward(200)  # 200 픽셀 만큼 이동.
# t.left(120)     # 왼쪽으로 120도 회전.
# t.forward(200)  # 200 픽셀 만큼 이동.
# t.left(120)     # 왼쪽으로 120도 회전.
# t.forward(200)  # 200 픽셀 만큼 이동.
# t.left(120)     # 왼쪽으로 120도 회전.

for i in range(9):
    t.forward(200)  # 200 픽셀 만큼 이동.
    t.left(144)  # 왼쪽으로 120도 회전.


t.mainloop()  # 그림판 사라지지 않는다
