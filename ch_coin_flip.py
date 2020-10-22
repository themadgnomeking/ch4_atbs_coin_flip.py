#create a coin flip protram
#track how many six streak of heads or tails happens in a given game
#generate a list of H - for heads, and T - for tails
#generate a number count of how many times a 6 streak of either heads or tails comes up

#example code
import random

numberOfStreaks = 0
head_tail_list = []
ht_master_list = []
average_count = 100
head_count = 0
tail_count = 0

for experimentNumber in range(10000):
    head_tail_result = random.randint(0,1)
    # Code that creates a list of 100 'heads' or 'tails' values.
    if head_tail_result == 0 and average_count != 0:
        head_tail_list.append('H')
        average_count -= 1
        head_count += 1
        tail_count = 0

    elif head_tail_result == 1 and average_count != 0:
        head_tail_list.append('T')
        average_count -= 1
        head_count = 0
        tail_count += 1

    elif average_count == 0:
        average_count = 100
        numberOfStreaks = 0
        ht_master_list.append(head_tail_list)
        head_tail_list = []

    # Code that checks if there is a streak of 6 heads or tails in a row.
    if head_count >= 6 or tail_count >= 6:
        numberOfStreaks = numberOfStreaks + 1

    print('Chance of streak: %s%%' % (numberOfStreaks / 1))
    #print('average count: ' + str(average_count) + ' number of streaks: ' + str(numberOfStreaks) + ' heads counted: ' + str(head_count) + ' tails counted: ' + str(tail_count))
#example code
