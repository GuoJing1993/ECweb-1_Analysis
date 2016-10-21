mydata=read.csv('/Users/peternapolon/desktop/test.csv',sep=',', header=T, comment.char = '@',encoding="big5")

#---Exploratory Research---

#Time depreciation(All)
(a=table(mydata$post_days_to_now))
plot(a)
c=c()
for (i in seq(95)){
  c=append(c,a[i]/sum(a))
}
c=round(c, digit=4)*100
c
sum(c[1:3])
sum(c[1:5])
sum(c[1:7])
sum(c[1:14])
sum(c[1:21])
sum(c[1:28])

#Time depreciation(by_categories)

#Top 10 cities of Carousell transaction places(All)
(a=table(mydata$item_location))
(a=sort(a, decreasing = T))
s=as.data.frame(a[0:10])
plot(a[0:10],xaxt='n')
t=as.vector(s$Var1)
axis(1,at=seq(1,10,1),label=FALSE,family = "SimSun")
text(1:10, par("usr")[1], labels=t, srt=20, pos=1, xpd=TRUE,family = "SimSun",cex=0.5)
title("Top 10 cities of Carousell transaction places",family = "SimSun")

#Top 10 cities of Carousell transaction places(by_categories)

#Price distribution(All)
quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
reasonable_price=mydata$item_price[mydata$item_price>=50&mydata$item_price<=9800&!is.na(mydata$item_price)]
mean(reasonable_price, na.rm=T)
median(reasonable_price, na.rm=T)
ss=summary(reasonable_price)
plot(density(reasonable_price, na.rm=T))

#Price distribution(by_categories)
p1=quantile(mydata$item_price[mydata$item_category=='women-s-fashion-4'], probs=c(5,95)/100, na.rm = T)
reasonable_price1=mydata$item_price[mydata$item_price>=p1[1]&mydata$item_price<=p1[2]&!is.na(mydata$item_price)&mydata$item_category=='women-s-fashion-4']
mean(reasonable_price1, na.rm=T)
median(reasonable_price1, na.rm=T)
summary(reasonable_price1)
lines(density(reasonable_price1, na.rm=T),col='red')

p2=quantile(mydata$item_price[mydata$item_category=='men-s-fashion-3'], probs=c(5,95)/100, na.rm = T)
reasonable_price2=mydata$item_price[mydata$item_price>=p2[1]&mydata$item_price<=p2[2]&!is.na(mydata$item_price)&mydata$item_category=='men-s-fashion-3']
mean(reasonable_price2, na.rm=T)
median(reasonable_price2, na.rm=T)
summary(reasonable_price2)
lines(density(reasonable_price2, na.rm=T),col='blue')

p3=quantile(mydata$item_price[mydata$item_category=='luxury-20'], probs=c(5,95)/100, na.rm = T)
reasonable_price3=mydata$item_price[mydata$item_price>=p3[1]&mydata$item_price<=p3[2]&!is.na(mydata$item_price)&mydata$item_category=='luxury-20']
mean(reasonable_price3, na.rm=T)
median(reasonable_price3, na.rm=T)
summary(reasonable_price3)
lines(density(reasonable_price3, na.rm=T),col='orange')

p4=quantile(mydata$item_price[mydata$item_category=='health-beauty-11'], probs=c(5,95)/100, na.rm = T)
reasonable_price4=mydata$item_price[mydata$item_price>=p4[1]&mydata$item_price<=p4[2]&!is.na(mydata$item_price)&mydata$item_category=='health-beauty-11']
mean(reasonable_price4, na.rm=T)
median(reasonable_price4, na.rm=T)
summary(reasonable_price4)
lines(density(reasonable_price4, na.rm=T),col='green')

#like_distribution(All&by_categories)
tapply(mydata$avg_weekly_likes,mydata$item_category,mean)
plot(density(mydata$avg_weekly_likes, na.rm=T),col='black')
lines(density(mydata$avg_weekly_likes[mydata$item_category=='women-s-fashion-4'], na.rm=T),col='red')
lines(density(mydata$avg_weekly_likes[mydata$item_category=='men-s-fashion-3'], na.rm=T),col='blue')
lines(density(mydata$avg_weekly_likes[mydata$item_category=='luxury-20'], na.rm=T),col='orange')
lines(density(mydata$avg_weekly_likes[mydata$item_category=='health-beauty-11'], na.rm=T),col='green')
boxplot(mydata$avg_weekly_likes~mydata$item_category, horizontal = T, axes=T)

#label_price_analysis
table(mydata$item_label)
reasonable=subset(mydata,mydata$item_price>=ss[2]&mydata$item_price<=ss[5]&!is.na(mydata$item_price))
summary(reasonable)
tapply(reasonable$item_price,reasonable$item_label,mean)

#label_likes_analysis
tapply(reasonable$avg_weekly_likes,reasonable$item_label,mean)

#label_titles_num_analysis
tapply(reasonable$title_words_num,reasonable$item_label,mean)

#label_descriptions_num_analysis
tapply(reasonable$description_num,reasonable$item_label,mean)

#faceable_likes_analysis
tapply(mydata$avg_weekly_likes,mydata$item_face_able,mean)

#truckable_likes_analysis
tapply(mydata$avg_weekly_likes,mydata$item_truck_able,mean)