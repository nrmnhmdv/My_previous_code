print("Global Local Variables Part1")
#Local And Global Variables


def times_ten(x):
    """Multiply a number by 10"""
    print("Current value ",str(x))
    x*=10
    print("Updated values ",str(x))
    return x


def char_replace(word):
    """Replace specific characters in a string with other chracters"""
    while 'a'in word:
        word=word.replace('a','@')
    while 'e' in word:
        word =word.replace('e','3')
    while 'i' in word:
        word=word.replace('i','!')
    while 'o'in word :
        word=word.replace('o','0')
    while 'u' in word:
        word=word.replace('u','#')
    #print(word) olduqda hec bir deyisene menimsetmeye ehtiyac qalmir ve
    # phrase ifadesi deyismir lakin retun ile deyisir
    return word




number = 3
print(number) # menimsedilme edildikden sonra number in qiymeti deyisir 
number=times_ten(number)
print("Number is ",number)

#Global variable 
phrase="Hello how are you doing today ? "
phrase1=char_replace(phrase)
print(phrase)
print(phrase1)
