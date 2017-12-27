

import subprocess
#import matplotlib.pyplot as plt

 


#plt.show('/home/pramod/Desktop/plot.png')

import matplotlib.pyplot as plt
import matplotlib.image as mpimg




def croston(fname):



	y=fname  ## this is the file name 


	#### able to pass inline arguement here 



	subprocess.call("Rscript /home/pramod/Desktop/analytics/forecast/croston.r "+ y, shell=True )   ## use single quotation
	#image = mpimg.imread("/home/pramod/Desktop/plot.png")
	#plt.imshow(image)
	#plt.show()


