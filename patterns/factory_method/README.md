# Padrão Factory Method 

O **Factory Method** é um padrão de projeto criacional que fornece uma interface para criar objetos em uma superclasse, permitindo que as subclasses alterem o tipo de objetos que serão criados.

---

## Problema

Em muitos programas, você precisa criar objetos de tipos diferentes, mas o código principal não deve conhecer os detalhes de como cada tipo é criado.

Exemplo: um sistema que gera diferentes tipos de botões — HTML, Windows, ou macOS.  
Seria ruim ter `if` e `else` em todo lugar para decidir qual botão criar.

---

## Solução

O Factory Method cria uma **classe base com um método-fábrica** (factory method), que pode ser sobrescrito nas subclasses para decidir qual objeto concreto instanciar.

---

## Estrutura UML

classDiagram
    class Creator {
        +factoryMethod()
        +someOperation()
    }

    class ConcreteCreatorA {
        +factoryMethod()
    }

    class ConcreteCreatorB {
        +factoryMethod()
    }

    class Product {
        +use()
    }

    class ConcreteProductA {
        +use()
    }

    class ConcreteProductB {
        +use()
    }

    Creator <|-- ConcreteCreatorA
    Creator <|-- ConcreteCreatorB

    Product <|-- ConcreteProductA
    Product <|-- ConcreteProductB

    Creator --> Product : cria