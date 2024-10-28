transform fom_log_screen_slide(offscreen_pos):
    on show:
        ypos offscreen_pos
        easeout 0.7 ypos 0
    on hide:
        ypos 0
        easein 0.7 ypos offscreen_pos

screen fom_log_screen():
    zorder 100

    python:
        config = store._fom_log_screen_config.get_config()
        handler = store._fom_log_screen_handler.get_handler()
        handler.update_log_lines()

        panel_size = max(1, len(handler.display_lines)) * config.font_ysize + 3
        offscreen_pos = -(max(1, len(handler.display_lines)) * config.font_ysize + 10)

    frame at fom_log_screen_slide(offscreen_pos):
        xanchor 0
        yanchor 0

        xpos 0
        ypos 0

        xfill True
        ysize panel_size

        background config.panel_background_color

        fixed:
            $ line_ypos = panel_size
            if len(handler.display_lines) > 0:
                use fom_log_screen_lines(handler.display_lines, line_ypos)
            else:
                use fom_log_screen_line("{color=#eeeeee}No log records here :({/color}", line_ypos)

screen fom_log_screen_lines(log_lines, line_ypos):
    $ config = store._fom_log_screen_config.get_config()
    for line in range(len(log_lines) - 1, -1, -1):
        $ log_line = log_lines[line]
        use fom_log_screen_line(log_line, line_ypos - 3)
        $ line_ypos -= config.font_ysize

screen fom_log_screen_line(log_line, line_ypos):
    text "[log_line!i]":
        style "mas_py_console_text"
        anchor (0, 1.0)
        xpos 3
        ypos line_ypos

init 10 python in _fom_log_screen:
    from store.mas_submod_utils import functionplugin
    from store._fom_log_screen_config import get_config
    from store._fom_log_screen_handler import show_screen

    @functionplugin("ch30_preloop", priority=0)
    def on_preloop():
        if get_config().show_on_startup:
            show_screen()
