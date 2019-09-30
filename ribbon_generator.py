from numpy import *

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
    for point in points:
        svg += canvas_coords(*point)
    style = "fill:{};opacity:{};".format(fill, opacity)
    if stroke:
        style += "stroke-linejoin:round;stroke:{};stroke-width:1".format(stroke)
    svg += '''"
        style="{}"
        shape-rendering="geometricPrecision"
    />'''.format(style)
    return svg

p = array([
    [1, 0],
    [cos(1/5*tau), sin(1/5*tau)],
    [cos(2/5*tau), sin(2/5*tau)],
    [cos(3/5*tau), sin(3/5*tau)],
    [cos(4/5*tau), sin(4/5*tau)],
])

knot_tie = polygon([
    p[0], p[2], p[3], p[4],
], 'blue', 'blue')

knot_undertie = polygon([
    p[0], p[1], p[2], p[3],
], 'orange')

v = array([cos(1/5*tau) - 1, sin(1/5*tau)])
v_flip = v.copy()
v_flip[1] = -v_flip[1]

low_end = array([
    p[0] + v * (RIBBON_WIDTH-1),
    p[4] + v * RIBBON_WIDTH,
])
lower_strip = polygon([
    p[4],
    p[0],
    low_end[0],
    low_end[1],
], 'orange')

high_end = array([
    p[0] + v_flip * (RIBBON_WIDTH-1),
    p[1] + v_flip * RIBBON_WIDTH,
])
upper_strip = polygon([
    p[1],
    p[0],
    high_end[0],
    high_end[1],
], 'blue', 'blue')

low_end_2 = array([
    high_end[1] + v * (2*RIBBON_WIDTH-2),
    high_end[0] + v * (2*RIBBON_WIDTH-2),
])
lower_diagonal = polygon([
    high_end[0],
    high_end[1],
    low_end_2[0],
    low_end_2[1],
], 'orange')

high_end_2 = array([
    low_end[1] + v_flip * (2*RIBBON_WIDTH-2),
    low_end[0] + v_flip * (2*RIBBON_WIDTH-2),
])
upper_diagonal = polygon([
    low_end[0],
    low_end[1],
    high_end_2[0],
    high_end_2[1],
], 'blue', 'blue')

content = ""

content += lower_diagonal
content += knot_undertie
content += lower_strip
content += upper_strip
content += knot_tie

lower_strip = polygon([
    low_end_2[0],
    low_end_2[1],
    low_end_2[1] + v_flip * RIBBON_WIDTH,
    low_end_2[0] + v_flip * (RIBBON_WIDTH-1),
], 'blue')

upper_strip = polygon([
    high_end_2[0],
    high_end_2[1],
    high_end_2[1] + v * RIBBON_WIDTH,
    high_end_2[0] + v * (RIBBON_WIDTH-1),
], 'orange', 'orange')

c = high_end_2[0] + v * (RIBBON_WIDTH-1)
c[0] += 1
knot_tie = polygon([
    c - p[0],
    c - p[1],
    c - p[2],
    c - p[3],
], 'orange', 'orange')


knot_undertie = polygon([
    c - p[0],
    c - p[2],
    c - p[3],
    c - p[4],
], 'blue')

content += knot_undertie
content += lower_strip
content += upper_strip
content += knot_tie
content += upper_diagonal

print(PRELUDE + content + FINALE)
