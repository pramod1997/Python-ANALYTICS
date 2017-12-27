#import rpy2.robjects as robjects

from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse 






import subprocess
 

def callcroston(request):

	subprocess.call("Rscript   ", shell=True )
    return HttpResponse("Hello,. You just executed croston check the file.")




