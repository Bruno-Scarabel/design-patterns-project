# Padrão Decorator (Estrutural)

O **Decorator** é um padrão de projeto estrutural que permite adicionar comportamentos a objetos dinamicamente, sem alterar sua implementação original e sem criar subclasses demais.

---

## Problema

Se um objeto precisa de várias variações de comportamento, criar uma subclasse para cada combinação explode o número de classes necessárias.

---

## Solução

Envolver o objeto original dentro de outros objetos decoradores, cada um adicionando um comportamento extra.  
Assim, você pode empilhar funcionalidades, como camadas.

---

## Estrutura UML

classDiagram
    class Component {
        +operation()
    }

    class ConcreteComponent {
        +operation()
    }

    class Decorator {
        -Component component
        +operation()
    }

    class ConcreteDecoratorA {
        +operation()
    }

    class ConcreteDecoratorB {
        +operation()
    }

    Component <|-- ConcreteComponent
    Component <|-- Decorator
    Decorator <|-- ConcreteDecoratorA
    Decorator <|-- ConcreteDecoratorB
    Decorator --> Component
