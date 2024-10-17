from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.graph import Graph, LinePlot
import numpy as np


class MainApp(App):
    def build(self):
        return Plotter()

class Plotter(BoxLayout):
    zoom = NumericProperty(1)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.samples = 512
        self.zoom = 1
        self.graph = Graph(xmin=0, xmax=self.samples,
                           ymin=-1, ymax=1,
                           border_color=[0, 1, 1, 1],
                           tick_color=[0, 1, 1, 0.7],
                           x_grid=True, y_grid=True,
                           draw_border=True,
                           x_grid_label=True, y_grid_label=True,
                           x_ticks_major=64, y_ticks_major=0.5)
        self.ids.graph.add_widget(self.graph)
        self.plot_x = np.linspace(0, 1, self.samples)
        self.plot_y = np.sin(2*np.pi*2*self.plot_x)
        self.plot = LinePlot(color=[1, 1, 0, 1], line_width=1.5)
        self.plot.points = [(x, self.plot_y[x]) for x in range(self.samples)]
        self.graph.add_plot(self.plot)

    def update_plot(self, freq):
        self.plot_y = np.sin(2*np.pi*freq*self.plot_x)
        self.plot.points = [(x, self.plot_y[x]) for x in range(self.samples)]

    def update_zoom(self, value):
        if value == "+" and self.zoom < 8:
            self.zoom *= 2
            self.graph.x_ticks_major /= 2
        elif value == "-" and self.zoom > 1:
            self.zoom /= 2
            self.graph.x_ticks_major *= 2

MainApp().run()
