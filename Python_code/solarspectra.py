#This program shows how to read data from excel file
#The data given in this example is a Standard Solar Spectra

#import libraries
import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd


#first read the excel file using pandas
nama=['wave','irr']
df=pd.read_excel('solar_spectra.xlsx',header=0,names=nama)
#print(df['wavelength'],df['irradiance'])
x= df['wave']
y=df['irr']



mpl.plot(x,y)
mpl.xlim(0,2000)
#mpl.ylim(0.0,2.5)
mpl.xlabel('Wavelenght (nm)')
mpl.ylabel('Spectral Irradiance (W m$^{-2}$ nm$^{-1}$)')
mpl.show() 




