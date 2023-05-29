# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка;Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, 
# либо только русские буквы.
# *Пример:*  ноутбук    12

first_block_letters = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R',
                                    'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
second_block_letters = dict.fromkeys(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2)
third_block_letters = dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
fourth_block_letters = dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы' ], 4)     
fifth_block_letters = dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч' ], 5)
sixth_block_letters = dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8)
seventh_block_letters = dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10)
letter_dict = (first_block_letters | second_block_letters | third_block_letters | fourth_block_letters |
              fifth_block_letters | sixth_block_letters | seventh_block_letters | seventh_block_letters)

print(f"Введите слово:", end = ' ')
word = input().upper()
result = 0

for i in word:
    if i in letter_dict.keys():
        result += letter_dict[i]
print(f"Сумма букв", word, ':', result)