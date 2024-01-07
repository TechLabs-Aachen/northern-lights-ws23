from nasaomnireader import omnireader
import datetime

#Create a time window
sTimeIMF = datetime.datetime(2023,12,1)
eTimeIMF = datetime.datetime(2023,12,3)

#omni_interval is a dictionary-like object
#that you can use to get the omni data for
#any variable as a numpy array
#for any span of time
omniInt = omnireader.omni_interval(sTimeIMF,eTimeIMF,'5min')
t = omniInt['Epoch'] #datetime timestamps
By,Bz = omniInt['BY_GSM'],omniInt['BZ_GSM']