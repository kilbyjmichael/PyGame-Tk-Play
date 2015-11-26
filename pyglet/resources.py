import pyglet

pyglet.resource.path = ['resources']
pyglet.resource.reindex()

ball_img = pyglet.resource.image("ball.gif")

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width/2
    image.anchor_y = image.height/2

center_image(ball_img)
