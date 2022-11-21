class FoodItem():
    barCode = 0
    productName = ""
    price = 0.0
    
    def __init__(self, code, name, cost):
        self.barCode = code
        self.productName = name
        self.price = cost
    
    def getBarCode(self):
        return self.barCode
    
    def getProductName(self):
        return self.productName
    
    def getPrice(self):
        return self.price
    
    def __str__(self):
        return ("{} costs ${:.2f}, barcode: {}".format
                (self.productName, self.price, self.barCode))

class ShoppingList():
    aList = list()
    
    def addItem(self, foodItem):
        self.aList.append(foodItem)
        
    def getLength(self):
        return len(self.aList)
    
    def __str__(self):
        total = 0
        for item in self.aList:
            total += item.getPrice()
            print(item)
        return "\n" + self.totalCost(total)
    
    def totalCost(self, total):
        return "Total cost: ${:.2f}".format(total) 
