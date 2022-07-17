str=str(input('Type your text '))
output1=str.lower()[0:5]+'...'
output2=str.upper()[0:5]+'...'
# якщо довжина строчки більше 5 та строчка починається з u/U
if len(str)>5 and (str.startswith('u') or str.startswith('U')):
 print(output2)
# якщо довжина строчки більше 5 та строчка починається з l/L
elif len(str)>5 and (str.startswith('l') or str.startswith('L')):
 print (output1)
# якщо довжина строчки більше 5
elif len(str)>5:
 print(str[0:5]+'...')
# Якщо перша літера строчки U/u 
elif str.startswith('u') or str.startswith('U'):
 print(str.upper()) 
# Якщо перша літера строчки L/l
elif str.startswith('l') or str.startswith('L'):
 print(str.lower())

else: print(str)

    
