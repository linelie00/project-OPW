class Book:
    total = 0

    def __init__(self, title, author, inventory):
        self.title = title
        self.author = author
        self.inventory = inventory
        Book.total += inventory

    @classmethod
    def total_inventory(self):
        print(f'Total inventory: {Book.total}')

    def increase_inventory(self, amount):
        self.inventory += amount
        Book.total += amount
    
    def decrease_inventory(self, amount):
        self.inventory -= amount
        Book.total -= amount
    
    def show_info(self):
        print(f'{self.title} by {self.author} - {self.inventory} in stock')

book1 = Book('Band Basics', 'Kai Huening', 10)
Book.total_inventory()
book2 = Book('Java Programming', 'Taehyun Kang', 20)
Book.total_inventory()
book1.show_info()
book2.show_info()