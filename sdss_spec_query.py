import numpy as np
import os
from astroquery.sdss import SDSS
from astropy import coordinates as coords
from astropy import units as u
import warnings
warnings.filterwarnings("ignore")

name=np.loadtxt('SDSS_GRG.txt', unpack=True, usecols=[0], dtype='str')
ra,dec=np.loadtxt('SDSS_GRG.txt', unpack=True, usecols=[2,3])
for i in range(len(ra)):
	if not os.path.exists('%s.gif' %name[i]) or os.stat('%s.gif' %name[i]).st_size <10240:
		print(name[i])
		pos = coords.SkyCoord(float(ra[i])*u.deg, float(dec[i])*u.deg,frame='fk5')
		xid = SDSS.query_region(pos, spectro=True, radius=3. * u.arcsec, data_release=17)
		if xid is not None :
			url='http://skyserver.sdss.org/dr17/en/get/SpecById.ashx?id=%d' %(xid['specobjid'][0])
			os.system('wget %s -O %s.gif' %(url,name[i]))
		else:
			print('No SDSS spectrum')
