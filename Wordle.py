#Chetan Sidhu WORDLE 4/22/22
import random
#intro/table
def intro():
    line="-"*50
    print()
    print(line)
    print("WORDLE")
    print(line)
    print()
    print("Rules- \nG=In Right Spot\nO=In Word But Not In Right Spot\nW=Not In Word")
    line="-"*21
    print()
    print(line)
    print("| _ | _ | _ | _ | _ |")
    print(line)
    print("| _ | _ | _ | _ | _ |")
    print(line)
    print("| _ | _ | _ | _ | _ |")
    print(line)
    print("| _ | _ | _ | _ | _ |")
    print(line)
    print("| _ | _ | _ | _ | _ |")
    print(line)
    print("| _ | _ | _ | _ | _ |")
    print(line)
    print()
#chooses random word and returns it
def guess():
    words=["abuse", "adult", "agent", "anger", "apple", "award", "basis", "beach", "birth", "block", "blood", "board", "brain", "bread", "break", "brown", "buyer", "cause", "chain", "chair", "chest", "chief", "child", "china", "claim"]
    ra = random.randint(0, 24)
    return words[ra]
#takes user input as a guess for word
def think():
    guess1 = input("Guess a 5 letter word: ")
    while len(guess1) != 5:
        guess1= input("That wasn't 5 letters, guess again! ")
    return guess1
#determines whats incorrect or correct with guess
def tries1(word, first):
    oneslot = "X"
    twoslot = "X"
    threeslot = "X"
    fourslot = "X"
    fiveslot = "X"

    if word[0]==first[0]:
        oneslot = first[0]+"(G)"
    elif word.find(first[0])>0:
        oneslot = first[0]+"(O)"
    elif word[0]!=first[0]:
        oneslot = first[0]+"(W)"

    if word[1]==first[1]:
        twoslot = first[1]+"(G)"
    elif word.find(first[1])>0:
        twoslot = first[1]+"(O)"
    elif word[1]!=first[1]:
        twoslot = first[1]+"(W)"

    if word[2]==first[2]:
        threeslot = first[2]+"(G)"
    elif word.find(first[2])>0:
        threeslot = first[2]+"(O)"
    elif word[2]!=first[2]:
        threeslot = first[2]+"(W)"

    if word[3]==first[3]:
        fourslot = first[3]+"(G)"
    elif word.find(first[3])>0:
        fourslot = first[3]+"(O)"
    elif word[3]!=first[3]:
        fourslot = first[3]+"(W)"

    if word[4]==first[4]:
        fiveslot = first[4]+"(G)"
    elif word.find(first[4])>0:
        fiveslot = first[4]+"(O)"
    elif word[4]!=first[4]:
        fiveslot = first[4]+"(W)"

    if word[0]==first[0] and word[1]==first[1] and word[2]==first[2] and word[3]==first[3] and word[4]==first[4]:
        return "won"
##    if word[0]==first[0]:
##        oneslot = first[0]+"(G)"
##    elif word[1]==first[1]:
##        twoslot = first[1]+"(G)"
##    elif word[2]==first[2]:
##        threeslot = first[2]+"(G)"
##    elif word[3]==first[3]:
##        fourslot = first[3]+"(G)"
##    elif word[4]==first[4]:
##        fiveslot = first[4]+"(G)"
##    elif word.find(first[0])>0:
##        oneslot = first[0]+"(O)"
##    elif word.find(first[1])>0:
##        twoslot = first[1]+"(O)"
##    elif word.find(first[2])>0:
##        threeslot = first[2]+"(O)"
##    elif word.find(first[3])>0:
##        fourslot = first[3]+"(O)"
##    elif word.find(first[4])>0:
##        fivesslot = first[4]+"(O)"
##    elif word[0]!=first[0]:
##        oneslot = first[0]+"(W)"
##    elif word[1]!=first[1]:
##        twoslot = first[1]+"(W)"
##    elif word[2]!=first[2]:
##        threeslot = first[2]+"(W)"
##    elif word[3]!=first[3]:
##        fourslot = first[3]+"(W)"
##    elif word[4]!=first[4]:
##        fiveslot = first[4]+"(W)"

    row = [oneslot, twoslot, threeslot, fourslot, fiveslot]
    return row
