## digi-el

This project began as simply using Python and its REPL to learn about logic gates, but now has ambitions of becoming a more interesting CLI tool to build and simulate digital circuits (currently experimenting with ncurses to build the interface).

Core components `Line` and `Container` allow logic gates such as `Nand` to be combined in circuits, with LOW and HIGH signals introduced to experiment with the results. Currently, builds are largely manual - See half-adder.py for an example - but in future they will be automated based on user input. 

Currently, new `Containers` are declared with input and output counts, and components connected by lines to each of these terminals internally. `Containers` are designed to be flexible and to allow encapsulation of components of varying size. A `Printer` class can take an outer `Container` as its source component, check its outputs and print whatever signals they pass to it. 

Currently signals must be introduced to the inputs of an outer container manually using lines, calling `receive_signal(signal)` on each.

All components built lovingly using TDD with `pytest`.

