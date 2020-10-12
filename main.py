import arcade
import random

WIDTH = 1000
HEIGHT = 1000
SCALE = 0.07
# LOWER = 3
# UPPER = 5

class Simulation(arcade.Window):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__(WIDTH, HEIGHT)
        self.agents_healthy = arcade.SpriteList()
        self.agents_ill = arcade.SpriteList()
        self.steps = dict()
        self.setup()


    def setup(self, n=100):
        arcade.set_background_color(arcade.color.BLACK)
        for x in range(n):
            agent = arcade.Sprite("dot.png", SCALE)
            agent.center_x = random.randint(0, WIDTH)
            agent.center_y = random.randint(0, HEIGHT)
            agent.change_x = random.uniform(-1,1)
            agent.change_y = random.uniform(-1,1)
            self.steps[agent] = 5
            self.agents_healthy.append(agent)

    def on_draw(self):
        arcade.start_render()
        self.agents_healthy.draw()

    def on_update(self, delta_time: float):
        for agent in self.agents_healthy:
            if not self.steps[agent]:
                self.steps[agent] = 5
            agent.center_x += agent.change_x*self.steps[agent]
            agent.center_y += agent.change_y*self.steps[agent]
            agent.center_x = agent.center_x % WIDTH
            agent.center_y = agent.center_y % HEIGHT
            agent.change_x += random.uniform(-0.3,0.3)
            agent.change_y += random.uniform(-0.3,0.3)
            self.steps[agent] -= 1



def main():
    window = Simulation(WIDTH, HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()