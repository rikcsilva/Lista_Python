#Converta uma temperatura digitada em Fahrenheit para Celsius. F = 9*C/5 + 32

f = float(input('Fahrenheit: '))
c = (f - 32) * 5 / 9
print ('%.2f Celsius' %c)
