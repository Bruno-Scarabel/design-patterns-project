# Padrão Decorator (Estrutural)
# Exemplo baseado no catálogo Refactoring Guru
# Implementação feita com auxílio do ChatGPT (GPT-5)

from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 5.00

    def description(self) -> str:
        return "Café simples"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.50

    def description(self) -> str:
        return self._coffee.description() + ", leite"

class ChocolateDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 2.00

    def description(self) -> str:
        return self._coffee.description() + ", chocolate"

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 1.00

    def description(self) -> str:
        return self._coffee.description() + ", chantilly"


if __name__ == "__main__":
    coffee = SimpleCoffee()
    print(coffee.description(), "-> R$", coffee.cost())

    coffee = MilkDecorator(coffee)
    coffee = ChocolateDecorator(coffee)
    coffee = WhippedCreamDecorator(coffee)

    print(coffee.description(), "-> R$", coffee.cost())
