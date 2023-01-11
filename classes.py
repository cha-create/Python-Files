

class Socks:
    def __init__(self, color, size, material):
        self.color = color
        self.size = size
        self.material = material

sock_1 = Socks('red', 11, 'cotton')
sock_2 = Socks('white', 15, 'spandex')
print('Hello, and welcome to the sock emporium. my name is GIGACHAD. To see the attributes of certian socks, either enter 1, or 2. to further inspect the socks, enter either: material, size, or color. Have Fun!')
selection_1 = input()
if selection_1 == '1':
    print('You selected sock one!')
    selection_2 = input()
    if selection_2 == 'material':
        print(sock_1.material)
    if selection_2 == 'size':
        print(sock_1.size)
    if selection_2 == 'color':
        print(sock_1.color)
if selection_1 == '2':
    print('You selected sock two!')
    selection_3 = input()
    if selection_3 == 'material':
        print(sock_2.material)
    if selection_3 == 'size':
        print(sock_2.size)
    if selection_3 == 'color':
        print(sock_2.color)
        