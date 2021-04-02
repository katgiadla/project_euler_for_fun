class Multiply_Problem:

    def create_multiply(factor: int, max_value: int) -> {}:
        """

        Args:
            max_value (int):    maximal value
            factor (int):       multiplier
        Returns:
            {} (int):           set of multipliers
        """
        if max_value == 0:
            raise ValueError("Incorrect value of max_value")
        elif factor <= 0:
            raise ValueError("Incorrect value of factor")
        return {factor for factor in range(factor, max_value + 1, factor)}

    def multiply_and_sum_universal(factor_1: int = 3, factor_2: int = 5, max_value: int = 1000) -> int:
        """

        Args:
            factor_1 (int, default=3):      first multiplier
            factor_2 (int, default=5):      second multiplier
            max_value (int, default=1000):  maximal value

        Returns:
            sum_multipliers (int):          sum of multipliers
        """
        if max_value <= 0:
            raise ValueError("Value is equal or less than 0")


        sum_multipliers = 0



        return sum_multipliers