from math import *

tau = 2*pi

PRELUDE = """<!DOCTYPE html>
<html>
<body>

<h1>Mythra Ribbon Logo</h1>

<svg width="850" height="500" style="border:1px solid #000000;">"""

FINALE = """
</svg>

</body>
</html>"""

# RIBBON_WIDTH = 2.6  # Tight
# RIBBON_WIDTH = 3.685  # Loose
RIBBON_WIDTH = 3.0

ORIGIN_X = 720
ORIGIN_Y = 250
SCALE = 120


def canvas_coords(x, y):
    return "{},{} ".format(x*SCALE + ORIGIN_X, y*SCALE + ORIGIN_Y)


def polygon(points, fill='blue', stroke=None, opacity=0.9):
    svg = '''<polygon points="'''
    for point in zip(points[::2], points[1::2]):
        svg += canvas_coords(*point)
    style = "fill:{};opacity:{};".format(fill, opacity)
    if stroke:
        style += "stroke-linejoin:round;stroke:{};stroke-width:1".format(stroke)
    svg += '''"
        style="{}"
        shape-rendering="geometricPrecision"
    />'''.format(style)
    return svg


knot_tie = polygon([
    cos(0/5*tau), sin(0/5*tau),
    cos(2/5*tau), sin(2/5*tau),
    cos(3/5*tau), sin(3/5*tau),
    cos(4/5*tau), sin(4/5*tau),
], 'blue', 'blue')

knot_undertie = polygon([
    cos(0/5*tau), sin(0/5*tau),
    cos(1/5*tau), sin(1/5*tau),
    cos(2/5*tau), sin(2/5*tau),
    cos(3/5*tau), sin(3/5*tau),
], 'orange')

vec_x = cos(1/5*tau) - 1
vec_y = sin(1/5*tau)

lower_strip = polygon([
    cos(4/5*tau), sin(4/5*tau),
    cos(0/5*tau), sin(0/5*tau),
    cos(0/5*tau) + vec_x * (RIBBON_WIDTH - 1), sin(0/5*tau) + vec_y * (RIBBON_WIDTH - 1),
    cos(4/5*tau) + vec_x * RIBBON_WIDTH, sin(4/5*tau) + vec_y * RIBBON_WIDTH,
], 'orange')

upper_strip = polygon([
    cos(1/5*tau), sin(1/5*tau),
    cos(0/5*tau), sin(0/5*tau),
    cos(0/5*tau) + vec_x * (RIBBON_WIDTH - 1), sin(0/5*tau) - vec_y * (RIBBON_WIDTH - 1),
    cos(1/5*tau) + vec_x * RIBBON_WIDTH, sin(1/5*tau) - vec_y * RIBBON_WIDTH,
], 'blue', 'blue')

lower_diagonal = polygon([
    cos(0/5*tau) + vec_x * (RIBBON_WIDTH - 1), sin(0/5*tau) - vec_y * (RIBBON_WIDTH - 1),
    cos(1/5*tau) + vec_x * RIBBON_WIDTH, sin(1/5*tau) - vec_y * RIBBON_WIDTH,
    cos(1/5*tau) + vec_x * (2*RIBBON_WIDTH + 1), sin(1/5*tau) + vec_y*(RIBBON_WIDTH-2),
    cos(0/5*tau) + vec_x * (2*RIBBON_WIDTH), sin(0/5*tau) + vec_y*(RIBBON_WIDTH-1),
], 'orange')

upper_diagonal = polygon([
    cos(0/5*tau) + vec_x * (RIBBON_WIDTH - 1), sin(0/5*tau) + vec_y * (RIBBON_WIDTH - 1),
    cos(4/5*tau) + vec_x * RIBBON_WIDTH, sin(4/5*tau) + vec_y * RIBBON_WIDTH,
    cos(4/5*tau) + vec_x * (2*RIBBON_WIDTH +1), sin(4/5*tau) - vec_y * (RIBBON_WIDTH - 2),
    cos(0/5*tau) + vec_x * (2*RIBBON_WIDTH), sin(0/5*tau) - vec_y * (RIBBON_WIDTH - 1),
], 'blue', 'blue')

content = ""

content += lower_diagonal
content += knot_undertie
content += lower_strip
content += upper_strip
content += knot_tie

ORIGIN_X += vec_x*(3*RIBBON_WIDTH-1.895) * SCALE

knot_tie = polygon([
    -cos(0/5*tau), sin(0/5*tau),
    -cos(2/5*tau), sin(2/5*tau),
    -cos(3/5*tau), sin(3/5*tau),
    -cos(4/5*tau), sin(4/5*tau),
], 'orange', 'orange')

knot_undertie = polygon([
    -cos(0/5*tau), sin(0/5*tau),
    -cos(1/5*tau), sin(1/5*tau),
    -cos(2/5*tau), sin(2/5*tau),
    -cos(3/5*tau), sin(3/5*tau),
], 'blue')

lower_strip = polygon([
    -cos(4/5*tau), sin(4/5*tau),
    -cos(0/5*tau), sin(0/5*tau),
    -cos(0/5*tau) - vec_x * (RIBBON_WIDTH - 1), sin(0/5*tau) + vec_y * (RIBBON_WIDTH - 1),
    -cos(4/5*tau) - vec_x * RIBBON_WIDTH, sin(4/5*tau) + vec_y * RIBBON_WIDTH,
], 'blue')

upper_strip = polygon([
    -cos(1/5*tau), sin(1/5*tau),
    -cos(0/5*tau), sin(0/5*tau),
    -cos(0/5*tau) - vec_x * (RIBBON_WIDTH - 1), sin(0/5*tau) - vec_y * (RIBBON_WIDTH - 1),
    -cos(1/5*tau) - vec_x * RIBBON_WIDTH, sin(1/5*tau) - vec_y * RIBBON_WIDTH,
], 'orange', 'orange')

content += knot_undertie
content += lower_strip
content += upper_strip
content += knot_tie
content += upper_diagonal

print(PRELUDE + content + FINALE)
