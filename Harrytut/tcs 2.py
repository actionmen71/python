Item_Number = [101, 102, 103, 104]
Item_Name = ["Milk", "Cheese", "Ghee", "Bread"]
Price = [42, 50, 500, 40]
Stock = [10, 20, 15, 16]

item_num = int(input("Item no to buy"))
item_quant = int(input("Quantity to buy"))
if (item_num in Item_Number):
    for i in range(len(Item_Number)):
        if (item_num == Item_Number[i]):
            index = i
            if item_quant <= Stock[index]:
                print(item_quant * Price[index], "INR")
                Stock = Stock[index] - item_quant
                print(Stock, "LEFT")
            elif item_quant > Stock[index]:
                print("NO STOCK")
                print(Stock[index], "LEFT")
else:
    print("Invalid input")


