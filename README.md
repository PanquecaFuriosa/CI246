# Program to manage boolean expressions

## Problem:

We want you to model and implement, in the language of your choice, a program that handles Boolean expressions. This program must meet the following characteristics:

a. You must know how to deal with expressions written in prefix and postfix order, with the following operators:
  - **Conjunction**: Represented by the symbol &.
  - **Disjunction**: Represented by the symbol |.
  - **Implication**: Represented by the symbol =>.
  - **Negation**: Represented by the symbol ˆ.
b. It must know how to deal with constant true and false logic.
c. Once the program is started, it will repeatedly ask the user for an action to proceed. Such action can be:
  1. ```EVAL <order> <expr>```<br>
    Represents an evaluation of the expression in <expr>, which is written according to <order>.<br>
    The <order> can only be:<br>
    - **PRE**: Which represents expressions written in prefix order.<br>
    - **POST**: Which represents expressions written in postfix order. <br>
    For example:<br>
    - ```EVAL PRE | & => true true false true``` should print **true**.<br>
    - ```EVAL POST true false => false | true false ˆ | &``` should print **false**.<br>

  2. ```MOSTRAR <order> <expr>```<br>
    Represents an in–fixed-order printout of the expression in <expr>, which is written according to <order>.<br>
    The <order> follows the same pattern as in the previous point.<br>
    Your program should take standard precedence and associativity, where:<br>
    - Denial has the greatest precedence.<br>
    - Conjunction and disjunction have the same precedence.<br>
    - Implication has lower precedence than conjunction and disjunction.<br>
    - Conjunction and disjunction associate left.<br>
    - The implication associates right.<br>
    The resulting expression should have as few parentheses as possible, so that the expression displayed as a result has the same semantics as the expression that was passed as an argument to the action.<br>
    For example:<br>
    - ```MOSTRAR PRE | & => true true false true``` should print ```(true => true) & false | true```.<br>
    - ```MOSTRAR POST true false => false | true false ˆ | &``` should print ```(true => false) | false & (true | ˆ false)```.<br>
  3. ```SALIR```<br>
    It must exit the simulator.

At the end of each action, the program must ask the user for the next action.

## Requirements:
To run this program, you must have the following installed:<br>
- Python

## How to install the project
Follow these steps to install the project:
1. **Clone the repository**: Clone the repository using the following git command:<br>
   ```git clone https://github.com/PanquecaFuriosa/Expression-Handler```

## How to run the project
Follow these steps to run the project:
1. **Run the following bash command**:<br>
   ```python ManejadorDeExpresiones.py```
