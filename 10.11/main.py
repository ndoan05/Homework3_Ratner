# Nam Doan
#1847037

class FoodItem:

    def __init__(self, name='None', fat=0.0, carbohydrates=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.protein = protein

    def get_calories(self, num_servings):

        calories = ((self.fat * 9) + (self.carbohydrates * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbohydrates))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":

    item_food_1 = FoodItem()

    item_name = input()
    amount_fat = float(input())
    amount_carbohydrates = float(input())
    amount_protein = float(input())

    item_food_2 = FoodItem(item_name, amount_fat, amount_carbohydrates, amount_protein)

    num_servings = float(input())

    item_food_1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    item_food_1.get_calories(num_servings)))

    print()

    item_food_2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    item_food_2.get_calories(num_servings)))

