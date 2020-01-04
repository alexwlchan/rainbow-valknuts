#!/usr/bin/env python

import math


def x_component(triangular_x, triangular_y):
    result = triangular_x + triangular_y * math.cos(math.radians(60))
    return "%.6f" % result


def y_component(triangular_x, triangular_y):
    result = -triangular_y * math.sin(math.radians(60))
    return "%.6f" % result


def xy_position(triangular_x, triangular_y):
    return "%s,%s" % (
        x_component(triangular_x, triangular_y),
        y_component(triangular_x, triangular_y)
    )


def get_valknut_tri_coordinates(bar_width, gap_width, stripe_count, stripe_start, stripe_end):
    """
    Stripes are 1-indexed.
    """
    # Coordinate axes
    #
    #              (0, t2)
    #             /
    #            /
    #           +------> (t1, 0)
    #
    # The shape to be drawn is defined as follows:
    #
    #                                 (0, 6B+5W)
    #                                      /\
    #
    #                                 (B, 4B+5W)
    #                                      /\
    #
    #                    ..    ..                          ..   ..
    #                   /     /                              \    \
    #                  /     /                                \    \
    #      (0, 3B+3W) +-----+ (B, 3B+3W)        (2B+2W, 3B+3W) +----+ (3B+2W, 3B+3W)
    #
    #     (0, 2B+W) +-----+ (B, 2B+W)              (3B+4W, 2B+W) +-----+ (4B+4W, 2B+W)
    #              /     /                                        \     \
    #             /     /                                          \     \
    #            /     +--------------------------------------------+     \
    #           /  (B, B)                                      (4B+5W, B)  \
    #          /                                                            \
    #  (0, 0) +--------------------------------------------------------------+ (6B+5W, 0)
    #
    # But then we need to adjust for the part of the stripe we're drawing.
    #
    lower_stripe = (stripe_start - 1) / stripe_count
    upper_stripe = stripe_end / stripe_count

    coordinates_lower = [
        (
            lower_stripe * bar_width,
            lower_stripe * bar_width
        ),
        (
            6 * bar_width + 5 * gap_width - lower_stripe * (2 * bar_width),
            lower_stripe * bar_width
        ),
        (
            4 * bar_width + 4 * gap_width - lower_stripe * bar_width,
            2 * bar_width + gap_width
        ),
        (
            4 * bar_width + 4 * gap_width - upper_stripe * bar_width,
            2 * bar_width + gap_width,
        ),
        (
            6 * bar_width + 5 * gap_width - upper_stripe * (2 * bar_width),
            upper_stripe * bar_width,
        ),
        (
            upper_stripe * bar_width,
            upper_stripe * bar_width
        ),
        (
            upper_stripe * bar_width,
            2 * bar_width + gap_width
        ),
        (
            lower_stripe * bar_width,
            2 * bar_width + gap_width
        ),
    ]

    coordinates_upper = [
        (lower_stripe * bar_width, 3 * bar_width + 3 * gap_width),
        (upper_stripe * bar_width, 3 * bar_width + 3 * gap_width),
        (
            upper_stripe * bar_width,
            6 * bar_width + 5 * gap_width - upper_stripe * (2 * bar_width)
        ),
        (
            3 * bar_width + 2 * gap_width - upper_stripe * bar_width,
            3 * bar_width + 3 * gap_width
        ),
        (
            3 * bar_width + 2 * gap_width - lower_stripe * bar_width,
            3 * bar_width + 3 * gap_width
        ),
        (
            lower_stripe * bar_width,
            6 * bar_width + 5 * gap_width - lower_stripe * (2 * bar_width)
        )
    ]

    return [
        coordinates_lower,
        coordinates_upper,
    ]


def draw_valknut(bar_width, gap_width, stripes):
    for index, fill_color in enumerate(stripes, start=1):
        stripe_start = index
        try:
            if stripes[index] == fill_color:
                stripe_end = index + 1
            else:
                stripe_end = index
        except IndexError:
            stripe_end = index

        for tri_coords in get_valknut_tri_coordinates(
            bar_width=bar_width,
            gap_width=gap_width,
            stripe_count=len(stripes),
            stripe_start=stripe_start,
            stripe_end=stripe_end
        ):
            xy_coords = [xy_position(*tc) for tc in tri_coords]
            xy_points = " ".join(xy_coords)

            yield f'<polygon points="{xy_points}" fill="{fill_color}"/>'


def get_valknut_svg(stripe1, stripe2, stripe3):
    lines = [
        '<svg viewBox="0 0 900, 400" xmlns="http://www.w3.org/2000/svg">'
    ]

    has_black = any("#000000" in s for s in (stripe1, stripe2, stripe3))

    if has_black:
        background = "#222222"
    else:
        background = "black"

    lines.extend([
        f'<polygon points="0,0 900,0 900,600 0,600" fill="{background}"/>',

        # Centre the valknut on the page by trial and error.
        '<g transform="translate(229 460)">',
    ])

    bar_width = 50
    gap_width = 10

    for svg_line in draw_valknut(
        bar_width=bar_width, gap_width=gap_width, stripes=stripe1
    ):
        lines.append(svg_line)

    center = xy_position(
        2 * bar_width + 5/3 * gap_width,
        3 * bar_width + (8/3) * gap_width,
    )

    lines.append(f'<g transform="rotate(120 {center})">')

    for svg_line in draw_valknut(
        bar_width=bar_width, gap_width=gap_width, stripes=stripe2
    ):
        lines.append(svg_line)

    lines.append('</g>')

    lines.append(f'<g transform="rotate(240 {center})">')

    for svg_line in draw_valknut(
        bar_width=bar_width, gap_width=gap_width, stripes=stripe3
    ):
        lines.append(svg_line)

    lines.append('</g>')
    lines.append('</g>')

    lines.append('</svg>')

    return '\n'.join(lines)


if __name__ == "__main__":
    print(
        get_valknut_svg(
            stripe1=["red", "orange", "yellow", "green", "blue", "purple"],
            stripe2=["#5BCEFA", "#F5A9B8", "white", "#F5A9B8", "#5BCEFA"],
            stripe3=["#000000", "#A3A3A3", "white", "#780378"],
        )
    )
