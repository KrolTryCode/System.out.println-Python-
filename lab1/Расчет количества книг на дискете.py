# TODO Найдите количество книг, которое можно разместить на дискете
capacity_in_MB = 1.44
capacity_in_B = capacity_in_MB * 1024 * 1024
pages = 100
str_in_page = 50
char_in_line = 25
weight_char_in_B = 4
weight_book_in_B = weight_char_in_B * char_in_line * str_in_page * pages

print("Количество книг, помещающихся на дискету:", "{:.0f}".format(capacity_in_B / weight_book_in_B))
