# Step 1 - Create the App
# Step 2 - Create the Game
# Step 3 - Build the Game
# Step 4 - Run the App

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    pass

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest Positon of the ball latest position = current velocity + current position
    def moveBall(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player_left = ObjectProperty(None)
    player_right = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(5, 0).rotate(randint(0, 360))

    def update(self, dt):
        # UPDATE gets data from Clock.schedule_interval itsels, and timing 1.0/60.0 //moves the ball by calling move()
        self.ball.moveBall()

        # CONTROLS THE BOUNCE OF THE BALL TOP and BOTTOM and LEFT RIGHT
        if (self.ball.y < 0) or (self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1
        elif (self.ball.x < 0) or (self.ball.x > self.width - 50):
            self.ball.velocity_x *= -1

    def on_touch_move(self, touch):
        if touch.x < self.width * 0.25:
            self.player_left.center_y = touch.y

        if touch.x > self.width * 0.75:
            self.player_right.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)  # call update function
        return game


PongApp().run()