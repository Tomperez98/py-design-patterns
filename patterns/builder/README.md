# Pattern Name: Builder

## How it works

**Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse: scaterred all over the client code.

For example, let's think about how to create a `House` object. To build a simple house, you need to construct four walls and a floor, install a door, fit a pair of windows, and build a roof. But what if you want it to be bigger, brighter house, with a backyard and other goodies (like a heating system, plumbing, and electrical wiring)?

The simplest solution is to extend the base `House` class and create a set of subclasses to cover all combinations of the parameters. But eventually you'll end up with a considerable number of subclasses. Any new parameter, such as the porch style, will require growing this heirarchy even more.

There's another approach that doesn't involve breeding subclasses. You can create a giant constructor right in the base `House` class with all possible parameters that control the house object. While this approach indeed eliminates the need for subclasses, it creates another problem.

In most cases most of the parameters will be unused, making [the constructor calls pretty ugly](https://refactoring.guru/smells/long-parameter-list). For instance, only a fraction of houses have swimming pools, so the parameters releated to swimming pools will be useless nine times out of ten.

The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called *builders*.

The pattern organizes object construction into a set of steps (`buildWalls`, `buildDoor`, etc.). To create an object, you execute a series of steps on a builder object. The important part is that you don't need to call all of the steps. You can only call those steps that are necessary for producing a particular configuration of an object.

Some of the construction steps might require different implementation when you need to build various representations of the product. For example, walls of a cabin may be built of wood, but the castle walls must be built with stone.

In this case, you can create several different builder classes that implement the same set of building steps, but in a different manner. Then you can use these builders in the construction process (i.e., an ordered set of calls to the building steps) to produce different kinds of objects.

For example, imagine a builder that builds everything from wood and glass, a second one that builds everything with stone and iron and a third one that uses gold and diamonds. By calling the same set of steps, you get a regular house from the first builder, a small castle from the second and a palace from the third. However, this would only work if the client code that calls the building steps is able to interact with builders using a common interface.

### Director

You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called ***director***. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.

Having a director class in your program isn't strictly necessary. You can always call the building steps in a specific order directly from the client code. However, the director class might be a good place to put various construction routines so you can reuse them across your program.

In addition, the director class completely hides the details of product construction from the client code. The client only needs to associate a builder with a director, launch the construction with the director, and get the results from the builder.

## Explanatory diagram

```mermaid
classDiagram
    class Builder{
        <<interface>>
        +reset()
        +build_step_a()
        +build_step_b()
        +build_step_z()
    }

    class ConcreteBuilderA{
        +reset()
        +build_step_a()
        +build_step_b()
        +build_step_z()
        +get_result() ProductA
    }

    class ConcreteBuilderB{
        +reset()
        +build_step_a()
        +build_step_b()
        +build_step_z()
        +get_result() ProductB
    }

    class Director{
        -builder Builder
        +director(builder)
        +change_builder(builder)
        +make(type)
    }

    Builder <|-- ConcreteBuilderA
    Builder <|-- ConcreteBuilderB
    Director *-- Builder
```