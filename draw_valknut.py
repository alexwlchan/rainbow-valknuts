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


def draw_valknut_bar(bar_width, gap_width, fill_color, proportion):
    # Coordinate axes
    #
    #              (0, t2)
    #             /
    #            /
    #           +------> (t1, 0)
    #
    # The shape to be drawn is defined as follows:
    #
    #
    #                                 (0, 6B+5W)
    #                                      /\
    #
    #                                 (B, 4B+3W)
    #                                      /\
    #
    #                    ..    ..                          ..   ..
    #                   /     /                              \    \
    #                  /     /                                \    \
    #      (0, 3B+2W) +-----+ (B, 3B+2W)        (2B+2W, 3B+2W) +----+ (3B+2W, 3B+2W)
    #
    #     (0, 2B+W) +-----+ (B, 2B+W)              (3B+3W, 2B+W) +-----+ (4B+3W, 2B+W)
    #              /     /                                        \     \
    #             /     /                                          \     \
    #            /     +--------------------------------------------+     \
    #           /  (B, B)                                      (4B+4W, B)  \
    #          /                                                            \
    #  (0, 0) +--------------------------------------------------------------+ (6B+5W, 0)
    #
    coordinates_lower = [
        (0, 0),
        (6 * bar_width + 5 * gap_width, 0),
        (4 * bar_width + 3 * gap_width, 2 * bar_width + gap_width),
        (3 * bar_width + 3 * gap_width, 2 * bar_width + gap_width),
        (4 * bar_width + 4 * gap_width, bar_width),
        (bar_width, bar_width),
        (bar_width, 2 * bar_width + gap_width),
        (0, 2 * bar_width + gap_width),
    ]

    coordinates_upper = [
        (0, 3 * bar_width + 2 * gap_width),
        (bar_width, 3 * bar_width + 2 * gap_width),
        (bar_width, 4 * bar_width + 3 * gap_width),
        (2 * bar_width + 2 * gap_width, 3 * bar_width + 2 * gap_width),
        (3 * bar_width + 2 * gap_width, 3 * bar_width + 2 * gap_width),
        (0, 6 * bar_width + 5 * gap_width),
    ]

    xy_coordinates_lower = [
        xy_position(*triangular_coords)
        for triangular_coords in coordinates_lower
    ]

    xy_coordinates_upper = [
        xy_position(*triangular_coords)
        for triangular_coords in coordinates_upper
    ]

    xy_points_lower = " ".join(xy_coordinates_lower)
    xy_points_upper = " ".join(xy_coordinates_upper)

    return f"""
        <polygon points="{xy_points_lower}" fill="{fill_color}"/>
        <polygon points="{xy_points_upper}" fill="{fill_color}"/>
    """


if __name__ == "__main__":
    print(
        draw_valknut_bar(
            bar_width=100,
            gap_width=10,
            fill_color="red",
            proportion=1.0
        )
    )