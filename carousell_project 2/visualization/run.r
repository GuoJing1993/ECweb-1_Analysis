library(shiny)
library(ggplot2)
library(wordcloud2)
library(markdown)
library(scales)
library(markdown)
library(rPython)

#Data Acquisition
for (i in c(1:32)){
  script=paste("cd /Users/peternapolon/Desktop/carousell_project/product_crawler/carousell/carousell/spiders/;scrapy crawl ",i," -o ",i,".csv",sep='')
  system(script)
  Sys.sleep(10)
}

#Data Cleaning and Transformation
source("/Users/peternapolon/desktop/carousell_project/analysis/Data Cleaning+Transformation.R")

#Run the App
mydata=read.csv('/Users/peternapolon/desktop/carousell_project/analysis/data/test.csv',sep=',', header=T, comment.char = '@',encoding="big5")
mydata = mydata[, c("item_id","post_time","post_days_to_now","post_weeks_to_now","item_location","item_category","item_title","title_words_num","title_words_num_range","item_description","description_num","description_num_range","item_likes","avg_weekly_likes","item_price","item_label","item_truck_able","item_face_able","item_sellerName")]
Sys.setlocale("LC_ALL", "zh_TW.UTF-8")
Sys.setlocale("LC_TIME", "C")
runApp("/Users/peternapolon/desktop/carousell_project/visualization/myapp_1")
