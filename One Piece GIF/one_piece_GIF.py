import imageio.v3 as iio
import os

# Defino la carpeta donde almaceno las imágenes
folder = 'images'

# Lista de los nombres de las imágenes
filenames = ['1.png', '2.png', '3.png', '4.png',
             '5.png', '6.png', '7.png', '8.png',
             '9.png', '10.png', '11.png', '12.png',
             '13.png', '14.png', '15.png', '16.png',
             '17.png']

# Aquí creo la ruta de acceso a cada imagen de la lista
filepaths = [os.path.join(folder, filename) for filename in filenames]

# Leo las imágenes
images = []
for filepath in filepaths:
    images.append(iio.imread(filepath))

# Creo el GIF
gif_path = 'one_piece.gif'
iio.imwrite(gif_path, images, duration=200, loop=0)
