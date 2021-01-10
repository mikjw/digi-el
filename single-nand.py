from src import line, nand, container, printer

c1 = container.Container(2, 1)
n1 = nand.Nand()

l0_0 = line.Line()
l0 = line.Line()
l1 = line.Line()
l2 = line.Line()
l3 = line.Line()

l0_0.connect_next(c1, 'A', 'A')
l0.connect_next(c1, 'A', 'B')

c1.connect_within(l1, 'A')
c1.connect_within(l2, 'B')

l1.connect_next(n1, 'A', 'A')
l2.connect_next(n1, 'A', 'B')

n1.connect_next(l3)

l3.connect_next(c1, 'A', 'Z')

p1 = printer.Printer(c1)

