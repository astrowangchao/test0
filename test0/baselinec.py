import numpy as np
from astropy.io import fits
#import matplotlib.pyplot as plt

filename='nh3_11'
rawcube = fits.getdata(filename+'.fits')
rawhea = fits.getheader(filename+'.fits')
cube=np.zeros(rawcube.shape[1:])
d1=rawcube[10:50,:,:]
d2=rawcube[-40:,:,:]
for y in range(len(cube)):
    for x in range(len(cube[0])):
        cube[y,x]=(np.mean(d1[:,y,x])+np.mean(d2[:,y,x]))/2
Mhdu = fits.PrimaryHDU(rawcube-cube, rawhea)
Mhdu.writeto(filename+'_c.fits', overwrite=True)
