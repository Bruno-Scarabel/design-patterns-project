# Padrão Observer (Comportamental)

O Observer é um padrão de projeto comportamental que permite que um objeto (chamado de Sujeito) notifique automaticamente uma lista de outros objetos (Observadores) sobre qualquer mudança de estado.

## Problema

Você tem vários componentes que precisam reagir automaticamente quando algo muda em outro componente.  
Por exemplo, em um sistema de notícias, quando uma nova matéria é publicada, todos os inscritos devem ser notificados.

## Solução

O padrão Observer cria uma relação um-para-muitos entre objetos:  
quando o sujeito muda, ele notifica todos os observadores.

## Estrutura UML

