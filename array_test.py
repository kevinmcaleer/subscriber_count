font = { 'a' : [0b01110,
     0b10001,
     0b11111,
     0b10001,
     0b10001,],
     'b' : [
         0b1000,
         0b1110,
         0b1001,
         0b1000,
         0b1110,
     ],
     }

message = 'ab'
for char in message:
    if char in font:
        print(f"found {char}")
        for row in font.get(char):
            digits = bin(row).lstrip('0b')
            print(digits)
            for digit in digits :
                print(digit)