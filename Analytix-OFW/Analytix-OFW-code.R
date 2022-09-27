###############################
# ANALYTIX-OFW-CODE.R
# J. Norman Pasamonte
# 25 Sep 2022
#
# Contains all the R code  
# used in ANALYTIX-OFW-PAPER.RMD
#
# Some graph outputs need to be
# manually saved as PNG files 
# using the Export button in 
# RStudio.
#
# Modeling output automatically
# saved as txt files.
#
###############################

### Checking/installing required packages 
### and setting (default) working directory.
### The working directory is the single
### directory where all the R, RMD,
### data and other figures are stored.

# Check required packages
required_packages <-  c("dplyr", "tidyverse", "ggplot2", "echarts4r", "plm", "lmtest", "rmarkdown", "GGally", "stargazer", "kableExtra", "tinytex")
need_install <- required_packages[!(required_packages) %in% installed.packages()]
if (length(need_install) > 0) {
  install.packages(need_install)}

# load required packages
lapply(required_packages, require, character.only = TRUE)

# Set working directory
dir_script <- getwd() #dirname(rstudioapi::getSourceEditorContext()$path)
setwd(dir_script)


### Loading datasets and spliting tables.

# Load datasets

# 1. ofw destinations
ofw_dest <- read.csv("analytix_ofw_dest.csv",TRUE,",")
colnames(ofw_dest) <- c("Rank", "Country", "Male", "Female", "OFW")

# 2. gender indices data
gender <- read.csv("analytix_gender_index.csv",TRUE,",")
# create a backup of original table
gender2 <- gender
# change year to type factor for graphing
gender$year <- as.factor(gender$year)
# create panel data frame
gender_df <- pdata.frame(read.csv("analytix_gender_index.csv",TRUE,","),index=c("rank","year"))

# Split gender indices per country

# 1. Philippines
mgi_PH <- gender
mgi_PH <- mgi_PH[c(7:20),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_PH) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 2. Saudi Arabia
mgi_SA <- gender
mgi_SA <- mgi_SA[c(27:40),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_SA) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 3. United Arab Emirates
mgi_AE <- gender
mgi_AE <- mgi_AE[c(47:60),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_AE) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 4. Kuwait
mgi_KW <- gender
mgi_KW <- mgi_KW[c(67:80),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_KW) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 5. Qatar
mgi_QA <- gender
mgi_QA <- mgi_QA[c(87:100),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_QA) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 6. Singapore
mgi_SG <- gender
mgi_SG <- mgi_SG[c(107:120),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_SG) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 7. Japan
mgi_JP <- gender
mgi_JP <- mgi_JP[c(127:140),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_JP) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 8. Australia
mgi_AU <- gender
mgi_AU <-mgi_AU[c(147:160),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_AU) <- c("Country", "Year", "GDI", "GII", "GGGI")

# 9. Malaysia
mgi_MY <- gender
mgi_MY <-mgi_MY[c(167:180),c("country_name", "year", "gdi", "gii", "gggi")]
colnames(mgi_MY) <- c("Country", "Year", "GDI", "GII", "GGGI")


### Leading OFW Destination Countries

# Figure 1.Pie chart of OFW Destination Countries
slices <- c(26.03,14.60,6.42,6.34,5.43,5.42,4.76,3.50,3.41,1.49,22.10)
lbls = c('(1) Saudi Arabia','(2) United Arab Emirates','(3) Kuwait','(4) Hongkong','(5) Qatar','(6) Singapore','(7) Taiwan','(8) Japan','(9) Australia','(10) Malaysia','Rest of the World')
pie(slices, labels=lbls, main="Figure 1. Top 10 OFW Destination Countries" )

# Figure 2. Line chart of OFW Destionation Countries
ofw_d <- ofw_dest
ofw_p <- ofw_d |>
  e_charts(Country, time_line=TRUE) |>
  e_bar(Male, color="green", stack = "grp") |>
  e_bar(Female, color="orange", stack = "grp") |>   
  e_title("Figure 2. Gender Distribution in Leading OFW Destinations", align="center") |>
  e_grid(left = '17%') |>
  e_legend(orient='vertical', right='5',top='15%')
e_flip_coords(ofw_p)

### Gender Inequality Analysis

# Figure 6A. Gender Measures: Philippines 
mgi_PH |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6A. Gender Measures (Philippines)", align="center")

