# Price Elasticity
![price-elasticity](https://github.com/adrielepinto/price-elasticity/assets/97919969/18d9fed6-8a79-4ff7-a158-5a6b26b2a888)


# Business Problem 
The company Prodcts & Cia intends to change the prices of the products sold, but also is afraid that this change will impact the demand for these products and, consequently, the billing. This demand has been submitted to you and as a data scientist me need to determine price elasticity using scientific methodology based on price data for the products sold by the company.
# Solution

Create cross-elasticity between all products, where it will be possible to detect the impact of price increases or decreases on each product.

# Attribute List
 - Date_imp = Date of Demand.
 - Category_name = Category name of the product.
 - name = Name of product;
 - price = Price of procuct;
 - disc_price = Price with discount.
 - merchant = Name of the company.
 - Disc_percentage = Percentage of discount.
 - isSale = If the product is for sale.
 - Imp_count = Countting of demand.
 - brand = Brand of the product.
 - p_description = Desription of the product.
 - dateAdded = When the was added to dataset.
 - dateSeen = When was sent.
 - dateUpdated = update date.
 - manufacturer = Manufacturer of the p[roduct.
 - Day_n = Day of the week by name.
 - month = Month by number.
 - month_n = Month by name.
 - day = Day by numbers.
 - Week_Number = Week number of the year.

 # Questions to answer:
 - Which merchant sold more?
 -  Which category  sold more?
 -  Which brand sol more?
 -  Which days sold more?
 -  Which months sold more?
 -  Which weeks sold more?
# Three Data Insigths: 
# H1 - Which merchant sold more?
<img width="802" alt="Screen Shot 2023-08-28 at 9 32 48 AM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/ee57fb45-44d1-4a42-b318-2e02bdeadd1d">

According to the data the merchant EBAY has a large amount of sells compared  to the others.

# H5 - Which brand sold moer?
<img width="370" alt="Screen Shot 2023-08-28 at 9 37 37 AM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/1db183ab-8f04-4af9-9d03-91a66eb65689">

Clearly, Sonny, Sansung and Apple sells more, however Sonny is the pioneer of the business.

# H8 - Which months sold more?
<img width="1177" alt="Screen Shot 2023-08-28 at 12 24 41 PM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/79352127-6b5a-4c03-9b92-5d727253a00a">

Jully  an dAugust are the months that sold more. Maybe it can be explainned bacause it's the month when kids are returning to school and many of them need electronics for their classes.

# Machine Learning

<img width="635" alt="Screen Shot 2023-09-01 at 11 15 20 AM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/4dbd6aee-970c-4f42-9fbd-2beff19bf392">


After run the Exploratoyr data analysis, I needed to split the dataset in two, and pivoted, making the name of the products the name of the columns. 

## OLS
Ordinary Least Squares regression (OLS) is a technique for estimating coefficients of linear regression equations which describe the relationship between one or more independent quantitative variables and a dependent variable (simple or multiple linear regression). This was the algorithm chosen to perform the linear regression model. The algorithm basically calculates the coefficients of a linear regression in such a way that the errors, or rather, the sum of squared errors (SQE) is as small as possible.



<img width="828" alt="Screen Shot 2023-09-01 at 11 47 45 AM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/67c02a6c-18f1-46db-abb7-1ddc12da13c8">


- Intercept = Linear coefficient.
- Slope = Angular Coefficient.
- Rsquared = R Squared.
- P_value = P Value.



# Business Performance
<img width="1119" alt="Screen Shot 2023-08-28 at 12 17 39 PM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/2005f105-afda-4e1e-a274-d4050bd0796a">


Of all the products tested, Details About Apple Macbook Air 13.3 Laptop (early 2015) 2.2ghz Core I7 8gb 256gb, is the product that showed the most elasticity.
- Current Demand 10; 
- The currente revenue is $7955.09;
- Suggested reducting of 10% the new price of the product would be $7159.58 ;
- Increase in demand due to the reduction to 34.12, the revenue would be $24432.58;
- A suggested reducting of 10% would add  $16477.49 


##  Infrastructure of Cross Price Viazualization  in production

<img width="763" alt="Screen Shot 2023-09-01 at 10 51 47 AM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/affaac6d-2cb5-4453-862c-92498f5dadc9">


In this production structure, the cleaning and data manipulation codes will be sent to a repository on Git Hub. With the updated files, an application will be created in Streamlite that will consume this data, creating the Price Elasticity of the product.


# Cross Price in production

The results of the model can seen by clicking on the link below:

- OBS: If your browser isn't compatible, you'll need copy the link and past on the Google Chrome to visualize.


https://price-elasticity-ogwc2dqguyjrchr6o4mfhj.streamlit.app/


# Conclusion

Price elasticity is a measure of how the demand for a product or service is affected by changes in the price, being an invaluable tool for companies to determine the ideal prices for their products and services, in order to maximize their profits.
A elastic demand means that a small change in price will result in a large change in quantity demanded. On the other hand, inelastic demand means that a change in price will have little impact on the quantity demanded. If demand is elastic, for example, a reduction in prices can increase sales and generate more profit. If demand is inelastic, it is possible to increase prices without affecting sales as much.
A clear understanding of price elasticity can help companies stay competitive and meet customer needs more effectively.


# Contact:


https://www.linkedin.com/in/adriele-pinto/




