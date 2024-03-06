one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "
x = 0
o = 0
win = 0
while one == " " or two == " " or three == " " or four == " " or five == " " or six == " " or seven == " " or eight == " " or nine == " ":
    if o <= x:
        if one == two == three != " " or four == five == six != " " or seven == eight == nine != " " or one == four == seven != " " or two == five == eight != " " or three == six == nine != " " or one == five == nine != " " or three == five == seven != " ":
            print "Player 2 wins."
            one = "X"
            two = "X"
            three = "X"
            four = "X"
            five = "X"
            six = "X"
            seven = "X"
            eight = "X"
            nine = "X"
            win = 1
        else:
            print "1|2|3"
            print "-+-+-"
            print "4|5|6"
            print "-+-+-"
            print "7|8|9"
            move = input("Player 1: Make your move. ")
            if move == 1:
                if one == " ":
                    one = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 2:
                if two == " ":
                    two = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 3:
                if three == " ":
                    three = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 4:
                if four == " ":
                    four = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 5:
                if five == " ":
                    five = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 6:
                if six == " ":
                    six = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 7:
                if seven == " ":
                    seven = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 8:
                if eight == " ":
                    eight = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            elif move == 9:
                if nine == " ":
                    nine = "O"
                    o = o+1
                else:
                    print "That's cheating!"
            else:
                print "Invalid input."
            print one, "|", two, "|", three
            print "--+---+--"
            print four, "|", five, "|", six
            print "--+---+--"
            print seven, "|", eight, "|", nine
            print
    elif o > x:
            if one == two == three != " " or four == five == six != " " or seven == eight == nine != " " or one == four == seven != " " or two == five == eight != " " or three == six == nine != " " or one == five == nine != " " or three == five == seven != " ":
                print "Player 1 wins."
                one = "O"
                two = "O"
                three = "O"
                four = "O"
                five = "O"
                six = "O"
                seven = "O"
                eight = "O"
                nine = "O"
                win = 1
            else:
                print "1|2|3"
                print "-+-+-"
                print "4|5|6"
                print "-+-+-"
                print "7|8|9"
                move = input("Player 2: Make your move. ")
                if move == 1:
                    if one == " ":
                        one = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 2:
                    if two == " ":
                        two = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 3:
                    if three == " ":
                        three = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 4:
                    if four == " ":
                        four = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 5:
                    if five == " ":
                        five = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 6:
                    if six == " ":
                        six = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 7:
                    if seven == " ":
                        seven = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 8:
                    if eight == " ":
                        eight = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                elif move == 9:
                    if nine == " ":
                        nine = "X"
                        x = x+1
                    else:
                        print "That's cheating!"
                else:
                    print "Invalid input."
                print one, "|", two, "|", three
                print "--+---+--"
                print four, "|", five, "|", six
                print "--+---+--"
                print seven, "|", eight, "|", nine
                print
if win != 1:
    if one == two == three != " " or four == five == six != " " or seven == eight == nine != " " or one == four == seven != " " or two == five == eight != " " or three == six == nine != " " or one == five == nine != " " or three == five == seven != " ":
        print "Player 1 wins."
    else:
        print "Cat, the board is full"