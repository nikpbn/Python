cnt = 1
sum = 0

while(True):
    # print()
    user_input = input("Enter Value for item Or Q to exit:")
    cnt +=1
    if user_input.upper() != 'Q':
        num = int(user_input)
        sum = sum+num

    else:
        print("------------------------------------")
        print("Total Items= ", cnt)
        print("Total bill= ", sum)
        break
print("Thank You for shopping with us")