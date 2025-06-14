import streamlit as st
from PIL import Image, ImageDraw
import math
import random
import time
import numpy as np

WIDTH, HEIGHT = 320, 256
CANDLE_COUNT = 3
CANDLE_BASE_Y = 80
CANDLE_HEIGHT = 32
CAKE_TOP = 100
CAKE_BOTTOM = 180
CANDLE_COLORS = [(255, 0, 0), (255, 255, 0), (0, 191, 255)]

def draw_cake(candle_offsets):
    img = Image.new("RGB", (WIDTH, HEIGHT), (68, 36, 52))
    draw = ImageDraw.Draw(img)
    draw.rectangle([60, CAKE_TOP, 260, CAKE_BOTTOM], fill=(255, 216, 124), outline=(126, 82, 36))
    draw.rectangle([60, 150, 260, CAKE_BOTTOM], fill=(255, 178, 102), outline=(126, 82, 36))
    draw.rectangle([60, CAKE_TOP, 260, CAKE_TOP+18], fill=(255, 255, 255))
    draw.rectangle([60, CAKE_BOTTOM, 260, CAKE_BOTTOM+8], fill=(180, 137, 82))
    draw.rectangle([50, CAKE_BOTTOM+8, 270, CAKE_BOTTOM+20], fill=(200, 200, 220))
    for i in range(CANDLE_COUNT):
        x = 100 + i * 40
        offset = candle_offsets[i]
        draw.rectangle([x+offset, CANDLE_BASE_Y, x+8+offset, CANDLE_BASE_Y+CANDLE_HEIGHT], fill=CANDLE_COLORS[i], outline=(80,80,80))
        flame_x = x+4+offset+random.randint(-1,1)
        flame_y = CANDLE_BASE_Y-8+random.randint(-1,1)
        draw.ellipse([flame_x-4, flame_y-5, flame_x+4, flame_y+3], fill=(255, 233, 82), outline=(255, 140, 0))
    draw.text((70, 24), "happy birthday", fill=(255,255,255))
    return img

st.title('生热快乐！Happy Birthday')

frame = st.empty()
angles = [0, 0.7, 1.4]
speeds = [0.05, 0.06, 0.07]
for _ in range(60):
    offsets = [int(math.sin(a)*4) for a in angles]
    img = draw_cake(offsets)
    frame.image(np.array(img))
    angles = [a + b for a, b in zip(angles, speeds)]
    time.sleep(0.08)
