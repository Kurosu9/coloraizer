from tkinter import *
from time import sleep
from random import randint, choice


class Field():
    def __init__(self, c, n, m, width, height):
        self.c = c
        self.a = []
        self.n = n
        self.m = m
        self.width = width
        self.height = height
        self.count = 0
        for i in range(self.n):
            self.a.append([])
            for j in range(self.m):
                self.a[i].append(1)
                self.a[i].append(1)

        self.draw()

    def step(self):
        b = []
        for i in range(self.n):
            b.append([])
            for j in range(self.m):
                b[i].append(0)

        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                neib_sum = (self.a[i - 1][j - 1] + self.a[i - 1][j] + self.a
                            [i - 1][j + 1] + self.a[i][j - 1] + self.a[i - 1]
                            [j + 1] + self.a[i + 1][j - 1] + self.a[i + 1][j] +
                            self.a[i + 1][j + 1])
                if neib_sum < randint(1, 10):
                    b[i][j] = 1
                else:
                    b[i][j] = self.a[i][j]
        self.a = b
        'sleep(3)'

    def print_field(self):
        for i in range(self.n):
            for j in range(self.m):
                print(self.a[i][j], end="")
            print()

    def draw(self):
        color = "grey"
        'If you want, you can change color here'
        black_white_style = ("black", "dimgray", "dimgrey", "gray", "grey",
                             "darkgray", "darkgrey", "silver", "lightgray",
                             "lightgrey", "gainsboro", "whitesmoke", "white",
                             "snow")
        red_brown_style = ("rosybrown", "lightcoral", "indianred", "brown",
                           "firebrick", "maroon", "darkred", "red",
                           "mistyrose", "salmon", "tomato", "darksalmon",
                           "coral", "orangered", "lightsalmon", "sienna",
                           "seashell", "chocolate", "saddlebrown",
                           "sandybrown", "peachpuff", "linen", "crimson")
        orange_yellow_style = ("bisque", "darkorange", "burlywood",
                               "antiquewhite", "tan", "navajowhite",
                               "blanchedalmond", "papayawhip", "moccasin",
                               "orange", "wheat", "oldlace", "floralwhite",
                               "darkgoldenrod", "goldenrod", "cornsilk",
                               "gold", "lemonchiffon", "khaki",
                               "palegoldenrod", "darkkhaki", "ivory", "beige",
                               "lightyellow", "lightgoldenrodyellow", "yellow")
        green_style = ("olive", "olivedrab", "yellowgreen", "darkolivegreen",
                       "greenyellow", "chartreuse", "lawngreen", "honeydew",
                       "darkseagreen", "palegreen", "lightgreen",
                       "forestgreen", "limegreen", "darkgreen", "green",
                       "lime", "seagreen", "mediumseagreen", "springgreen",
                       "mintcream", "mediumspringgreen")
        blue_style = ("mediumaquamarine", "aquamarine", "turquoise",
                      "lightseagreen", "mediumturquoise", "azure", "lightcyan",
                      "paleturquoise", "darkslategray", "darkslategrey",
                      "teal", "darkcyan", "aqua", "cyan", "darkturquoise",
                      "cadetblue", "powderblue", "lightblue", "deepskyblue",
                      "skyblue", "lightskyblue", "steelblue", "aliceblue",
                      "dodgerblue", "lightslategray", "lightslategrey",
                      "slategray", "slategrey", "lightsteelblue",
                      "cornflowerblue", "royalblue", "ghostwhite", "lavender",
                      "midnightblue", "navy", "darkblue", "mediumblue", "blue",
                      "slateblue", "darkslateblue", "mediumslateblue")
        purple_pink_style = ("mediumpurple", "blueviolet", "indigo",
                             "darkorchid", "darkviolet", "mediumorchid",
                             "thistle", "plum", "violet", "purple",
                             "darkmagenta", "fuchsia", "magenta", "orchid",
                             "mediumvioletred", "deeppink", "hotpink",
                             "lavenderblush", "palevioletred", "pink",
                             "lightpink")
        sizen = self.width // (self.n - 2)
        sizem = self.height // (self.m - 2)
        for i in range(1, self.n - 1):
            for j in range(1, self.m - 1):
                if (self.a[i][j] == 1):
                    'You can change style to show in the field here'
                    color = choice(red_brown_style + black_white_style +
                                   orange_yellow_style + green_style +
                                   blue_style + purple_pink_style)
                else:
                    color = "white"
                self.c.create_rectangle((i-1) * sizen, (j-1) * sizem, (i) *
                                        sizen, (j) * sizem, fill=color)
        self.step()
        self.c.after(100, self.draw)

root = Tk()
root.geometry("600x800")
c = Canvas(root, width=500, height=500)
c.pack()

f = Field(c, 40, 40, 800, 800)
f.print_field()


def resize():
    w = width_entry.get()
    h = height_entry.get()
    root.geometry(f"{w}x{h}")

width_label = Label(root, text="Width:")
width_label.pack()
width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text="Heght:")
height_label.pack()
height_entry = Entry(root)
height_entry.pack()

button = Button(root, text="Resize", command=resize)
button.pack(pady=20)

root.mainloop()
