class SnakeDefaults:

    SCREEN = {
        "bgcolor": "black",
        "title": "The Python Tail",
        "width": 600,
        "height": 600,
        "tracer": 0
    }

    TURTLE = {
        "shape": "circle",
        "color": "green",
        "step_len": 20
    }

    KEY_BINDINGS = {
        "Left": {"function": "set_heading_east", "heading": 0},
        "Up": {"function": "set_heading_north", "heading": 90},
        "Right": {"function": "set_heading_west", "heading": 180},
        "Down": {"function": "set_heading_south", "heading": 270}
    }

    HEADINGS = {}