#---Data_Download_Time: 2016/09/24---
Sys.setlocale("LC_ALL", "zh_TW.UTF-8")
Sys.setlocale("LC_TIME", "C")
Sys.getlocale()
sessionInfo()

#---merge_tables---
fpath1 = "/Users/peternapolon/desktop/carousell_project/analysis/raw_data/1.csv"
mydata1 = read.csv(fpath1, sep=',', header=T, comment.char = '@',encoding="big5")
summary(mydata1)
fpath2 = "/Users/peternapolon/desktop/carousell_project/analysis/raw_data/2.csv"
mydata2=read.csv(fpath2, sep=',', header=T, comment.char = '@')
summary(mydata2)
fpath3 = "/Users/peternapolon/desktop/carousell_project/analysis/raw_data/3.csv"
mydata3=read.csv(fpath3, sep=',', header=T, comment.char = '@')
summary(mydata3)
fpath4 = "/Users/peternapolon/desktop/carousell_project/analysis/raw_data/4.csv"
mydata4=read.csv(fpath4, sep=',', header=T, comment.char = '@')
summary(mydata4)
fpath5 = "/Users/peternapolon/desktop/carousell_project/analysis/raw_data/5.csv"
mydata5=read.csv(fpath5, sep=',', header=T, comment.char = '@')
summary(mydata5)
mydata=rbind(mydata1,mydata2,mydata3,mydata4,mydata5, all=T)
summary(mydata)


#---data_cleaning---

#item_id
mydata$item_id[is.na(mydata$item_id)]
mydata=mydata[complete.cases(mydata$item_id), ]

#post_time
mydata$post_time[is.na(mydata$post_time)]
mydata=mydata[complete.cases(mydata$post_time), ]
(mydata$post_time=as.Date(mydata$post_time, '%b %d, %Y'))

#item_location
is.factor(mydata$item_location)

#item_category

#item_title
mydata$item_title[is.na(mydata$item_title)]
library("stringi")
mydata$item_title[is.na(mydata$item_title)]
head(mydata$item_title)
mydata$item_title=stri_sub(mydata$item_title, 0,-13)

#item_description
mydata$item_description[is.na(mydata$item_description)]
mydata$item_description = as.character(mydata$item_description)

#item_likes

#item_label
mode(mydata$item_label)
class(mydata$item_label)
levels(mydata$item_label)= c(levels(mydata$item_label), 'No Data Provided')
mydata$item_label[is.na(mydata$item_label)|mydata$item_label==""]='No Data Provided'
head(mydata$item_label)

#item_truck_able
mydata$item_truck_able = as.factor(mydata$item_truck_able)

#item_face_able
mydata$item_face_able = as.factor(mydata$item_face_able)

#item_keywords
mode(mydata$item_keywords)
mydata$item_keywords = as.character.factor(mydata$item_keywords)

#item_sellerName
mode(mydata$item_sellerName)
mydata$item_sellerName=as.factor(mydata$item_sellerName)


#---save file---
write.csv(mydata,file='/Users/peternapolon/desktop/test.csv',row.name=T)


#---data_transformation---

#post_days_to_now
mydata$post_days_to_now=as.Date(Sys.Date())-as.Date(mydata$post_time)
mydata$item_days_to_now=NULL

#post_weeks_to_now
mydata$post_weeks_to_now = mydata$post_days_to_now/7
mydata$post_weeks_to_now = trunc(mydata$post_weeks_to_now)+1

#avg_weekly_likes
mydata$avg_weekly_likes=round(mydata$item_likes/as.numeric(mydata$post_weeks_to_now),digits = 2)

#title_words_num
mydata$title_words_num=nchar(mydata$item_title)
plot(density(mydata$title_words_num, na.rm=T))
mydata$title_words_num_range=cut(mydata$title_words_num, breaks=c(0,10,20,30,40,50,300), include.lowest = T)
table(mydata$title_words_num_range)
(a=tapply(mydata$avg_weekly_likes,mydata$title_words_num,mean))
plot(a)
(b=tapply(mydata$avg_weekly_likes,mydata$title_words_num_range,mean))
plot(b)
c=tapply(mydata$avg_weekly_likes,mydata$item_category,mean)

#description_num
mydata$description_num=nchar(mydata$item_description)
plot(density(mydata$description_num, na.rm=T))
mydata$description_num_range=cut(mydata$description_num, breaks=c(0,30,60,90,120,150,300), include.lowest = T)
table(mydata$description_num_range)
(a=tapply(mydata$avg_weekly_likes,mydata$description_num,mean))
plot(a)
(b=tapply(mydata$avg_weekly_likes,mydata$description_num_range,mean))
plot(b)


#---save file---
detach(mydata)
mydata = mydata[, c("item_id","post_time","post_days_to_now","post_weeks_to_now","item_location","item_category","item_title","title_words_num","title_words_num_range","item_description","description_num","description_num_range","item_likes","avg_weekly_likes","item_price","item_label","item_truck_able","item_face_able","item_sellerName")]
write.csv(mydata,file='/Users/peternapolon/desktop/carousell_project1/analysis/data/test_20161013.csv',row.name=T)