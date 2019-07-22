library(fpp2)
library(readr)

auscafe
autoplot(auscafe)

auscafe_df <- data.frame(
  expenditure = as.matrix(auscafe),
  time = time(auscafe)
)

food <- auscafe_df %>%
  filter(time >= 2004, time < 2017)

write_csv(x = food, "aus_food.csv")

ggplot(data = auscafe_df %>% mutate(log_expenditure = log(expenditure)) %>%
         filter(time >= 2004),
    mapping = aes(x = time, y = log_expenditure)) +
  geom_line()
