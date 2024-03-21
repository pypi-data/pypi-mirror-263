# BrightnessBooster
The code enhances an image's brightness and contrast

## Description
### Main functions in library
```python
beta_parameters_of_image
birghtness_contrast_from_beta_parameters
approximate_beta_distribution
modify_image
```
## How to use
### How to modify image using BrightnessBooster library
```python
import BrightnessBooster as BB
from PIL import Image

#test image
image_path = 'test_image.jpg'

# load test image use Pillow
image = Image.open(image_path)

# show image
image.show()
a_red_org, b_red_org, a_green_org, b_green_org, a_blue_org, b_blue_org = BB.beta_parameters_of_image(image)
print('Betta parameters of original image:')
print(f'a_red = {a_red_org}')
print(f'b_red = {b_red_org}')
print(f'a_red = {a_green_org}')
print(f'b_green = {b_green_org}')
print(f'a_blue = {a_blue_org}')
print(f'b_blue = {a_blue_org}')
beta_parameters_ort = (a_red_org, b_red_org, a_green_org, b_green_org, a_blue_org, b_blue_org)
brightness, contrast = BB.birghtness_contrast_from_beta_parameters(beta_parameters_org)
print('Brightness and Contrast of original image:')
print('Brightness = {brightness}')
print('Contrast = {contrast}')
  
beta_parameters_mod = (a_red, b_red,a_green, b_green,a_blue, b_blue)   
image_modified = BB.modify_image(image, beta_parameters_mod)
image_modified.show()

brightness_mod, contrast_mod = BB.birghtness_contrast_from_beta_parameters(beta_parameters_mod)
print('Brightness and Contrast of modified image:')
print('Brightness = {brightness_mod}')
print('Contrast = {contrast_mod}')
```
### How to aproximate data by beta distribution
```python
import BrightnessBooster as BB
import numpy as np

# Задайте параметры распределения
a = 2.0  # Параметр формы (alpha)
b = 5.0  # Параметр формы (beta)
size = 1000  # Размер выборки

# Генерируем выборку из бета-распределения
data = np.random.beta(a, b, size)
a_approx, b_approx = BB.approximate_beta_distribution(data)
print(a_approx, b_approx)
```

## Licence
