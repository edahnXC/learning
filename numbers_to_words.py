number=int(input("enter the number: "))
def number_to_words(number):
    ones=["","one","two","three","four","five","six","seven","eight","nine"]
    tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
    teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    in_words=""
    if number <10:
        in_words+=ones[number]
    elif number <20:
        in_words+=teens[number-10]
    elif number >20 and number<100:
        in_words=tens[number//10]
        if number%10>0:
            in_words=tens[number//10]+'-'+ones[number%10]
    elif number>100 and number<1000:
        if number%100==0:
            in_words=ones[number//100]+" hundred"
        # else:
    elif number>1000 and number<10000:
        if number%1000==0:
            in_words=ones[number//1000]+" thousand"
        #else
    elif number>10000 and number<100000:
        if number%10000==0:
            in_words=tens[number//10000]+" thousand"
        #else:
    elif number>100000 and number<1000000:
        if number%100000==0:
            in_words=ones[number//100000]+" lakh"
    elif number==0:
        print("zero")
    elif number==100:
        print("hundred")
    elif number==1000:
        print("thousand")
    elif number==10000:
        print("ten thousand")
    elif number==100000:
        print("one lakh")
    return in_words

in_words=number_to_words(number)
print(in_words)
