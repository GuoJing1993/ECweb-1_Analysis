library(shiny)

shinyUI(navbarPage("Carousell Analytics Dashboard",
  tabPanel("Trend",
    actionButton("scrapy", "Acquire Data"),
    titlePanel("# of items posted in rencent 2 months"),               
    hr(),
    fluidRow(
      column(2,
        wellPanel(
          selectInput("timerange", "Time Range:", choices=c('7-days','14-days','1-month','2-month'), selected='7-days')
        )),
      column(10,
        mainPanel(
          plotOutput("trendplot")
        ))
      ),
    br(),
    titlePanel("KPIs of items posted in rencent 2 months"),               
    hr(),
    fluidRow(
      column(2,
             wellPanel(
               selectInput("tmimerange", "Time Range:", choices=c('7-days','14-days','1-month','2-month'), selected='7-days'),
               selectInput("tmeasure", "Choose indicators you're interested", choices=c('title_words_num','description_num','avg_weekly_likes','item_price','item_truck_able','item_face_able'), selected='item_price'),
               actionButton("tsubmit", "Enter")
             )),
      column(10,
             mainPanel(
               plotOutput("trendmplot")
             ))
      ),
    br(),
    titlePanel("Hot keywords in this week"),
    hr(),
    fluidRow(
      column(3,
             wellPanel(
               selectInput("hotcategory", "Category:", choices=c(levels(mydata$item_category)), selected='luxury-20')
             )),
      column(6,
             mainPanel(
               wordcloud2Output("hotkeywordplot",width="520px")
             )),
      column(3,
             mainPanel(
               htmlOutput("hotkeywordtext")
             ))
    )
  ),
                   
  tabPanel("Detail",
    actionButton("scrapy", "Acquire Data"),
    titlePanel("Price Distribution"),
    hr(),
    fluidRow(
      column(3,
        wellPanel(
          selectInput("pcategory", "Category:", choices=c(levels(mydata$item_category),'All'), selected='luxury-20'),
          br(),
          sliderInput("range","Choose your price range:",min = 100,max = 2000,value = 300,step=100),
          helpText("Data Downloaded At 2016-09-23 From Carousell.com.tw")
        )
      ),
      column(6,
        mainPanel(
          plotOutput("priceplot")
        )
      ),
      column(3,
          htmlOutput("pricetext",width="500px")
      )
    ),
    
    br(),
    
    titlePanel("Days Posted Distribution"),
    
    hr(),
    
    fluidRow(
      column(3,
        wellPanel(
          selectInput("dcategory", "Category:", choices=c(levels(mydata$item_category),'All'), selected='luxury-20'),
          strong("Please Select Date Range: "),
          helpText("(Every date represents beginning of the day)"),
          dateInput("fromdate", "From: ", value = "2016-09-24"),
          dateInput("todate", "To: ", value = "2016-09-24"),
          actionButton("dsubmit", "Submit")
        )
      ),
      column(6,
        mainPanel(
          plotOutput("dayplot")
        )
      ),
      column(3,
          htmlOutput("daytext")
      )
    ),
  
    p('\n'),
    
    titlePanel("Location Info"),
    
    hr(),
    
    fluidRow(
      column(3,
        wellPanel(
          selectInput("lcategory", "Category:", choices=levels(mydata$item_category),'All')
        )
      ),
      column(6,
        mainPanel(
          plotOutput("locationplot")
        )
      ),
      column(3,
        mainPanel(
          htmlOutput("locationtext")
        )
      )
      
    ),
    
    p('\n'),
  
    titlePanel("Measures by different item_labels"),
    
    hr(),
    
    fluidRow(
      column(3,
             wellPanel(
               selectInput("lmeasure", "Measures:", choices=c('post_days_to_now', 'title_words_num','description_num','item_likes','item_price','item_truck_able','item_face_able','Count'), selected='C')
             )             
      ),
      
      column(6,
             mainPanel(
               plotOutput("labelplot")
             )
      ))),
  tabPanel("Text-Mining",
    actionButton("scrapy", "Acquire Data"),
    titlePanel("Most frequent keywords of item titles"),
      hr(),
      fluidRow(
        column(3,
          wellPanel(
              selectInput("kcategory", "Category:", choices=levels(mydata$item_category)),
              sliderInput("mf","Minimum frequency:",min = 25,max = 500,value = 25,step=25)
          )
        ),
        column(6,
          mainPanel(
              #strong('WordCloud Plot in given category'),
              wordcloud2Output("wordcloud",width="520px")
          )
        ),
        column(3,
          mainPanel(
              htmlOutput("titletext")
          )
        )
      ),
      titlePanel("Most frequent keywords of all item descriptions"),
      hr(),
      fluidRow(
        column(3,
          wellPanel(
              selectInput("kdcategory", "Category:", choices=levels(mydata$item_category)),
                        sliderInput("kdmf","Minimum frequency:",min = 100,max = 500,value = 150,step=25),
                        sliderInput("kdmaf","Maximum frequency:",min = 1000,max = 10000,value = 10000,step=500)
          )             
        ),
        column(6,
          mainPanel(
              #helpText('WordCloud Plot in given category'),
              wordcloud2Output("kdwordcloud",width="520px")
          )
        ),
        column(3,
          mainPanel(
              htmlOutput("desriptiontext")
          )
        )
      ),
    titlePanel("Average likes by different length of item titles & item descriptions"),
    hr(),
    fluidRow(
        column(2,
          wellPanel(
                selectInput("aktcategory", "Category:", choices=c(levels(mydata$item_category),'All'), selected='luxury-20'),
                sliderInput("aktbin","Number of bins:",min = 3,max = 10,value = 5)
          )             
        ),
        column(4,
          mainPanel(
                plotOutput("aktplot")
          )
        ),
        column(2,
          wellPanel(
                selectInput("akdcategory", "Category:", choices=c(levels(mydata$item_category),'All'), selected='luxury-20'),
                sliderInput("akdbin","Number of bins:",min = 3,max = 10,value = 5)
          )             
        ),
        column(4,
          mainPanel(
                plotOutput("akdplot")
          )
        )
      )
  ),
  tags$style(type='text/css', "#scrapy { float: right;}")
))

