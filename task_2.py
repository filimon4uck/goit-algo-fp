import turtle
import math


def config_screen():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")
    return screen


def create_turtle():
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()
    return t


def interpolate_color(level, max_level):
    start_color = (34, 139, 34)
    end_color = (139, 69, 19)
    ratio = level / max_level
    r = int(start_color[0] * (1 - ratio) + end_color[0] * ratio)
    g = int(start_color[1] * (1 - ratio) + end_color[1] * ratio)
    b = int(start_color[2] * (1 - ratio) + end_color[2] * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"


def draw_branch(t, branch_length, angle, level, max_level):
    if level == 0:
        t.penup()
        return
    t.pendown()
    t.pensize(level * 1)
    t.color(interpolate_color(level, max_level))
    t.forward(branch_length)

    t.left(angle)
    draw_branch(
        t, branch_length * math.cos(math.radians(angle)), angle, level - 1, max_level
    )

    t.right(2 * angle)
    draw_branch(
        t, branch_length * math.cos(math.radians(angle)), angle, level - 1, max_level
    )

    t.left(angle)
    t.backward(branch_length)


def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (рекомендується 5-10): "))
            break
        except ValueError:
            print("Введіть коректне число для рівня рекурсії")

    screen = config_screen()
    t = create_turtle()
    draw_branch(t, branch_length=140, angle=30, level=level, max_level=level)
    screen.mainloop()


if __name__ == "__main__":
    main()
