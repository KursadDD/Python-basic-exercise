PROBLEM-1:
You work for a manufacturer as a programmer and have been asked to calculate the total profit made on the sales of a product. You are given a dictionary (sales) containing the cost price per unit (in dollars), sell price per unit (in dollars), and the beginning inventory. Write a program to return the total profit made, rounded to the nearest dollar. Assume all of the inventory has been sold. The name and the keys of the dictionary are constant, so use them as they are.
The example of the values (sell-cost value, inventory) and total profit :

sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  

# the profit will be : 13130

PROBLEM-2:
Your boss wants you to prepare the payrolls of the workers in your department. You have to convert the amount of dollars into payroll format. In order to help move things along, you have volunteered to write a code that will take a float and return the amount formatting in dollars and cents. 

SOLUTİON-1:
 
sales = {"cost_value": 31.87,

"sell_value": 45.00,

"inventory": 1000 }

# the profit will be : 13130

profit = float((sales["sell_value"] - sales["cost_value"]) * sales["inventory"])

print("%.2f" %profit)



SOLUTİON-2:

value1 = float(input("1.değeri giriniz: "))

value2 = float(input("2.değeri giriniz: "))

value3 = float(input("3.değeri giriniz: "))

bordro = {

    "pay1":value1,

    "pay2":value2,

    "pay3":value3

}

print("Pay1: $%.2f\nPay2: $%.2f\nPay3: $%.2f" %(bordro["pay1"], bordro["pay2"], bordro["pay3"]))