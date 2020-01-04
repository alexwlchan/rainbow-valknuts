#!/usr/bin/env python

import math


def x_component(triangular_x, triangular_y):
    result = triangular_x + triangular_y * math.cos(math.radians(60))
    return "%.6f" % result


def y_component(triangular_x, triangular_y):
    result = triangular_y * math.sin(math.radians(60))
    return "%.6f" % result


def xy_position(triangular_x, triangular_y):
    return "%s,%s" % (
        x_component(triangular_x, triangular_y),
        y_component(triangular_x, triangular_y)
    )


def get_valknut_tri_coordinates(bar_width, gap_width, stripe_count, stripe_index):
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
    #                                 (B, 4B+4W)
    #                                      /\
    #
    #                    ..    ..                          ..   ..
    #                   /     /                              \    \
    #                  /     /                                \    \
    #      (0, 3B+3W) +-----+ (B, 3B+3W)        (2B+2W, 3B+3W) +----+ (3B+2W, 3B+3W)
    #
    #     (0, 2B+W) +-----+ (B, 2B+W)              (3B+3W, 2B+W) +-----+ (4B+3W, 2B+W)
    #              /     /                                        \     \
    #             /     /                                          \     \
    #            /     +--------------------------------------------+     \
    #           /  (B, B)                                      (4B+4W, B)  \
    #          /                                                            \
    #  (0, 0) +--------------------------------------------------------------+ (6B+5W, 0)
    #
    # But then we need to adjust for the part of the stripe we're drawing.
    #
    lower_stripe = (stripe_index - 1) / stripe_count
    upper_stripe = stripe_index / stripe_count

    coordinates_lower = [
        (
            lower_stripe * bar_width,
            lower_stripe * bar_width
        ),
        (
            6 * bar_width + 5 * gap_width - lower_stripe * (2 * bar_width + gap_width),
            lower_stripe * bar_width
        ),
        (
            4 * bar_width + 3 * gap_width - lower_stripe * bar_width,
            2 * bar_width + gap_width
        ),
        (
            4 * bar_width + 3 * gap_width - upper_stripe * bar_width,
            2 * bar_width + gap_width,
        ),
        (
            6 * bar_width + 5 * gap_width - upper_stripe * (2 * bar_width + gap_width),
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
            6 * bar_width + 5 * gap_width - upper_stripe * (2 * bar_width + gap_width)
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
            6 * bar_width + 5 * gap_width - lower_stripe * (2 * bar_width + gap_width)
        )
    ]

    return [
        coordinates_lower,
        coordinates_upper,
    ]


def draw_valknut_coordinates(tri_coordinates, fill_color):
    xy_coords = [xy_position(*tri_coords) for tri_coords in tri_coordinates]
    xy_points = " ".join(xy_coords)

    print(f'<polygon points="{xy_points}" fill="{fill_color}"/>')


if __name__ == "__main__":
    print('<svg viewBox="0 0 1000, 1000" xmlns="http://www.w3.org/2000/svg">')

    for index, color in enumerate([
        "red", "orange", "yellow", "green", "blue"
    ], start=1):

        for tri_coords in get_valknut_tri_coordinates(
            bar_width=100,
            gap_width=10,
            stripe_count=6,
            stripe_index=index
        ):
            draw_valknut_coordinates(tri_coords, fill_color=color)

    print("</svg>")