# Figure 7A. Gender Indices Correlation Matrix: Philippines
ggpairs(data=mgi_PH, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7A. Gender Indices Correlation Matrix (Philippines)" )

# Figure 6B. Gender Measures: Saudi Arabia
mgi_SA |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6B. Gender Measures (Saudi Arabia)", align="center")

# Figure 7B. Gender Indices Correlation Matrix: Saudi Arabia
ggpairs(data=mgi_SA, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7B. Gender Indices Correlation Matrix (Saudi Arabia)" )

# Figure 6C. Gender Measures: United Arab Emirates
mgi_AE |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6C. Gender Measures (United Arab Emirates)", align="center")

# Figure 7C. Gender Indices Correlation Matrix: United Arab Emirates
ggpairs(data=mgi_AE, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7C. Gender Indices Correlation Matrix (United Arab Emirates)" )

# Figure 6D. Gender Measures: Kuwait
mgi_KW |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6D. Gender Measures (Kuwait)", align="center")

# Figure 7D. Gender Indices Correlation Matrix: Kuwait 
ggpairs(data=mgi_KW, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7D. Gender Indices Correlation Matrix (Kuwait)" )

# Figure 6E. Gender Measures: Qatar
mgi_QA |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6E. Gender Measures (Qatar)", align="center")

# Figure 7E. Gender Indices Correlation Matrix: Qatar 
ggpairs(data=mgi_QA, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7E. Gender Indices Correlation Matrix (Qatar)" )

# Figure 6F. Gender Measures: Singapore
mgi_SG |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6F. Gender Measures (Singapore)", align="center")

# Figure 7F. Gender Indices Correlation Matrix: Singapore 
ggpairs(data=mgi_SG, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7F. Gender Indices Correlation Matrix (Singapore)" )

# Figure 6G. Gender Measures: Japan
mgi_JP |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6G. Gender Measures (Japan)", align="center")

# Figure 7G. Gender Indices Correlation Matrix: Japan
ggpairs(data=mgi_JP, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7G. Gender Indices Correlation Matrix (Japan)" )

# Figure 6H. Gender Measures: Australia
mgi_AU |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6H. Gender Measures (Australia)", align="center")

# Figure 7H. Gender Indices Correlation Matrix: Australia
ggpairs(data=mgi_AU, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7H. Gender Indices Correlation Matrix (Australia)" )

# Figure 6I. Gender Measures: Malaysia
mgi_MY |>
  e_charts(x = Year) |>
  e_line(serie = GDI) |>
  e_line(serie = GII) |>
  e_line(serie = GGGI) |>
  e_grid(right = '20%') |>
  e_legend(orient='vertical', right='5',top='15%') |>
  e_title("Figure 6I. Gender Measures (Malaysia)", align="center")

# Figure 7I. Gender Indices Correlation Matrix: Malaysia
ggpairs(data=mgi_MY, columns=3:5, 
        aes(color="Country", alpha=0.5), title="Figure 7I. Gender Indices Correlation Matrix (Malaysia)" )


### Data Panel Regression Analysis

# Table 1. Gender Development Index based on HDI for females and males
gdi_po <- plm(log(gdi)~hdi_f+hdi_m, data=gender_df[which(!is.na(gender_df$gdi)),], model = "pooling")
gdi_fe <- plm(log(gdi)~hdi_f+hdi_m, data=gender_df[which(!is.na(gender_df$gdi)),], model = "within")
gdi_re <- plm(log(gdi)~hdi_f+hdi_m, data=gender_df[which(!is.na(gender_df$gdi)),], model = "random")

stargazer(gdi_po, gdi_fe, gdi_re, align=TRUE, type="text",
          title="Table 1. Panel Regression Models (GDI)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("HD Female", "HD Male"), 
          dep.var.caption = "Gender Development Index",
          out="preg_gdi.txt")

# Table 1A. Gender Development Index based on indicator variables for females
gdi_po_f <- plm(log(gdi)~le_f+eys_f+mys_f+gni_pc_f, data=gender_df[which(!is.na(gender_df$gdi)),], model = "pooling")
gdi_fe_f <- plm(log(gdi)~le_f+eys_f+mys_f+gni_pc_f, data=gender_df[which(!is.na(gender_df$gdi)),], model = "within")
gdi_re_f <- plm(log(gdi)~le_f+eys_f+mys_f+gni_pc_f, data=gender_df[which(!is.na(gender_df$gdi)),], model = "random")

stargazer(gdi_po_f, gdi_fe_f, gdi_re_f, align=TRUE, type="text",
          title="Table 1A. Panel Regression Models (GDI)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Life Expectancy (F)","Years of Schooling (F)", "Mean: Years of Schooling (F)", "Gross National Income (F)"), 
          dep.var.caption = "Gender Development Index",
          out="preg_gdi_f.txt")

# Table 1B. Gender Development Index based on indicator variables for males
gdi_po_m <- plm(log(gdi)~le_m+eys_m+mys_m+gni_pc_m, data=gender_df[which(!is.na(gender_df$gdi)),], model = "pooling")
gdi_fe_m <- plm(log(gdi)~le_m+eys_m+mys_m+gni_pc_m, data=gender_df[which(!is.na(gender_df$gdi)),], model = "within")
gdi_re_m <- plm(log(gdi)~le_m+eys_m+mys_m+gni_pc_m, data=gender_df[which(!is.na(gender_df$gdi)),], model = "random")

stargazer(gdi_po_m, gdi_fe_m, gdi_re_m, align=TRUE, type="text",
          title="Table 1B. Panel Regression Models (GDI)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Life Expectancy (M)","Years of Schooling (M)", "Mean: Years of Schooling (M)", "Gross National Income (M)"), 
          dep.var.caption = "Gender Development Index",
          out="preg_gdi_m.txt")

# Table 2. Gender Inequality Index
gii_po <- plm(log(gii)~sdg3_matmort+sdg3_fertility+sdg5_parl+sdg4_second+sdg5_lfpr, data=gender_df[which(!is.na(gender_df$gii)),], model = "pooling")
gii_fe <- plm(log(gii)~sdg3_matmort+sdg3_fertility+sdg5_parl+sdg4_second+sdg5_lfpr, data=gender_df[which(!is.na(gender_df$gii)),], model = "within")
gii_re <- plm(log(gii)~sdg3_matmort+sdg3_fertility+sdg5_parl+sdg4_second+sdg5_lfpr, data=gender_df[which(!is.na(gender_df$gii)),], model = "random")

stargazer(gii_po, gii_fe, gii_re, align=TRUE, type="text",
          title="Table 2. Panel Regression Models (GII)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Maternal Mortality", "Adolescent Fertility","Seats in Parliament","Secondary Education","Labor Force Participation"), 
          dep.var.caption = "Gender Inequality Index",
          out="preg_gii.txt")

# Table 3. Global Gender Gap Index  
gggi_po <- plm(log(gggi)~ggg_pe+ggg_epo+ggg_ea+ggg_hs, data=gender_df[which(!is.na(gender_df$gggi)),], model = "pooling")
gggi_fe <- plm(log(gggi)~ggg_pe+ggg_epo+ggg_ea+ggg_hs, data=gender_df[which(!is.na(gender_df$gggi)),], model = "within")
gggi_re <- plm(log(gggi)~ggg_pe+ggg_epo+ggg_ea+ggg_hs, data=gender_df[which(!is.na(gender_df$gggi)),], model = "random")

stargazer(gggi_po, gggi_fe, gggi_re, align=TRUE, type="text",
          title="Table 3. Panel Regression Models (GGGI)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Political Empowerment", "Economic Participation","Educational Attainment","Health Survival"), 
          dep.var.caption = "Global Gender Gap Index",
          out="preg_gggi.txt")

### Modeling Gender Measures using SDG5 gender inequality indicators 

# Table 4. Panel regression results: GDI
gdi_sdg_po <- plm(log(gdi)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gdi)),], model = "pooling")
gdi_sdg_fe <- plm(log(gdi)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gdi)),], model = "within")
gdi_sdg_re <- plm(log(gdi)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gdi)),], model = "random")

