##### runs under the python script






library('forecast')
library('graphics')
library('methods')

args <- commandArgs(trailingOnly = TRUE)
print(args)  #### file name  = args
# trailingOnly=TRUE means that only your arguments are returned, check:
# print(commandArgs(trailingOnly=FALSE))


#name <- as.args[1]

#print name


folder='/home/pramod/Desktop/analytics/'






path=paste(folder,args,sep="")

print(path)

y= read.csv(path, sep=',')

x=y[,2]
print(x)
print('\n')

pre=croston(x,h=5)

print(pre)

fileConn<-file("output.txt")
writeLines(paste(pre[1]), fileConn)
close(fileConn)




png(filename="/home/pramod/Desktop/analytics/forecastdjango/static/forecast/croston2.png")
plot(pre)
dev.off()




