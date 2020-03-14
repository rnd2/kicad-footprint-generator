""" Calculates the silkscreen lines for components with
non-standard pin number positions.

calc_silk_y: Calculates the start and end coordinates for
    the left and right lines on either side of the part.

    Showing silk arrangement for CCW pin count.
    Silkscreen indpendent of CW/CCW.

    l1      l2
               top_left
               --------
      1*  4 | l1 (0, body_edge['bottom'])
    | 2   3 | l2 (body_edge['top'], body_edge['bottom'])

               bottom_left
               -----------
    | 4   3 | l1 (0, body_edge['top'])
      1*  2 | l2 (body_edge['top'], body_edge['bottom'])

               bottom_right
               ------------
    | 3   2 | l1 (body_edge['top'], body_edge['bottom'])
    | 4   1*  l2 (0, body_edge['top'])

               top_right
               ---------
    | 2   1*  l1 (body_edge['top'], body_edge['bottom'])
    | 3   4 | l2 (0, body_edge['bottom'])

    There are three different lines:
     1. (0, body_edge['top'])
     2. (0, body_edge['bottom'])
     3. (body_edge['top'], body_edge['bottom'])

calc_silk_x: Calculates the start and end coordinates for
    the top and bottom lines on either side of the part.

    Showing silk arrangement for CCW pin count.
    Silkscreen indpendent of CW/CCW.

               top_left
l1    ---      --------
    1*  4  l1 (0, body_edge['right'])
    2   3  l2 (body_edge['left'], body_edge['right'])
l2  -----
                bottom_left
    _____      -----------
    4   3  l1 (body_edge['left'], body_edge['right'])
    1*  2  l2 (0, body_edge['right'])
      ---
                bottom_right
    _____      ------------
    3   2  l1 (body_edge['left'], body_edge['right'])
    4   1* l2 (0, body_edge['left'])
    ---
                top_right
    ___         ---------
    2   1* l1 (0, body_edge['left'])
    3   4  l2 (body_edge['left'], body_edge['right'])
    -----

    There are three different lines:
      1. (0, body_edge['top'])
      2. (0, body_edge['bottom'])
      3. (body_edge['top'], body_edge['bottom'])

"""


def calc_silk_x(device_params, body_edge):
    """Calculates the start and end coordinates for
    the top and bottom lines on either side of the part.

    Args:
        device_params: Device parameters dictionary
        body_edge: Part's body edge dict

    Returns:
       line1, line2: Silkscreen lines

    """
    lines = [
        (0, body_edge["left"]),
        (0, body_edge["right"]),
        (body_edge["left"], body_edge["right"]),
    ]

    # Default silkscreen lines
    line1, line2 = lines[1], lines[2]

    if device_params.get("pad_numbers"):
        start = device_params["pad_numbers"].get("start") or "top_left"
        # start can be either of "[top, bottom]_[left, right]"
        tb, lr = start.split("_")

        if "top" in tb:
            line2 = lines[2]
            if "left" in lr:
                line1 = lines[1]
            else:
                line1 = lines[0]
        else:
            line1 = lines[2]
            if "left" in lr:
                line2 = lines[1]
            else:
                line2 = lines[0]
    return line1, line2


def calc_silk_y(device_params, body_edge):
    """Calculates the start and end coordinates for
    the left and right lines on either side of the part.

    Args:
        device_params: Device parameters dictionary
        body_edge: Part's body edge dict

    Returns:
       line1, line2: Silkscreen lines
    """
    lines = [
        (0, body_edge["top"]),
        (0, body_edge["bottom"]),
        (body_edge["top"], body_edge["bottom"]),
    ]

    # Default silkscreen lines
    line1, line2 = lines[1], lines[2]

    if device_params.get("pad_numbers"):
        start = device_params["pad_numbers"].get("start") or "top_left"
        # start can be either of "[top, bottom]_[left, right]"
        tb, lr = start.split("_")

        if "left" in lr:
            line2 = lines[2]
            if "top" in tb:
                line1 = lines[1]
            else:
                line1 = lines[0]
        else:
            line1 = lines[2]
            if "top" in tb:
                line2 = lines[1]
            else:
                line2 = lines[0]
    return line1, line2
