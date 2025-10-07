class Supplier:
    def __init__(self, name): self.name = name
    def __str__(self): return self.name

class Product:
    def __init__(self, name, price, qty, supplier):
        self.name, self.price, self.qty, self.supplier = name, price, qty, supplier
    def restock(self, amt): self.qty += amt
    def __str__(self): return f"{self.name} - ${self.price:.2f} | Qty: {self.qty} | {self.supplier}"

class Inventory:
    def __init__(self): self.items = []
    def add(self, product): self.items.append(product)
    def restock(self, name, amt):
        for p in self.items:
            if p.name == name: p.restock(amt); print(f"{name} restocked by {amt}."); break
    def show(self):
        print("\nInventory:")
        for p in self.items: print(p)


s1, s2 = Supplier("Tech Co."), Supplier("Office Inc.")
inv = Inventory()
inv.add(Product("Laptop", 900, 5, s1))
inv.add(Product("Printer", 150, 2, s2))

inv.show()
inv.restock("Laptop", 5)
inv.show()