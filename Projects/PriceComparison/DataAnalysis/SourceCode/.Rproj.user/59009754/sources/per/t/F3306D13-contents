require(readxl)

extraxted_data_amz <-  read_xlsx("../ExtractedData/AmzProd.xlsx")
df_AMZ_price <- data.frame(Price = extraxted_data_amz[2])#get only the prices column
AMZ_values <- as.numeric(unlist(df_AMZ_price))

n<-1
for (n in c(1:length(AMZ_values))){#remove outline values
  if(AMZ_values[n]>=100){
    AMZ_values[n] = NA
  }
}

AMZ_mean <- mean(AMZ_values, na.rm = TRUE)
AMZ_md <- median(sort(AMZ_values), na.rm = TRUE)
AMZ_mean
AMZ_md

hist(AMZ_values)
AMZ_values <- AMZ_values[!AMZ_values %in% boxplot.stats(AMZ_values)$out]#Discard extreme values
boxplot(AMZ_values)

