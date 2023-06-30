import argparse
from rife_ncnn_vulkan_python import Rife
from PIL import Image
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()
path = args.path
f = open(path + '/tri_testlist.txt', 'r')
j=0
print(f'=========================Starting Generation=========================')
for i in f:
  name = str(i).strip()
  if(len(name) < 1):
        continue
  with Image.open(path + name + '\\' +'0.jpg') as image0:
    with Image.open(path + name + '\\' + '8.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'4.jpg')
  with Image.open(path + name + '\\' +'0.jpg') as image0:
    with Image.open(path + name + '\\' + '4.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'2.jpg')
  with Image.open(path + name + '\\' +'0.jpg') as image0:
    with Image.open(path + name + '\\' + '2.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'1.jpg')
  with Image.open(path + name + '\\' +'2.jpg') as image0:
    with Image.open(path + name + '\\' + '4.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'3.jpg')
  with Image.open(path + name + '\\' +'4.jpg') as image0:
    with Image.open(path + name + '\\' + '8.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'6.jpg')
  with Image.open(path + name + '\\' +'4.jpg') as image0:
    with Image.open(path + name + '\\' + '6.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'5.jpg') 
  with Image.open(path + name + '\\' +'6.jpg') as image0:
    with Image.open(path + name + '\\' + '8.jpg') as image1:
      rife = Rife(gpuid=0) # or RIFE(0) like upstream
      image = rife.process(image0, image1)
      image.save(path + name + '\\' +'7.jpg')      
print(f'=========================Done=========================')