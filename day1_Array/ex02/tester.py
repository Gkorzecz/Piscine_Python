from load_image import ft_load


print("\033[1mSubject Test :\033[0m")
print(ft_load("landscape.jpg"))
print()

print("\033[1mWrong extension (.png) :\033[0m")
print(ft_load("wrong_extension.png"))
print()

print("\033[1mNo extension :\033[0m")
print(ft_load("no_extension"))
print()

print("\033[1mDoes not exist :\033[0m")
print(ft_load("does_not_exist.jpg"))
print()

print("\033[1mInvalid Image:\033[0m")
print(ft_load("invalid_image.jpg"))
print()

print("\033[1mBlack vertical line (10x1, [0,0,0]) :\033[0m")
print(ft_load("black_vert_line.jpg"))
print()

print("\033[1mWhite vertical line (10x1, [255, 255, 255]) :\033[0m")
print(ft_load("white_vert_line.jpg"))
print()

print("\033[1mWhite vertical line (1x10, [255, 255, 255]) :\033[0m")
print(ft_load("white_hori_line.jpg"))
print()

print("\033[1mBlack Square white diagonal(10x10) :\033[0m")
print(ft_load("black_square_white_diag.jpg"))
print()
