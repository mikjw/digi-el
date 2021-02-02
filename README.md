## digi-el

This project began as simply using Python and its REPL to learn about logic gates, but it now has ambitions to become a more interesting CLI tool to build and simulate digital circuits (currently experimenting with ncurses for an interface).

Core components `Line` and `Container` allow logic gates such as `Nand` to be combined in circuits, and LOW and HIGH signals introduced to experiment with the results. Currently builds are largely manual - See half-adder.py for an example - but this will be taken care of based on user input from the interface. 

Currently, new `Containers` are declared with input and output counts, with compnents connected by lines to each internally. `Containers` are designed to be flexible and allow encapsulation of components of varying size. A `Printer` class takes an outer `Container` as its soure component, checks its outputs and print whatever signals they pass it. 

Currently signals must be introduced to the inputs of an outer container manually using a line connected to each, calling inputting with `receive_signal(signal)`.

Components built lovingly using TDD with `pytest`.

