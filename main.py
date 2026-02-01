from function import space , even , odd , show_history , save_history

history = []

while True:

        option = input("Choose one option\n"
        "----------------------------\n"
        "1- Range and Odd or Even\n"
        "2- See Before Informations\n"
        "3- Exit\n"
        "----------------------------\n"
        "Option: ")
        space()


        if option == "1":

            range = input("Choose range (ex: 1,10): ")

            start, end = [int(delete_space.strip()) for delete_space in range.split(",")]

            choose = input("Choose Odd or Even: ").lower()

            if choose == "odd":
                    result = odd(start, end)
                    space()
                    print(result)
            elif choose == "even":
                    result = even(start, end)
                    space()
                    print(result)
            else:
                print("You don't choose 'odd' or 'even'")

            save_history(history, start, end, choose, result)

            space()

            again = input("Do you whant to be continue or exit (Continue/Exit): ").lower()

            if again == "continue":
                print("")

            else:
                print("Goodbye !\n")
                break
        
        elif option == "2":
                show_history(history)
                "\n"
                space()

        elif option == "3":
            print("Goodbye !\n")
            break

        else:
            print("You don't choose any option !")
            space()