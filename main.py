def on_forever():
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(500)
    basic.show_leds("""
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(500)
    basic.show_leds("""
        # # # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(500)
    basic.clear_screen()
basic.forever(on_forever)
