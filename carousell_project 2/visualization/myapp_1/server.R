library(shiny)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
    
    acquiredata <- eventReactive(input$scrapy, {
      python.load("/Users/peternapolon/desktop/hello.py")
    })
    
    output$trendplot <- renderPlot(
      width = 1200,
      height = 400,units="px",
      {
      q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
      if (input$timerange=='7-days'){
        weeks=1
        days=weeks*7
        q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
        new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
        length(new$item_price[new$post_weeks_to_now<=weeks & new$item_category=='luxury-20'])
        ggplot(data=new, aes(new$post_days_to_now,color=new$item_category)) +
          geom_line(stat='count',position='dodge') + 
          geom_point(stat='count',position='dodge') +
          geom_text(stat='count', aes(label=round(..count..)),size=4,vjust = -0.5,alpha=0.5) +
          scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
          scale_x_reverse(breaks=1:days,labels=as.Date(as.integer(as.Date('2016-09-24'))-c(1:days)+1, origin = "1970-01-01")) +
          labs(title='# of items posted in given time range') +
          labs(x="Time", y='Count') +
          theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
          theme(axis.title = element_text(color="darkgray", face="bold", size=13))
      }
      else if (input$timerange=='14-days'){
        weeks=2
        days=weeks*7
        q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
        new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
        ggplot(data=new, aes(new$post_days_to_now,color=new$item_category)) +
          geom_line(stat='count',position='dodge') + 
          geom_point(stat='count',position='dodge') + 
          geom_text(stat='count', aes(label=round(..count..)),size=4,vjust = -0.5,alpha=0.5) +
          scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
          scale_x_reverse(breaks=1:days,labels=as.Date(as.integer(as.Date('2016-09-24'))-c(1:days)+1, origin = "1970-01-01"))+
          labs(title='# of items posted in given time range') +
          labs(x="Time", y='Count') +
          theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
          theme(axis.title = element_text(color="darkgray", face="bold", size=13))
        
      }
      else if (input$timerange=='1-month'){
        weeks=5
        days=weeks*7
        q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
        new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
        ggplot(data=new, aes(new$post_weeks_to_now,color=new$item_category)) +
          geom_line(stat='count',position='dodge') +
          geom_point(stat='count',position='dodge') + 
          geom_text(stat='count', aes(label=round(..count..)), vjust=1,hjust=2,size=5,alpha=0.5) +
          scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
          scale_x_reverse(breaks=1:weeks,labels=as.Date(as.integer(as.Date('2016-09-24'))-7*c(1:weeks)+7, origin = "1970-01-01"))+
          labs(title='# of items posted in given time range') +
          labs(x="Time", y='Count') +
          theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
          theme(axis.title = element_text(color="darkgray", face="bold", size=13))
      }
      else{
        weeks=10
        days=weeks*7
        q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
        new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
        ggplot(data=new, aes(new$post_weeks_to_now,color=new$item_category)) +
          geom_line(stat='count',position='dodge') +
          geom_point(stat='count',position='dodge') + 
          geom_text(stat='count', aes(label=round(..count..)),size=4,vjust = -0.5,alpha=0.5) +
          scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
          scale_x_reverse(breaks=1:weeks,labels=as.Date(as.integer(as.Date('2016-09-24'))-7*c(1:weeks)+7, origin = "1970-01-01"))+
          labs(title='# of items posted in given time range') +
          labs(x="Time", y='Count') +
          theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
          theme(axis.title = element_text(color="darkgray", face="bold", size=13))
      }
    })
    
    trenddata <- eventReactive(input$tsubmit, {
      input$tmimerange
      input$tmeasure
    })
    
    output$trendmplot <- renderPlot(
      width = 1200,
      height = 400,units="px",
      {
        input$tsubmit
        q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
        if (isolate(input$tmimerange)=='7-days'){
          weeks=1
          days=weeks*7
          q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
          new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
          isolate(ggplot(data=new, aes(y=isolate(new[input$tmeasure]),x=new$post_days_to_now,color=new$item_category)) +
            stat_summary(fun.y = "mean", geom='point',position='dodge') + 
            stat_summary(fun.y = "mean", geom='line',position='dodge') + 
            stat_summary(aes(label=round(..y..,0)), fun.y=mean, geom="text",size=4,vjust = -0.5,alpha=0.5)+
            scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
            scale_x_reverse(breaks=1:days,labels=as.Date(as.integer(as.Date('2016-09-24'))-c(1:days)+1, origin = "1970-01-01")) +
            labs(title=paste(input$tmeasure,' ',sep=" ")) +
            labs(x="Time", y=input$tmeasure) +
            theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
            theme(axis.title = element_text(color="darkgray", face="bold", size=13)))
          }
        else if (isolate(input$tmimerange)=='14-days'){
          weeks=2
          days=weeks*7
          q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
          new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
          isolate(ggplot(data=new, aes(y=isolate(new[input$tmeasure]),x=new$post_days_to_now,color=new$item_category)) +
            stat_summary(fun.y = "mean", geom='point',position='dodge') + 
            stat_summary(fun.y = "mean", geom='line',position='dodge') +
              stat_summary(aes(label=round(..y..,0)), fun.y=mean, geom="text",size=4,vjust = -0.5,alpha=0.5)+
            scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
            scale_x_reverse(breaks=1:days,labels=as.Date(as.integer(as.Date('2016-09-24'))-c(1:days)+1, origin = "1970-01-01")) +
            labs(title=paste(input$tmeasure,' ',sep=" ")) +
            labs(x="Time", y=input$tmeasure) +
            theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
            theme(axis.title = element_text(color="darkgray", face="bold", size=13)))
          }
        else if (isolate(input$tmimerange=='1-month')){
          weeks=5
          days=weeks*7
          q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
          new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
          isolate(ggplot(data=new, aes(y=isolate(new[input$tmeasure]),x=new$post_weeks_to_now,color=new$item_category)) +
            stat_summary(fun.y = "mean", geom='point',position='dodge') + 
            stat_summary(fun.y = "mean", geom='line',position='dodge') + 
            stat_summary(aes(label=round(..y..,0)), fun.y=mean, geom="text",size=4,vjust = -0.5,alpha=0.5)+
            scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
            scale_x_reverse(breaks=1:weeks,labels=as.Date(as.integer(as.Date('2016-09-24'))-7*c(1:weeks)+7, origin = "1970-01-01")) +
            labs(title=paste(input$tmeasure,' ',sep=" ")) +
            labs(x="Time", y=input$tmeasure) +
            theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
            theme(axis.title = element_text(color="darkgray", face="bold", size=13)))
        }
        else{
          weeks=10
          days=weeks*7
          q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
          new=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2] &mydata$post_weeks_to_now<=weeks ,select=c(1:19))
          isolate(ggplot(data=new, aes(y=new[isolate(input$tmeasure)],x=new$post_weeks_to_now,color=new$item_category)) +
            stat_summary(fun.y = "mean", geom='point',position='dodge') + 
            stat_summary(fun.y = "mean", geom='line',position='dodge') +
            stat_summary(aes(label=round(..y..,0)), fun.y=mean, geom="text",size=4,vjust = -0.5,alpha=0.5)+  
            scale_color_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A")) + 
            scale_x_reverse(breaks=1:weeks,labels=as.Date(as.integer(as.Date('2016-09-24'))-7*c(1:weeks)+7, origin = "1970-01-01")) +
            labs(title=paste(input$tmeasure,' ',sep=" ")) +
            labs(x="Time", y=input$tmeasure) +
            theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
            theme(axis.title = element_text(color="darkgray", face="bold", size=13)))
        }
      })

    output$hotkeywordplot <- wordcloud2::renderWordcloud2(
      {
      path=paste('/Users/peternapolon/desktop/carousell_project/analysis/data/',input$hotcategory,'_words_1weeks.csv',sep = "")
      x=read.csv(path,header=F)
      x=x[1:100,]
      wordcloud2(x, size=1, shape='circle')
      })

    output$hotkeywordtext <- renderUI({
      path=paste('/Users/peternapolon/desktop/carousell_project/analysis/data/',input$hotcategory,'_words_1weeks.csv',sep = "")
      x=read.csv(path,header=F)
      l1 = "<h4>Hottest keywords in this week: </h4>"
      l2 = paste(as.character(x$V1[1]),': ',round(x$V2[1]/sum(x$V2)*100,digits = 0),'%')
      l3 = paste(as.character(x$V1[2]),': ',round(x$V2[2]/sum(x$V2)*100,digits = 0),'%')
      l4 = paste(as.character(x$V1[3]),': ',round(x$V2[3]/sum(x$V2)*100,digits = 0),'%')
      l5 = paste(as.character(x$V1[4]),': ',round(x$V2[4]/sum(x$V2)*100,digits = 0),'%')
      l6 = paste(as.character(x$V1[5]),': ',round(x$V2[5]/sum(x$V2)*100,digits = 0),'%')
      l7 = paste(as.character(x$V1[6]),': ',round(x$V2[6]/sum(x$V2)*100,digits = 0),'%')
      l8 = paste(as.character(x$V1[7]),': ',round(x$V2[7]/sum(x$V2)*100,digits = 0),'%')
      l9 = paste(as.character(x$V1[8]),': ',round(x$V2[8]/sum(x$V2)*100,digits = 0),'%')
      l10 = paste(as.character(x$V1[9]),': ',round(x$V2[9]/sum(x$V2)*100,digits = 0),'%')
      l11 = paste(as.character(x$V1[10]),': ',round(x$V2[10]/sum(x$V2)*100,digits = 0),'%')
      HTML(paste(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11, sep = '<br/>'))
    })
    
    
    output$priceplot <- renderPlot(
      width = 675,
      height = 400,units="px",
      {
      if(input$pcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$pcategory,select=c(1:19))
      }
      q=quantile(newdata$item_price, probs=c(5,95)/100, na.rm = T)
      x=newdata$item_price[!is.na(newdata$item_price) & newdata$item_price>=q[1] & newdata$item_price<=q[2]]
      x=as.data.frame(x)
      #plot(density(mydata$item_price[mydata$item_category==input$pcategory & !is.na(mydata$item_price) & mydata$item_price>=q[1]&mydata$item_price<=q[2]]),
      #     main=input$pcategory,
      #     ylab="Density",
      #     xlab="Price")
      #hist(mydata$item_price[mydata$item_category==input$pcategory & !is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2]], 
      #     breaks=input$bins,
      #     main=input$pcategory,
      #     ylab="Counts",
      #     xlab="Price")
      ggplot(data=x, aes(x),width=1000) + 
        geom_histogram(binwidth=input$range,col='white', boundary=0, fill='#004B97', alpha=0.5) +
        stat_bin(binwidth=input$range, origin=0, geom='text', aes(label=ifelse(round(..count../sum(..count..)*100)>0, paste(as.character(round(..count../sum(..count..)*100)),'%',''), "")), vjust=0, closed = c("right"),alpha=0.5) +
        labs(title=paste(input$pcategory,'',sep="")) +
        labs(x="Price", y="# of Items") +
        theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
        theme(axis.title = element_text(color="darkgray", face="bold", size=13)) 
    })
    
    output$pricetext <- renderUI({
      if(input$pcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$pcategory,select=c(1:19))
      }
      q=quantile(newdata$item_price, probs=c(5,95)/100, na.rm = T)
      x=newdata$item_price[!is.na(newdata$item_price) & newdata$item_price>=q[1] & newdata$item_price<=q[2]]
      l1="<h4>The summary of this category: </h4>"
      l2=paste('Min: ',summary(x)[1])
      l3=paste('1st Qu: ',summary(x)[2])
      l4=paste('Median: ',summary(x)[3])   
      l5=paste('Mean: ',summary(x)[4])
      l6=paste('3rd Qu: ',summary(x)[5])
      l7=paste('Max: ',summary(x)[6])
      HTML(paste(l1,l2,l3,l4,l5,l6,l7, sep = '<br/>'))
    })  
    
    daydata <- eventReactive(input$dsubmit, {
      input$fromdate
      input$todate
    })

    output$dayplot <- renderPlot(
      width = 675,
      height = 400,units = "px",
      {
      input$dsubmit
      if(input$dcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$dcategory,select=c(1:19))
      }
      t = as.numeric(newdata$post_days_to_now)
      t = as.data.frame(table(t))
      t$t = as.numeric(t$t)
      long=isolate(as.Date('2016-09-24')-as.Date(input$fromdate))
      long=as.numeric(long)
      short=isolate(as.Date('2016-09-24')-as.Date(input$todate))
      short=as.numeric(short)
      x=rep('darkgray',length(t$t))
      x[short:long]='#004B97'
      #barplot(table(t), col = x, xlim = c(0,60),main = 'Days from 2016-09-24\n(Only show recent 2 month data)', xlab = 'Days', ylab = '# of items')
      ggplot(t,aes(t,Freq)) + 
        geom_bar(stat="identity", fill=x[1:60], alpha=0.5) +
        xlim(0,60) +
        labs(title=paste(input$dcategory,'',sep="")) +
        labs(x="Days from 2016.09.24", y="# of Items") +
        theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
        theme(axis.title = element_text(color="darkgray", face="bold", size=13)) 
    })  
    
    output$daytext <- renderUI({
      if(input$pcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$pcategory,select=c(1:19))
      }
      input$dsubmit
      t = as.numeric(newdata$post_days_to_now)
      long=isolate(as.Date('2016-09-24')-as.Date(input$fromdate))
      long=as.numeric(long)
      short=isolate(as.Date('2016-09-24')-as.Date(input$todate))
      short=as.numeric(short)
      l1 = "<h4>There are almost </h4>"
      l2 = paste('<h1><b>',as.character(round(sum(table(t)[short:long])/sum(table(t))*100,digits=2)),'%','</b></h2>')
      l3 = "<h4>items in given date range.</h4>"
      HTML(paste(l1,l2,l3, sep = '<br/>'))
    })
    
    output$locationplot <- renderPlot(
      width = 675,
      height = 400,units = "px",
      {
      #a=table(mydata$item_location[mydata$item_category==input$lcategory])
      #a=sort(a, decreasing = T)
      #s=as.data.frame(a[0:10])
      #t=as.vector(substr(s$Var1,1,3))
      #barplot(rev(sort(table(mydata$item_location[mydata$item_category==input$lcategory])))[10:1],horiz =T,family = "SimSun",names.arg = rev(t),cex.names=0.7,las=1,space=0.5)
      if(input$lcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$lcategory,select=c(1:19))
      }
      title("Top 10 cities of given category of items")
      a=rev(table(newdata$item_location))
      a=sort(a, decreasing = F)
      a=as.data.frame(tail(a,10))
      a$Var1=substr(a$Var1,1,3)
      ggplot(a,aes(a$Var1,a$Freq)) +
        labs(title=paste(input$lcategory,'',sep="")) +
        labs(x="# of items", y="Area") +
        geom_bar(stat="identity", width = 0.5, fill='#004B97', alpha=0.5) +
        coord_flip() +
        theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
        theme(axis.title = element_text(color="darkgray", face="bold", size=13)) +
        theme(axis.text = element_text(color="#666666", family = 'SimSun', size=8))
    })
  
    output$locationtext <- renderUI({
      a=table(mydata$item_location[mydata$item_category==input$lcategory])
      a=sort(a, decreasing = T)
      s=as.data.frame(a[0:10])
      t=as.vector(substr(s$Var1,1,3))
      l1 = "<h4>The Ratio of Top10 Locations of this category: </h4>"
      l2 = paste(as.character(s$Var[1]),': ',round(a[1]/sum(a)*100,digits = 0),'%')
      l3 = paste(as.character(s$Var[2]),': ',round(a[2]/sum(a)*100,digits = 0),'%')
      l4 = paste(as.character(s$Var[3]),': ',round(a[3]/sum(a)*100,digits = 0),'%')
      l5 = paste(as.character(s$Var[4]),': ',round(a[4]/sum(a)*100,digits = 0),'%')
      l6 = paste(as.character(s$Var[5]),': ',round(a[5]/sum(a)*100,digits = 0),'%')
      l7 = paste(as.character(s$Var[6]),': ',round(a[6]/sum(a)*100,digits = 0),'%')
      l8 = paste(as.character(s$Var[7]),': ',round(a[7]/sum(a)*100,digits = 0),'%')
      l9 = paste(as.character(s$Var[8]),': ',round(a[8]/sum(a)*100,digits = 0),'%')
      l10 = paste(as.character(s$Var[9]),': ',round(a[9]/sum(a)*100,digits = 0),'%')
      l11 = paste(as.character(s$Var[10]),': ',round(a[10]/sum(a)*100,digits = 0),'%')
      HTML(paste(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11, sep = '<br/>'))
    })  

    output$wordcloud <- wordcloud2::renderWordcloud2({
      path=paste('/Users/peternapolon/desktop/carousell_project/analysis/data/',input$kcategory,'_words.csv',sep = "")
      x=read.csv(path,header=F)
      x=subset(x,V2>input$mf,select = c(V1,V2))
      wordcloud2(x, size=1, shape='circle')
    })
    
    output$titletext <- renderUI({
      path=paste('/Users/peternapolon/desktop/carousell_project/analysis/data/',input$kcategory,'_words.csv',sep = "")
      x=read.csv(path,header=F)
      x=subset(x,V2>25,select = c(V1,V2))
      l1 = "<h4>Most frequent keywords of item titles of given category: </h4>"
      l2 = paste(as.character(x$V1[1]),': ',round(x$V2[1]/sum(x$V2)*100,digits = 2),'%')
      l3 = paste(as.character(x$V1[2]),': ',round(x$V2[2]/sum(x$V2)*100,digits = 2),'%')
      l4 = paste(as.character(x$V1[3]),': ',round(x$V2[3]/sum(x$V2)*100,digits = 2),'%')
      l5 = paste(as.character(x$V1[4]),': ',round(x$V2[4]/sum(x$V2)*100,digits = 2),'%')
      l6 = paste(as.character(x$V1[5]),': ',round(x$V2[5]/sum(x$V2)*100,digits = 2),'%')
      l7 = paste(as.character(x$V1[6]),': ',round(x$V2[6]/sum(x$V2)*100,digits = 2),'%')
      l8 = paste(as.character(x$V1[7]),': ',round(x$V2[7]/sum(x$V2)*100,digits = 2),'%')
      l9 = paste(as.character(x$V1[8]),': ',round(x$V2[8]/sum(x$V2)*100,digits = 2),'%')
      l10 = paste(as.character(x$V1[9]),': ',round(x$V2[9]/sum(x$V2)*100,digits = 2),'%')
      l11 = paste(as.character(x$V1[10]),': ',round(x$V2[10]/sum(x$V2)*100,digits = 2),'%')
      HTML(paste(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11, sep = '<br/>'))
    })
    
    output$kdwordcloud <- wordcloud2::renderWordcloud2({
      path=paste('/Users/peternapolon/desktop/carousell_project/analysis/data/',input$kdcategory,'_contents.csv',sep = "")
      x=read.csv(path,header=F)
      x=subset(x,V2>=input$kdmf &V2<=input$kdmaf,select = c(V1,V2))
      wordcloud2(x, size=1, shape='circle')
    })
    
    output$desriptiontext <- renderUI({
      path=paste('/Users/peternapolon/desktop/carousell_project/analysis/data/',input$kdcategory,'_contents.csv',sep = "")
      x=read.csv(path,header=F)
      sum_=sum(x$V2)
      x=subset(x,V2>=input$kdmf &V2<=input$kdmaf,select = c(V1,V2))
      l1 = "<h4>Most frequent keywords of all item description of given category: </h4>"
      l2 = paste(as.character(x$V1[1]),': ',round(x$V2[1]/sum_*100,digits = 2),'%')
      l3 = paste(as.character(x$V1[2]),': ',round(x$V2[2]/sum_*100,digits = 2),'%')
      l4 = paste(as.character(x$V1[3]),': ',round(x$V2[3]/sum_*100,digits = 2),'%')
      l5 = paste(as.character(x$V1[4]),': ',round(x$V2[4]/sum_*100,digits = 2),'%')
      l6 = paste(as.character(x$V1[5]),': ',round(x$V2[5]/sum_*100,digits = 2),'%')
      l7 = paste(as.character(x$V1[6]),': ',round(x$V2[6]/sum_*100,digits = 2),'%')
      l8 = paste(as.character(x$V1[7]),': ',round(x$V2[7]/sum_*100,digits = 2),'%')
      l9 = paste(as.character(x$V1[8]),': ',round(x$V2[8]/sum_*100,digits = 2),'%')
      l10 = paste(as.character(x$V1[9]),': ',round(x$V2[9]/sum_*100,digits = 2),'%')
      l11 = paste(as.character(x$V1[10]),': ',round(x$V2[10]/sum_*100,digits = 2),'%')
      HTML(paste(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11, sep = '<br/>'))
    })
    
    output$aktplot <- renderPlot(
      width = 400,
      height = 400,units="px",
      {
      if(input$aktcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$aktcategory,select=c(1:19))
      }
      q=quantile(newdata$title_words_num, probs=c(5,95)/100, na.rm = T)
      tmp=subset(newdata, title_words_num>=q[1] & title_words_num<=q[2], select=c(avg_weekly_likes, title_words_num))
      tmp$cutrange=cut(tmp$title_words_num, input$aktbin, include.lowest = T)
      y=tapply(tmp$avg_weekly_likes,tmp$cutrange,mean)
      plot(y,ylab = 'Avg Weekly Likes',xlab = 'Range of title length',main='Avg Weekly Likes by title length range',xaxt='n',ylim=c(1,4))
      text(y,label=round(y,digits = 2),pos =3)
      lines(y)
      axis(2,1:5)
      axis(1,1:input$aktbin,levels(tmp$cutrange),cex.axis=1)
      
    })
    
    output$akdplot <- renderPlot(
      width = 400,
      height = 400,units="px",
      {
      if(input$akdcategory=="All"){
        newdata=mydata
      }
      else{
        newdata=subset(mydata,item_category==input$akdcategory,select=c(1:19))
      }      
      q=quantile(newdata$description_num, probs=c(5,95)/100, na.rm = T)
      tmp=subset(newdata, description_num>=q[1] & description_num<=q[2] , select=c(avg_weekly_likes, description_num))
      tmp$cutrange=cut(tmp$description_num, input$akdbin, include.lowest = T)
      y=tapply(tmp$avg_weekly_likes,tmp$cutrange,mean)
      plot(y,ylab = 'Avg Weekly Likes',xlab = 'Range of description length',main='Avg Weekly Likes by description length range',xaxt='n',ylim=c(1,4))
      text(y,label=round(y,digits = 2),pos =3)
      lines(y)
      axis(2,1:5)
      axis(1,1:input$akdbin,levels(tmp$cutrange),cex.axis=1)
      
    })

    output$labelplot <- renderPlot(
      width = 675,
      height = 400,units="px",
      {
      q=quantile(mydata$item_price, probs=c(5,95)/100, na.rm = T)
      tmp=subset(mydata,!is.na(mydata$item_price) & mydata$item_price>=q[1] & mydata$item_price<=q[2],select=c(1:19))
      if (input$lmeasure != 'Count'){
        ggplot(data=tmp, aes(x=tmp$item_label, y=tmp[input$lmeasure], fill=tmp$item_category)) +
        labs(title=paste(input$lmeasure,'',sep="")) +
        stat_summary(fun.y = "mean", geom='bar', position='dodge',alpha=0.5) +
        scale_fill_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A"))+
        labs(title=paste(input$lmeasure,' ',sep=" ")) +
        labs(x="Item_labels", y=input$lmeasure) +
        theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
        theme(axis.title = element_text(color="darkgray", face="bold", size=13))
        
      }
      else{
        ggplot(data = tmp, aes(tmp$item_label, fill=tmp$item_category)) +
          geom_bar(stat='count', position='dodge',alpha=0.5, width = 0.5) +
          labs(title=paste(input$lmeasure,'',sep="")) +
          scale_fill_manual(values=c("#01814A","#9F5000", "#004B97", "#743A3A"))+
          theme(plot.title = element_text(color="#666666", face="bold", size=20, hjust=0.5)) +
          theme(axis.title = element_text(color="darkgray", face="bold", size=13))
      }
      
    })
    
})