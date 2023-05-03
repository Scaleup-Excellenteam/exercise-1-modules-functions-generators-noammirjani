"""5.2 Piece of cake by Noam Mir"""


def get_recipe_price(prices, optionals=[], **ingredients) -> int:
    """
    Return the price of the recipe, given the prices of the ingredients.
    :param prices:  a dictionary of ingredient names and their prices
    :param optionals: a list of optional ingredients
    :param ingredients:  a dictionary of ingredient names and their amounts
    :return: the price of the recipe
    """
    price = 0
    for ingredient, amount in ingredients.items():
        if ingredient not in optionals:
            price += prices[ingredient] * amount
    return price//100


print(get_recipe_price({}))