#main function, runs the tables and plugs in all other functions
def main():
    intro()
    correct ="n"
    word = guess()
    line="-"*46
    tries= 0
    won = 0
    
    if won == 0:
        first = think()
        row1 = tries1(word, first)
        print()
        if row1 == "won":
            print("WINNER")
            print()
            print(line)
            print("| ", word[0], " | ", word[1], " | ", word[2], " | ", word[3], " | ", word[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            won+=1
        else:
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            tries+=1

    if won == 0:
        first = think()
        row2 = tries1(word, first)
        print()
        if row2 == "won":
            print("WINNER")
            print()
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", word[0], " | ", word[1], " | ", word[2], " | ", word[3], " | ", word[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            won+=1
        else:
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            tries+=1

    if won == 0:
        first = think()
        row3 = tries1(word, first)
        print()
        if row3 == "won":
            print("WINNER")
            print()
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", word[0], " | ", word[1], " | ", word[2], " | ", word[3], " | ", word[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            won+=1
        else:
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            tries+=1

    if won == 0:
        first = think()
        row4 = tries1(word, first)
        print()
        if row4 == "won":
            print("WINNER")
            print()
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| ", word[0], " | ", word[1], " | ", word[2], " | ", word[3], " | ", word[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            won+=1
        else:
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| ", row4[0], " | ", row4[1], " | ", row4[2], " | ", row4[3], " | ", row4[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            tries+=1

    if won == 0:
        first = think()
        row5 = tries1(word, first)
        print()
        if row5 == "won":
            print("WINNER")
            print()
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| ", row4[0], " | ", row4[1], " | ", row4[2], " | ", row4[3], " | ", row4[4], " |")
            print(line)
            print("| ", word[0], " | ", word[1], " | ", word[2], " | ", word[3], " | ", word[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            won+=1
        else:
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| ", row4[0], " | ", row4[1], " | ", row4[2], " | ", row4[3], " | ", row4[4], " |")
            print(line)
            print("| ", row5[0], " | ", row5[1], " | ", row5[2], " | ", row5[3], " | ", row5[4], " |")
            print(line)
            print("| _ | _ | _ | _ | _ |")
            print(line)
            print()
            tries+=1

    if won == 0:
        first = think()
        row6 = tries1(word, first)
        print()
        if row6 == "won":
            print("WINNER")
            tries -=4
            print()
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| ", row4[0], " | ", row4[1], " | ", row4[2], " | ", row4[3], " | ", row4[4], " |")
            print(line)
            print("| ", row5[0], " | ", row5[1], " | ", row5[2], " | ", row5[3], " | ", row5[4], " |")
            print(line)
            print("| ", word[0], " | ", word[1], " | ", word[2], " | ", word[3], " | ", word[4], " |")
            print(line)
            won+=1
        else:
            print(line)
            print("| ", row1[0], " | ", row1[1], " | ", row1[2], " | ", row1[3], " | ", row1[4], " |")
            print(line)
            print("| ", row2[0], " | ", row2[1], " | ", row2[2], " | ", row2[3], " | ", row2[4], " |")
            print(line)
            print("| ", row3[0], " | ", row3[1], " | ", row3[2], " | ", row3[3], " | ", row3[4], " |")
            print(line)
            print("| ", row4[0], " | ", row4[1], " | ", row4[2], " | ", row4[3], " | ", row4[4], " |")
            print(line)
            print("| ", row5[0], " | ", row5[1], " | ", row5[2], " | ", row5[3], " | ", row5[4], " |")
            print(line)
            print("| ", row6[0], " | ", row6[1], " | ", row6[2], " | ", row6[3], " | ", row6[4], " |")
            print(line)
            print()
            tries+=1
    if tries == 6:
        print("You have reached 6 tries, good try! The correct answer is", word+ ". ")
        exit()
    if won ==1:
        print("Good Job, you got the answer in", str(tries+1), "tries!")
        exit()

if __name__ == "__main__":
    main()
