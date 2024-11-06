class Car:
    def __init__(self, model, year, color, for_sale) -> None:
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You are driving {self.color} {self.model}.")

    def stop(self):
        print(f"{self.color} {self.model} Stopped.")
        
    def describe(self):
        print(f"{self.year} {self.model} {self.color}")