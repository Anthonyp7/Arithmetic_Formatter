def arithmetic_arranger(l, b):
    
    b = bool(1)
    dash = "-"
    space = " "

    nbr_dash = 0
    space_align = 0

    if b == False:
        print("Réponses masquées !")

    else:

        if len(l) > 5:
            print("Error: Too many problem.")


        else:

            for i in l:
                resultat = eval(i)


                i = i.split(" ")
                nbr1 = i.pop(0)
                ope = i.pop(0)
                nbr2 = i.pop(0)

                nbr1 = int(nbr1)
                nbr2 = int(nbr2)
                
                if ope != "+" and ope != "-":
                    print("Error: Operator must be '+' or '-'.")

                else:
                    if type(nbr1) != int or type(nbr2) != int:
                        print("Error: Numbers must only contain digits.")
                    
                    else:
                        if nbr1 >= 10000 or nbr2 >= 10000:
                            print("Error: Numbers cannot be more than four digits.")
                        
                        else:
                            if nbr1 > nbr2:
                                space_align = len(str(nbr1)) - len(str(nbr2)) + 1
                                nbr_dash = 2 + len(str(nbr1))


                                if len(str(resultat)) >= 5 :
                                    print("  {}\n{}".format(nbr1, ope) + space_align * space + "{}\n".format(nbr2) + nbr_dash * dash + " \n {}".format(resultat) + 4 * space)
                                
                                else :

                                    print("  {}\n{}".format(nbr1, ope) + space_align * space + "{}\n".format(nbr2) + nbr_dash * dash + " \n  {}".format(resultat) + 4 * space)

                            elif nbr1 == nbr2:
                                nbr_dash = 2 + len(str(nbr1))


                                if len(str(resultat)) >= 5 :
                                    print("  {}\n{} {}\n".format(nbr1, ope, nbr2) + nbr_dash * dash + " \n {}".format(resultat) + 4 * space)
                                
                                else :
                                    print("  {}\n{} {}\n".format(nbr1, ope, nbr2) + nbr_dash * dash + " \n  {}".format(resultat) + 4 * space)

                            else:
                                nbr_dash = 2 + len(str(nbr2))
                                space_align = len(str(nbr2)) - len(str(nbr1)) + 1


                                if len(str(resultat)) >= 5 :
                                    print(space_align * space + " {}\n{} {}\n".format(nbr1, ope, nbr2) + nbr_dash * dash + " \n {}".format(resultat) + 4 * space)
                            
                                else :
                                    print(space_align * space + " {}\n{} {}\n".format(nbr1, ope, nbr2) + nbr_dash * dash + " \n  {}".format(resultat) + 4 * space)



    return 