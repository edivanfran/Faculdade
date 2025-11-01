a, b, c, d = 2, 3 , 6, 23
média = (a + b + c + d) / 4

maior = a > média and a
maior = b > média and b
maior = c > média and c
maior = d > média and d

maior = maior > média

print(f"Média deles é: {maior}")