import turtle as t
import random as r
import time

# Đặt tốc độ vẽ
t.speed("fastest")

# Thiết lập màn hình
t.screensize(bg='black')

# Hàm kiểm soát thời gian vẽ
def draw_within_time_limit(duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        draw_tree()

# Hàm vẽ cây
def draw_tree():
    n = 100.0
    t.left(90)
    t.forward(3 * n)
    t.color("orange", "yellow")
    t.begin_fill()
    t.left(126)
    for i in range(5):
        t.forward(n / 5)
        t.right(144)
        t.forward(n / 5)
        t.left(72)
    t.end_fill()
    t.right(126)

    color = ('tomato', 'orange', 'dark green')

    def draw_light():
        if r.randint(0, 30) == 0:
            t.color('tomato')
            t.circle(6)
        elif r.randint(0, 30) == 1:
            t.color('orange')
            t.circle(3)
        else:
            t.color('dark green')

    t.color("dark green")
    t.backward(n * 4.8)

    def tree(d, s):
        if d <= 0:
            return
        t.forward(s)
        tree(d - 1, s * 0.8)
        t.right(120)
        tree(d - 3, s * 0.5)
        draw_light()
        t.right(120)
        tree(d - 3, s * 0.5)
        t.right(120)
        t.backward(s)

    tree(15, n)
    t.backward(n / 2)

# Gọi hàm vẽ trong 10 giây
draw_within_time_limit(10)

# Kết thúc chương trình
t.done()
