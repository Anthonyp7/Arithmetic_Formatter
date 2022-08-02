def arithmetic_arranger(l, b):
    
    b = True
    
    if len(l) > 5:
        print("Error: Too many problem.")


    else:

        for i in l:
            resultat = eval(i)


            i = i.split(" ")
            j = i.pop(0)
            k = i.pop(0)
            l = i.pop(0)

            
            if k != "+" and k != "-":
                print("Error: Operator must be '+' or '-'.")

            else:

                print(" {}\n{} {}\n------ \n {} ".format(j, k, l, resultat))



    



    return 


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)