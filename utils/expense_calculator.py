class Calculator:
    @staticmethod
    def multiply(a: int, b: int)-> int:
        return a*b
    
    @staticmethod
    def calculate_total(*x:float) -> float:
        """
        Arg: 
        x (list): List of floating numbers
        Returns:
        Float: The sum of numbers on the list x
        """
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Arg: 
        total(float): Total cost
        days (int) Total number of days
        Returns:
        Float: The expense per day.
        """
        return total / days if days >0 else 0
    
