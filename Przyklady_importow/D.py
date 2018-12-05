from A import foo as foo_z_A   #bierzemy tylko wycinek A
from B import foo as foo_z_B  #inaczej foo sie pomieszaja i zostanie tylko z B

foo_z_A()
foo_z_B()
