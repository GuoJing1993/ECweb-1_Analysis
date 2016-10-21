Sys.setlocale("LC_ALL", "zh_TW.UTF-8")
Sys.setlocale("LC_TIME", "C")
path='/Users/peternapolon/desktop/carousell_project/analysis/test01.csv'
df=read.csv(path, sep=',', header=T, comment.char = '@')
df=df[2:1003]
#new=data.frame(df$Y, df[2:501])
#names(new)[1]='Y'

names(df)
tt=sample(nrow(df), 24000)
train_df = df[tt,]
test_df =df[-tt,]

train_df$Y=as.character(train_df$Y)
test_df$Y=as.factor(test_df$Y)

# SVM test
# library(e1071)
# model <- svm(Y ~ ., data = train_df[1:500])
# summary(model)
# pred_result <- predict(model, test_df[2:500])
# table(pred_result,test_df$Y)

#Decsion-Tree test
library(rpart)
cats_rpart_model <- rpart(Y~., data = train_df)
plot(cats_rpart_model)
text(cats_rpart_model,family='SimSun')
cats_rpart_pred <- predict(cats_rpart_model, test_df)
c=as.data.frame(cats_rpart_pred)
final=ifelse(c$Y>c$N,'Y','N')
table(final,test_df$Y)

tt=data.frame(final,test_df)
names(tt)
tt[tt$final=='Y'&tt$Y=='N']
sub=subset(tt, tt$final=='Y'&tt$Y=='N', select=c(1:502))
