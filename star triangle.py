def draw_triangle():
    for i in range(1, 16, 2):
        print((15-i) // 2 * ' ' + i * '*')
# основная программа
draw_triangle()  # вызов функции