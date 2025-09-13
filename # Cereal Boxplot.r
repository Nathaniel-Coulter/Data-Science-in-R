# Cereal Boxplot 

library(MASS)
df=UScereal

ggplot(df,aes(y = sugars))
    geom_boxplot() + scale_x_discrete() + 
    labs(title = "Sugar Content in One Cup of US Cerreal",
         y = "Grams of Sugar")
 
    theme_minimal()
   summary(df$sugars)
   which.max()
   df[45,]
   #df[which.max(df$sugars),]