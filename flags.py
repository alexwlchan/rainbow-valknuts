# Taken from https://github.com/queerjs/website/blob/fc6712d8e48ad185521a54e76f78eb3754bfe715/web/src/helpers/useRainbow.js

import colorsys


def to_pastel(hex_string):
    hex_string = hex_string.strip("#")
    assert len(hex_string) in {3, 6}

    if len(hex_string) == 6:
        r = int(hex_string[0:2], 16)
        g = int(hex_string[2:4], 16)
        b = int(hex_string[4:6], 16)
    else:
        r = int(hex_string[0] * 2, 16)
        g = int(hex_string[1] * 2, 16)
        b = int(hex_string[2] * 2, 16)

    hue, lightness, saturation = colorsys.rgb_to_hls(r, g, b)
    saturation *= 0.9
    lightness = lightness + (100 - lightness) * 0.2

    r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
    return f"#%02x%02x%02x" % (int(r), int(g), int(b))


def pastelise(colors):
    return [to_pastel(col) for col in colors]


flags = {
    "rainbow": ["#FF5D7D", "#FF764E", "#FFC144", "#88DF8E", "#00CCF2", "#B278D3"],
    "ace": pastelise(["#000000", "#A3A3A3", "#DDD", "#810082"]),
    "agender": pastelise(
        [
            "#000000",  # black
            "#BBC3C6",
            "#BBC3C6",  # grey
            "#FEFEFE",
            "#FEFEFE",  # white
            "#B7F582",
            "#B7F582",  # green
            "#FEFEFE",
            "#FEFEFE",  # white
            "#BBC3C6",
            "#BBC3C6",  # grey
            "#000000",  # black
        ]
    ),
    "aromantic": pastelise(["#3BA441", "#A8D378", "#FEFEFE", "#A9A9A9", "#000"]),
    "bear": pastelise(
        ["#4e2801", "#ca4e05", "#fdd951", "#fde2ac", "#EEE", "#424242", "#000000"]
    ),
    "lazy_bi_boy": pastelise(["#D9006F", "#D9006F", "#744D98"]),
    "lazy_bi_girl": pastelise(["#744D98", "#0033AB", "#0033AB"]),
    "bi": pastelise(["#D9006F", "#D9006F", "#744D98", "#0033AB", "#0033AB"]),
    "genderqueer": pastelise(["#B999DD", "#FEFEFE", "#6A8C3A"]),
    "non_binary": pastelise(["#FDF333", "#FEFEFE", "#9858CF", "#2D2D2D"]),
    "pan": pastelise(["#FF008E", "#FFD800", "#00B3FF"]),
    "philly": pastelise(
        [
            "#000",
            "#794F18",
            "#E40400",
            "#FE8C00",
            "#FFED00",
            "#008126",
            "#064EFF",
            "#750687",
        ]
    ),
    "poly": pastelise(["#F71BB9", "#08D569", "#1C91F6"]),
    "trans": ["#55CDFC", "#F7A8B8", "#DDD", "#F7A8B8", "#55CDFC"],
    "lesbian": [
        "#B60063",
        "#C84896",
        "#E253AB",
        "#DDD",
        "#F0A7D2",
        "#D73F4F",
        "#990200",
    ],
}

black_stripe = ["#000000"] * 4
blue_stripe = ["#0000c0"] * 4
red_stripe = ["#fb0006"]
white_stripe = ["#EEE"] * 4

flags["leather"] = pastelise(
    black_stripe
    + blue_stripe
    + red_stripe
    + black_stripe
    + blue_stripe
    + white_stripe
    + blue_stripe
    + black_stripe
    + blue_stripe
    + black_stripe
)
