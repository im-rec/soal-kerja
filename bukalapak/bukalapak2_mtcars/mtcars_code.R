## @knitr read
mtc <- mtcars
head(mtc)
str(mtc)

## @knitr explore
cor(mtc)
sort(cor(mtc)[1,], decreasing = T)

## @knitr m1
fit1 <- lm(mpg ~ wt, data = mtc)
summary(fit1)

## @knitr m2
fit2 <- lm(mpg ~ wt + hp, data = mtc)
summary(fit2)

## @knitr ujicoba
# fit1 <- lm(mpg ~ wt + cyl, data = mtc)
# summary(fit1)
# 
# fit1 <- lm(mpg ~ wt + hp, data = mtc)
# summary(fit1)
# 
# fit1 <- lm(mpg ~ wt + cyl + disp, data = mtc)
# summary(fit1)
# 
# fit2 <- lm(mpg ~ wt + cyl + hp, data = mtc)
# summary(fit2)
# 
# fit2 <- lm(mpg ~ wt + cyl + am, data = mtc)
# summary(fit2)
# 
# fit1 <- lm(mpg ~ wt + hp + am, data = mtc)
# summary(fit1)

# @knitr dc
layout(matrix(c(1,2,3,4),2,2))
plot(fit2)

# @knitr cat
# additional
# using packages to see VIF, homoskeasticity, and autocolinearity
# but we can see that the model has already good by the number of statistics

