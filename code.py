from pyfiglet import Figlet

custom_fig = Figlet(font='graffiti')


def ascii(text):
  print(custom_fig.renderText(text))
