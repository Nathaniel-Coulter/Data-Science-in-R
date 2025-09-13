# MLB Teams Data Analysis 

# libraries
library(dplyr)  # data manipulation
library(ggplot2)  # visualization


mlb <- read.csv("C:/Users/hocke/OneDrive/Documents/R Programs (Intro to Data Science Class)/MLB_1973-2024_Teams.csv", 
                header = TRUE, stringsAsFactors = FALSE)


print(colnames(mlb))


colnames(mlb)[colnames(mlb) == "W.L."] <- "Win_Loss"


if (!all(c("R", "Rallow") %in% colnames(mlb))) {
  stop("Columns 'R' or 'Rallow' not found in dataset.")
}


mlb <- mlb %>% select(-Pythag)

mlb$Pythag <- mlb$R^2 / (mlb$R^2 + mlb$Rallow^2)

mlb2 <- filter(mlb, Season <= 1998)

plot1 <- ggplot(mlb2, aes(x = Pythag, y = Win_Loss)) + 
  geom_point() +
  labs(title = "MLB Teams 1973-1998",
       x = "Pythagorean Win Percentage",
       y = "Actual Win Percentage") +
  theme_minimal()

print(plot1)

plot2 <- ggplot(mlb2, aes(x = OPS, y = R)) + 
  geom_point() +
  labs(title = "MLB Teams 1973-1998",
       x = "Team OPS",
       y = "Runs Scored") +
  theme_minimal()

print(plot2)


