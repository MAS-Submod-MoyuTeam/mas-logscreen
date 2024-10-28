init -1000 python in _fom_log_screen_utils:
    def quote(msg):
        return renpy.substitute("[msg!q]", {"msg": msg}, False)
