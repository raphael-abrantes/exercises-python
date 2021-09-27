from math import radians, sin, cos, tan
â = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(â))
cos = cos(radians(â))
tan = tan(radians(â))
if tan > 1000000:
    tan = str('∞')
elif tan < -1000000:
    tan = str('-∞')
print(f'O ângulo {â}° em Radianos é {radians(â):.2f}')
print (f'O seno de {â}° é {sen:.2f};\nO cosseno de {â}° é {cos:.2f};\nA tangente de {â}° é {tan}')
