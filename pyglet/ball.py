import pyglet
import resources

main_window = pyglet.window.Window(500,500)
test_label = pyglet.text.Label(text="Testing", x=100, y=99)
ball_sprite = pyglet.sprite.Sprite(img=resources.ball_img, x=250, y=250)

@main_window.event
def on_draw():
    main_window.clear()

    test_label.draw()
    ball_sprite.draw()
    

if __name__=='__main__':
    pyglet.app.run()
