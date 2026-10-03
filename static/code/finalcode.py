current_val = 0
strip = neopixel.create(DigitalPin.P0, 12, NeoPixelMode.RGB)
strip.set_brightness(60)
raw_data = [-11, -17, -2, 15, 29, -1, -3, -11, 21, 81, 84, 127]
for j in range(12):
    current_val = raw_data[j]
    if current_val <= -15:
        strip.set_pixel_color(j, neopixel.colors(NeoPixelColors.BLUE))
    elif current_val <= -6:
        strip.set_pixel_color(j, neopixel.rgb(0, 150, 255))
    elif current_val <= 15:
        strip.set_pixel_color(j, neopixel.colors(NeoPixelColors.WHITE))
    elif current_val <= 82:
        strip.set_pixel_color(j, neopixel.colors(NeoPixelColors.ORANGE))
    else:
        strip.set_pixel_color(j, neopixel.colors(NeoPixelColors.RED))
strip.show()
