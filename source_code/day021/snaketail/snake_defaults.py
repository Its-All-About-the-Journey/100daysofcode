class SnakeDefaults:

    KEY_BINDINGS = {
        "Left": {"function": "set_heading_east", "heading": 0},
        "Up": {"function": "set_heading_north", "heading": 90},
        "Right": {"function": "set_heading_west", "heading": 180},
        "Down": {"function": "set_heading_south", "heading": 270}
    }

    SCOREBOARD = {
        "gameover_msg": "GAME OVER",
        "gameover_offset": 20,
        "offset_x": 30,
        "offset_y": 30,
        "color": "white"
    }

    SCREEN = {
        "bgcolor": "black",
        "title": "The Python Tail",
        "width": 600,
        "height": 600,
        "tracer": 0,
        "wall_offset": 10
    }

    TURTLE = {
        "shape": "circle",
        "color": "green",
        "step_len": 20,
        "speed": 0.1
    }