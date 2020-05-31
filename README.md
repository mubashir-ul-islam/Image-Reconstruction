# Image-Reconstruction using python

This Repository contain python code to reconstruct image from just small number of samples from original images. Below given examples show how accurate we were getting results, just from **5%** of the orignal images we were able to construct a pressentable image. 

Python file **`Image_Reconstruction.py`** contains the code for the reconstruction of the image.

## Requirements:
`Python 2 or 3`\
`Numpy`\
`matplotlib`\
`imageio`

## How to run code:
If you want to run this code for your own image then you need to place the link of image inside the file **`Image_Reconstruction.py`** and replace **`'elephants.jpg'`** with the link of your image and also need to specify how much data you want from the original image to do this replace **0.25** from `sample_rate = 0.25` and put your desired value (0.25 means 25%). 

Running the code will save two images, one `25.0%_input.jpg` and other `Output.jpg`. First image is the input to the program and the other is the final output.

### 10% random samples:
`10.0%_input.jpg` **----------------------------->>>>** `Output.jpg`

![image text]()
![image text]()


### 25% random samples:
`25.0%_input.jpg` **----------------------------->>>>** `Output.jpg`

![image text](https://github.com/Mubashir-ul-Islam/Image-Reconstruction/blob/master/media/25%25_input.jpg)
![image text](https://github.com/Mubashir-ul-Islam/Image-Reconstruction/blob/master/media/25%25_gif.gif)


### 50% random samples:
`50.0%_input.jpg` **----------------------------->>>>** `Output.jpg`

![image text](https://github.com/Mubashir-ul-Islam/Image-Reconstruction/blob/master/media/50%25_input.jpg)
![image text](https://github.com/Mubashir-ul-Islam/Image-Reconstruction/blob/master/media/50%25_gif.gif)
