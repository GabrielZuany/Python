require(readxl)

cv <- function(x){
  coef<-(sd(x, na.rm = TRUE)/mean(x, na.rm = T))*100
  return(coef)
}


#-----------AMZ-----------

extraxted_data_amz <-  read_xlsx("../ExtractedData/AMZProd.xlsx")
df_AMZ_price <- data.frame(Price = extraxted_data_amz[2])#get only the prices column
AMZ_values <- as.numeric(unlist(df_AMZ_price))

AMZ_mean <- mean(AMZ_values, na.rm = TRUE)
AMZ_md <- median(sort(AMZ_values), na.rm = TRUE)
AMZ_var <- var(AMZ_values, na.rm=T)
AMZ_sd <- sd(AMZ_values, na.rm=T)
AMZ_cv <- cv(AMZ_values)

boxplot(AMZ_values)
AMZ_statistical_report <- data.frame(AMZ_Max = max(AMZ_values,  na.rm = T), 
                                 AMZ_Min = min(AMZ_values,  na.rm = T), 
                                 AMZ_Mean = AMZ_mean, AMZ_Md = AMZ_md, 
                                 AMZ_Sd = AMZ_sd, AMZ_CoefVar = AMZ_cv)


#------------ML------------

extraxted_data_ML <-  read_xlsx("../ExtractedData/ML_list.xlsx")
df_ML_price <- data.frame(Price = extraxted_data_ML[2])#get only the prices column
ML_values <- as.numeric(unlist(df_ML_price))

ML_mean <- mean(ML_values, na.rm = TRUE)
ML_md <- median(sort(ML_values), na.rm = TRUE)
ML_var <- var(ML_values, na.rm=T)
ML_sd <- sd(ML_values, na.rm=T)
ML_cv <- cv(ML_values)

boxplot(ML_values)
ML_statistical_report <- data.frame(ML_Max = max(ML_values,  na.rm = T), 
                                    ML_Min = min(ML_values,  na.rm = T), 
                                    ML_Mean = ML_mean, ML_Md = ML_md, 
                                    ML_Sd = ML_sd, ML_CoefVar = ML_cv)