stargazer(gdi_sdg_po, gdi_sdg_fe, gdi_sdg_re, align=TRUE, type="text",
          title="Table 4. Panel Regression Models (GDI with SDG gender inequality indicators)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Family Planning", "Years of Education", "Labor Force Participation", "Seats in Parliament"), 
          dep.var.caption = "Gender Development Index",
          out="preg_gdi_sdg.txt")

# Table 5. Panel regression results: GII
gii_sdg_po <- plm(log(gii)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gii)),], model = "pooling")
gii_sdg_fe <- plm(log(gii)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gii)),], model = "within")
gii_sdg_re <- plm(log(gii)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gii)),], model = "random")

stargazer(gii_sdg_po, gii_sdg_fe, gii_sdg_re, align=TRUE, type="text",
          title="Table 5. Panel Regression Models (GII with SDG gender inequality indicators)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Family Planning", "Years of Education", "Labor Force Participation", "Seats in Parliament"), 
          dep.var.caption = "Gender Inequality Index",
          out="preg_gii_sdg.txt")

# Table 6. Panel regression results: GGGI
gggi_sdg_po <- plm(log(gggi)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gggi)),], model = "pooling")
gggi_sdg_fe <- plm(log(gggi)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gggi)),], model = "within")
gggi_sdg_re <- plm(log(gggi)~sdg5_fplmodel+sdg5_edat+sdg5_lfpr+sdg5_parl, data=gender_df[which(!is.na(gender_df$gggi)),], model = "random")

stargazer(gggi_sdg_po, gggi_sdg_fe, gggi_sdg_re, align=TRUE, type="text",
          title="Table 6. Panel Regression Models (GGGI with SDG gender inequality indicators)",
          column.labels = c("Pooled", "Fixed Effects", "Random Effects"),
          covariate.labels = c("Family Planning", "Years of Education", "Labor Force Participation", "Seats in Parliament"), 
          dep.var.caption = "Global Gender Gap Index",
          out="preg_gggi_sdg.txt")


