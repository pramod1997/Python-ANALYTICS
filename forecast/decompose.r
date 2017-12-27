
library('forecast')
library('graphics')
library('methods')

args <- commandArgs(trailingOnly = TRUE)
print(args)  


folder='/home/pramod/Desktop/analytics/'


path=paste(folder,args,sep="")

print(path)

##### path for seasonal data ##### 
data=read.csv(path)

y= ts(data,freq=12)

decomposedata=decompose(y,type='multiplicative')


png(filename="/home/pramod/Desktop/analytics/forecastdjango/static/forecast/decompose.png")

plot(decomposedata)

dev.off()



trendpattern=filter(y,filter = c(1/8, 1/4, 1/4, 1/4, 1/8), sides=2)



png(filename="/home/pramod/Desktop/analytics/forecastdjango/static/forecast/decomposesmooth.png")

plot (y, type= "b", main = "moving average annual trend")
 
dev.off()

#### smoothing time series #### let us see the trend
























################ wrong not able to detect the seasonalily there ....-----methos where seasonlity is there or not #####



y= read.csv('/home/pramod/Desktop/HONORS/AirPassengers.csv')


x <- y[,2, drop=FALSE]
d <- ts(x,freq=4)

fit<- ets(d)
plot(fit)

seasonal <- !is.null(fit$seasonal)
 
print(seasonal)


