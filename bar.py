from PIL import Image
import time

def main(number=1):
  bar_complete = "./img/source/bar_complete.jpeg"

  img_complete = Image.open(bar_complete) 
  width, height = img_complete.size 

  in_percent = number/100
  value = 900*in_percent

  area = (0, 0, ((0+value)+50), height) 
  img_complete = img_complete.crop(area) 
  #950 == 0%
  #em 0% colocar o bar_back
  img_complete.save("./img/bar_cropped.jpeg")  
    
  bar_back = "./img/source/bar.jpeg"

  img_bar = Image.open(bar_back) 

  img_bar.paste(img_complete, (0, 0)) 
  img_bar.save("./img/bar_final.jpeg")


if __name__ == "__main__": 
  main() 