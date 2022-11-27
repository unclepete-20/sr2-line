from bmp_renderer import Render

frame = Render()

frame.glCreateWindow(300, 300)

frame.glViewPort(30, 30, 250, 250)

frame.glClear()

frame.glColor(255, 0, 0)

# House drawing
frame.glLine(-1, 0, -0.6, -0.6)
frame.glLine(-1, 0, -1, 0.5)
frame.glLine(-1, 0.5, -0.6, 0.2)
frame.glLine(-0.6, 0.2, -0.6, -0.6)
frame.glLine(-0.6, -0.6, 0, -0.5)
frame.glLine(0, -0.5, 0, -0.2)
frame.glLine(0, -0.2, 0.3, -0.15)
frame.glLine(0.3, -0.15, 0.3, -0.45)
frame.glLine(0.3, -0.45, 0.8, -0.38)
frame.glLine(0.8, -0.38, 0.8, 0.2)
frame.glLine(0.8, 0.2, 0.15, 0.6)
frame.glLine(-0.6, 0.2, 0.15, 0.6)
frame.glLine(0.15, 0.6, -0.6, 0.8)
frame.glLine(-1, 0.5, -0.6, 0.8)

# Chimney
frame.glLine(-0.3, 0.72, -0.3, 0.85)
frame.glLine(-0.2, 0.7, -0.2, 0.8)
frame.glLine(-0.1, 0.67, -0.1, 0.85)
frame.glLine(-0.3, 0.85, -0.2, 0.8)
frame.glLine(-0.2, 0.8, -0.1, 0.85)
frame.glLine(0.8, 0.2, 0.15, 0.6)
frame.glLine(-0.3, 0.85, -0.2, 0.9)
frame.glLine(-0.2, 0.9, -0.1, 0.85)

frame.glFinish('house.bmp')