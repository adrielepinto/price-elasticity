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
Ordinary Least Squares regression (OLS) is a common technique for estimating coefficients of linear regression equations which describe the relationship between one or more independent quantitative variables and a dependent variable (simple or multiple linear regression).
<img width="791" alt="Screen Shot 2023-08-28 at 12 12 00 PM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/d6b20370-83f3-4c77-868d-8ff39b0de5f6">

I ran a test to see how the algorithm would behave..


# Price Elastice 
<img width="1119" alt="Screen Shot 2023-08-28 at 12 15 53 PM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/e438cc14-ac99-4b23-9781-1c8271068afb">

# Business Performance
<img width="1119" alt="Screen Shot 2023-08-28 at 12 17 39 PM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/2005f105-afda-4e1e-a274-d4050bd0796a">


# Cross Price Viazualization


# Infrastructure in production

<img width="763" alt="Screen Shot 2023-09-01 at 10 51 47 AM" src="https://github.com/adrielepinto/price-elasticity/assets/97919969/affaac6d-2cb5-4453-862c-92498f5dadc9">


In this production structure, the cleaning and data manipulation codes will be sent to a repository on Git Hub. With the updated files, an application will be created in Streamlite that will consume this data, creating the Price Elasticity of the product.


# Learnings





