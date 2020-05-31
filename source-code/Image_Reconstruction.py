import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import imageio
import time as t

s = t.time()
#Enter sample percentage
sample_rate = 0.25 #5% sampling if '0.05'

#Enter image adress
Xorig = img.imread('elephants.jpg')

X = Xorig
ny,nx,nz = X.shape
print("Shape of Image: ",X.shape)
# Randomly selecting samples
k = round(nx * ny * sample_rate) # 50% sample
ri = np.random.choice(nx * ny, k, replace=False) # random sample of indices
print("Number of samples: ",k)
b = X.T.flat[ri]
Xm = np.zeros(X.shape)
for i in range(nz):
    Xm[:,:,i].T.flat[ri] = X[:,:,i].T.flat[ri]
X1 = np.zeros(X.shape)
for i in range(nz):
    X1[:,:,i].T.flat[ri] = X[:,:,i].T.flat[ri]

condi = True
count = 1
while condi:
    X2=np.zeros((ny+2,nx+2,nz))
    for i in range(nz):
        X2[:,:,i] = np.pad(X1[:,:,i], [(1, 1), (1, 1)], mode='constant')
    X3 = X1
    zero_num = (X1 == 0).astype(int)
    if 0 < np.sum(zero_num):
        print('Iteration number: ', count)
        count += 1
        for channel in range(nz):
            for i in range(len(X2[:,0,channel])-2):
                for j in range(len(X2[0,:,channel])-2):
                    r = i+1
                    c = j+1
                    if (X2[r,c,channel] == 0):
                        mean = 0
                        k = 0
                        if (X2[r-1,c-1,channel] != 0):
                            mean += X2[r-1,c-1,channel]
                            k += 1
                        if (X2[r-1,c,channel] != 0):
                            mean += X2[r-1,c,channel]
                            k += 1
                        if (X2[r-1,c+1,channel] != 0):
                            mean += X2[r-1,c+1,channel]
                            k += 1
                        if (X2[r,c-1,channel] != 0):
                            mean += X2[r,c-1,channel]
                            k += 1
                        if (X2[r,c+1,channel] != 0):
                            mean += X2[r,c+1,channel]
                            k += 1
                        if (X2[r+1,c-1,channel] != 0):
                            mean += X2[r+1,c-1,channel]
                            k += 1
                        if (X2[r+1,c,channel] != 0):
                            mean += X2[r+1,c,channel]
                            k += 1
                        if (X2[r+1,c+1,channel] != 0):
                            mean += X2[r+1,c+1,channel]
                            k += 1
                        if (k != 0):
                            mean = mean / k
                            X1[i,j,channel] = mean
    else:
        condi=False

Execution_time = int(np.round(t.time()-s))
print('Execution time: {} sec'.format(Execution_time))

Xm[Xm == 0] = 255
fig, axs = plt.subplots(1, 3,figsize=(15,10))
axs[0].imshow(X)
#for jpg file type
axs[1].imshow((Xm).astype(np.uint8))
axs[2].imshow((X1).astype(np.uint8))
#for png type file
#axs[1].imshow((Xm))
#axs[2].imshow((X1))
axs[0].set_title('Orignal')
axs[1].set_title('{}% sampled.jpg'.format(sample_rate*100))
axs[2].set_title('Output')

imageio.imwrite('input_image.jpg', X)
imageio.imwrite('{}%_input.jpg'.format(sample_rate*100), Xm)
imageio.imwrite('Output.jpg', X1)