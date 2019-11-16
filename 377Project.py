import random
from time import sleep

def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def inBuffer(bufflist):
    for inBuffer in range(bufflist):
        inBuffer = random.randint(0, totvm)
        pages.append(inBuffer)



def printpages(pages):
    print("\nPages in Buffer: ", end=" ")
    for x in pages:
        print(x, end=" ")
    print("")
    input("\n\nPress Enter to continue")


def quick_fifo(pages):
    cpu = list(())
    old = 0
    pg_fault = 0
    for x in pages:
        if old >= pgframe:
            old = 0
        if x not in cpu:
            pg_fault += 1
            if len(cpu) >= pgframe:
                cpu[old] = x
                old += 1
            else:
                cpu.append(x)
    print("\n\n\t%d | FIFO Page Faults" % pg_fault)


def fifo(pages):
    cpu = list(())
    old = 0
    pg_fault = 0
    for x in pages:
        if old >= pgframe:
            old = 0
        if x in cpu:
            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                cpu[old] = x
                d = x
                old += 1
                for x in cpu:
                    print(x, end=" ")
                print("  <-- Here we load in page frame %d (oldest page) with the new page %d" % (old, d), end="")
            else:
                cpu.append(x)
                for x in cpu:
                    print(x, end=" ")
        sleep(0.25)
    print("\n\n\tFIFO Page Faults = %d" % pg_fault)


def optimal(pages):
    cpu = list(())
    copypage = pages.copy()
    my_book = list(())
    pg_fault = 0
    for x in pages:
        pgindex = x
        if x in cpu:
            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                base = 0
                my_book.clear()
                for y in cpu:
                    pgincpu = y
                    if y not in copypage:
                        cpu[base] = pgindex
                        for x in cpu:
                            print(x, end=" ")
                        print("  <--We replace page frame %d with %d because it isn't seen in our inBuffer again" % (
                            base + 1, pgindex), end="")
                        break
                    elif y in copypage:
                        val = copypage.index(y)
                        my_book.append(val)
                        val += 1
                        base += 1
                        if base == pgframe:
                            maxi = max(my_book)
                            x = my_book.index(maxi)
                            cpu[x] = pgindex
                            for x in cpu:
                                print(x, end=" ")
                            print(
                                "  <--We replace page frame %d with %d because everything else will be used sooner" % (
                                base, pgindex), end="")

            else:
                cpu.append(x)
                for x in cpu:
                    print(x, end=" ")
        copypage.pop(0)
        sleep(0.25)
    print("\n\n\tOPTIMAL Page Faults = %d" % pg_fault)


def quick_optimal(pages):
    cpu = list(())
    copypage = pages.copy()
    my_book = list(())
    pg_fault = 0
    for x in pages:
        pgindex = x
        if x in cpu:
            x = x
        else:
            pg_fault += 1
            if len(cpu) >= pgframe:
                base = 0
                my_book.clear()
                for y in cpu:
                    pgincpu = y
                    if y not in copypage:
                        cpu[base] = pgindex
                        break
                    elif y in copypage:
                        val = copypage.index(y)
                        my_book.append(val)
                        val += 1
                        base += 1
                        if base == pgframe:
                            maxi = max(my_book)
                            x = my_book.index(maxi)
                            cpu[x] = pgindex
            else:
                cpu.append(x)
        copypage.pop(0)
    print("\t%d | Optimal Page Faults" % pg_fault)


def second(pages):
    cpu = list(())
    my_book = list(())
    my_timer = list(())
    time = 0
    tpoint = 0
    pg_fault = 0
    t = 0

    for x in pages:
        pgindex = x
        if x in cpu:
            base = cpu.index(pgindex)
            my_book[base] = 1
            base = my_timer.index(base)
            tpoint = my_timer[base]

            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                x = 1
                while x == 1:
                    base = my_timer[tpoint]
                    if my_book[base] == 1:
                        my_book[base] = 0
                        base += 1
                        t += 1
                        tpoint += 1

                        if base == pgframe:
                            base = 0
                        if tpoint == pgframe:
                            tpoint = 0
                    else:
                        cpu[base] = pgindex
                        my_book[base] = 1
                        base = my_timer.index(base)
                        val = my_timer[base]
                        my_timer.pop(base)
                        my_timer.append(val)
                        if tpoint == pgframe:
                            tpoint = 0
                        for x in cpu:
                            print(x, end=" ")
                        print("  <--Page Frame %d will be replaced with Program Page %d" % (val + 1, pgindex), end="")

                        break
            else:
                cpu.append(x)
                my_book.append(1)
                my_timer.append(time)
                time += 1
                tpoint = cpu.index(x)
                for x in cpu:
                    print(x, end=" ")
        sleep(0.25)
    print("\n\n\tSecond-Chance Page Faults = %d" % pg_fault)


def quick_second(pages):
    cpu = list(())
    my_book = list(())
    my_timer = list(())
    time = 0
    tpoint = 0
    pg_fault = 0
    t = 0

    for x in pages:
        pgindex = x
        if x in cpu:
            base = cpu.index(pgindex)
            my_book[base] = 1
            base = my_timer.index(base)  # position
            tpoint = my_timer[base]

        else:
            pg_fault += 1

            if len(cpu) >= pgframe:
                x = 1
                while x == 1:
                    base = my_timer[tpoint]
                    if my_book[base] == 1:
                        my_book[base] = 0
                        base += 1
                        t += 1
                        tpoint += 1

                        if base == pgframe:
                            base = 0
                        if tpoint == pgframe:
                            tpoint = 0
                    else:
                        cpu[base] = pgindex
                        my_book[base] = 1
                        base = my_timer.index(base)
                        val = my_timer[base]
                        my_timer.pop(base)
                        my_timer.append(val)
                        if tpoint == pgframe:
                            tpoint = 0

                        break
            else:
                cpu.append(x)
                my_book.append(1)
                my_timer.append(time)
                time += 1
                tpoint = cpu.index(x)

    print("\t%d | Second-Chance Page Faults" % pg_fault)


def lru(pages):
    cpu = list(())
    my_book = list(())
    pg_fault = 0
    pos = 0

    for x in pages:
        pgindex = x
        if x in cpu:
            val = cpu.index(pgindex)
            base = my_book.index(val)
            my_book.pop(base)
            my_book.append(val)

            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                val = my_book[0]
                base = my_book.index(val)
                my_book.pop(base)
                my_book.append(val)
                cpu[val] = pgindex
                for x in cpu:
                    print(x, end=" ")
                print(
                    "  <--Page Frame %d will be replaced with Program Page %d because its the Least Recently Used " % (
                    val + 1, pgindex), end="")

            else:
                cpu.append(x)
                my_book.append(pos)
                pos += 1
                for x in cpu:
                    print(x, end=" ")
        sleep(0.25)
    print("\n\n\tLeast Recently Used Page Faults = %d" % pg_fault)


def quick_lru(pages):  # Each page start withs 2
    cpu = list(())  # Each page decreses 0.4 on each tick
    my_book = list(())  # use minimization to find the smallest value
    pg_fault = 0
    pos = 0

    for x in pages:
        pgindex = x
        if x in cpu:  # if it is in the frames
            val = cpu.index(pgindex)  # The position of the vaule in CPU
            base = my_book.index(val)  # The position of the position of the value
            my_book.pop(base)
            my_book.append(val)
        else:
            pg_fault += 1
            if len(cpu) >= pgframe:
                val = my_book[0]
                base = my_book.index(val)
                my_book.pop(base)
                my_book.append(val)
                cpu[val] = pgindex
            else:
                cpu.append(x)
                my_book.append(pos)
                pos += 1
    print("\t%d | Least Recently Used Page Faults" % pg_fault)


def aging(pages):  # Each page start withs 2
    birth = 2  # 100 VM        20 pgframe    50buff
    die_rate = 0.05
    revive_rate = 2
    cpu = list(())  # Each page decreses 0.4 on each tick
    my_book = list(())  # use minimization to find the smallest value
    pg_fault = 0

    for x in pages:
        pgindex = x
        if x in cpu:  # if it is in the frames
            base = cpu.index(pgindex)  # find the index
            my_book[base] += revive_rate  # add 1.2 to that index's time

            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                base = min(my_book)  # compare values for min
                val = my_book.index(base)  # Index smallest time
                my_book[val] = birth  # Reset time to new page
                cpu[val] = pgindex  # Reset page to new page
                for x in cpu:
                    print(x, end=" ")
                print("  <--Page Frame %d will be replaced with Program Page %d because its the Oldest Page " % (
                val + 1, pgindex), end="")

            else:
                cpu.append(x)
                my_book.append(birth)
                for x in cpu:
                    print(x, end=" ")
        my_book[:] = [x - die_rate for x in my_book]
        sleep(0.25)
    print("\n\n\tAging Page Faults = %d" % pg_fault)


def quick_aging(pages):  # Each page start withs 2
    birth = 2  # 100 VM        20 pgframe    50buff
    die_rate = 0.05
    revive_rate = 2
    cpu = list(())  # Each page decreses 0.4 on each tick
    my_book = list(())  # use minimization to find the smallest value
    pg_fault = 0

    for x in pages:
        pgindex = x
        if x in cpu:  # if it is in the frames
            base = cpu.index(pgindex)  # find the index
            my_book[base] += revive_rate  # add 1.2 to that index's time

        else:
            pg_fault += 1

            if len(cpu) >= pgframe:
                base = min(my_book)  # compare values for min
                val = my_book.index(base)  # Index smallest time
                my_book[val] = birth  # Reset time to new page
                cpu[val] = pgindex  # Reset page to new page

            else:
                cpu.append(x)
                my_book.append(birth)

        my_book[:] = [x - die_rate for x in my_book]
    print("\t%d | Aging Page Faults" % pg_fault)


def quick_random(pages):
    cpu = list(())  # Each page decreses 0.4 on each tick
    pg_fault = 0
    for x in pages:
        pgindex = x
        if x in cpu:
            x = x
        else:
            pg_fault += 1
            if len(cpu) >= pgframe:
                val = random.randint(0, pgframe - 1)
                cpu[val] = pgindex
            else:
                cpu.append(x)
    print("\t%d | Random Page Faults" % pg_fault)


def Random(pages):
    cpu = list(())  # Each page decreses 0.4 on each tick
    pg_fault = 0

    for x in pages:
        pgindex = x
        if x in cpu:
            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                val = random.randint(0, pgframe - 1)
                cpu[val] = pgindex
                for x in cpu:
                    print(x, end=" ")
                print("  <--Randomly, Page Frame %d will be replaced with Program Page %d " % (
                    val + 1, pgindex), end="")

            else:
                cpu.append(x)
                for x in cpu:
                    print(x, end=" ")
            sleep(0.25)
    print("\n\n\tRandom Page Faults = %d" % pg_fault)


def nfu(pages):  # Copy Pages List, make into a set, make a list to the same size for counter
    cpu = list(())  # Each time a page is seen, it is counted
    my_book = list(())
    my_list = list(())
    pg_fault = 0
    copypage = pages.copy()
    copypage = remove(copypage)

    for x in pages:
        pgindex = x

        if x in cpu:  # if it is in the frames
            base = copypage.index(pgindex)
            my_book[base] += 1
            print("\nNo Fault!  ", end="")
            for x in cpu:
                print(x, end=" ")
        else:
            pg_fault += 1
            print("\nFault!    ", end=" ")
            if len(cpu) >= pgframe:
                t = 0
                my_list.clear()
                while t != pgframe:
                    val = cpu[t]
                    base = copypage.index(val)
                    val = my_book[base]
                    my_list.append(val)  # my list will have mybook values to transfer back to cpu
                    t += 1
                val = min(my_list)
                base = my_list.index(val)
                cpu[base] = pgindex
                base = copypage.index(pgindex)
                val = cpu.index(pgindex)
                if len(my_list) - 1 < copypage.index(pgindex):
                    my_book.append(0)
                    my_book[base] += 1
                else:
                    my_book[base] += 1

                for x in cpu:
                    print(x, end=" ")
                print("  <--Page Frame %d will be replaced with Program Page %d because its Not Frequently Used " % (
                val + 1, pgindex), end="")

            else:
                cpu.append(x)
                base = copypage.index(pgindex)
                my_book.append(0)
                my_book[base] += 1
                for x in cpu:
                    print(x, end=" ")
        sleep(0.25)
    print("\n\n\tNot Frequently Used Page Faults = %d" % pg_fault)


def quick_nfu(pages):  # Copy Pages List, make into a set, make a list to the same size for counter
    cpu = list(())  # Each time a page is seen, it is counted
    my_book = list(())
    my_list = list(())
    pg_fault = 0
    copypage = pages.copy()
    copypage = remove(copypage)
    for x in pages:
        pgindex = x

        if x in cpu:  # if it is in the frames
            base = copypage.index(pgindex)
            my_book[base] += 1

        else:
            pg_fault += 1
            if len(cpu) >= pgframe:
                t = 0
                my_list.clear()
                while t != pgframe:
                    val = cpu[t]
                    base = copypage.index(val)
                    val = my_book[base]
                    my_list.append(val)  # my list will have mybook values to transfer back to cpu
                    t += 1
                val = min(my_list)
                base = my_list.index(val)
                cpu[base] = pgindex
                base = copypage.index(pgindex)
                if len(my_list) - 1 < copypage.index(pgindex):
                    my_book.append(0)
                    my_book[base] += 1
                else:
                    my_book[base] += 1
            else:
                cpu.append(x)
                base = copypage.index(pgindex)
                my_book.append(0)
                my_book[base] += 1

    print("\t%d | NFU" % pg_fault)


def vmi():
    print("\n\n")
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n_____________________________________________________________________________________")
    print("_______________________VIRTUAL MEMORY REPRESENTATION________________________________\n\n\n\n\n")
    vmpa.clear()
    c = pgframe * 2
    d = c + 2
    for i in range(pgframe, totvm):
        vmpa.append("\r" + "[]{}K-{}K".format(c, d))
        c += 2
        d += 2
    for i in reversed(vmpa):
        print(i)
    vmpa.clear()
    c = pgframe * 2
    d = c + 2

    for i in range(0, pgframe):
        c -= 2
        d -= 2
        print("[]%dK-%dK" % (c, d), end="")

        print("\t\t\t\t\t[]{0}K-{1}K".format(c, d))

    print(
        "\nProgram Memory\t\t\tCPU Memory \n\n\nThis program requires %d pages of memory and we have %d Page Frames " % (
        totvm, pgframe))
    input("\n\nPress Enter To Continue")


def intro():
    input("\n\n\nPlease use full screen and press enter to start program")



pgframe = 3
bufflist = 15
pages = []
vmpa = []
totvm = 0
vm = 7

totvm = (vm)
inBuffer(bufflist)
intro()
choice = 's'
while choice == 's' or 'q':
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n_____________________________________________________________________________________")
    print("_______________________________SIMULATION MENU_______________________________________")
    print("                                                                    PageFrames: %d" % (pgframe))
    print("                                                                      VM Pages: %d" % (totvm))
    print("                                                                 PagesInBuffer: %d" % (bufflist))
    print("\n\tALGORITHMS")
    print("\t\t\t\tf| Fifo Simulation")
    print("\t\t\t\to| Bélády's Optimal Simulation")
    print("\t\t\t\tu| Least Recently Used")
    print("\t\t\t\ts| Second-Chance (Clock) Simulation")
    print("\t\t\t\ta| Austin's Aging Simulation")
    print("\t\t\t\tr| Random Replacement Simulation")
    print("\t\t\t\tn| Not Frequently Used Simulation")
    print("\n\tDEV'S FAVORITES")
    print("\t\t\t\tq| Quick Results     ")
    print("\t\t\t\ty| Bélády's Anomaly")
    print("\t\t\t\tv| Virtual Memory Representation")
    print("\t\t\t\tc| Customize Parameters")
    print("\n\tEXIT")
    print("\t\t\t\te| Exit              ")
    print("\n\tPress your choice and enter:\n\n\t", end="")

    choice = input()
    if choice == 'y':
        print(
            "\n\n\n\t\tBélády's anomaly is the phenomenon in which increasing the number of page frames \n\t\tresults in an increase in the number of page faults "
            "for certain memory access patterns.\n\t\tIn FIFO, the page fault may or may not increase as the page frames increase,\n\t\t"
            "but in Optimal and stack-based algorithms like LRU, \n\t\tas the page frames increase the page fault decreases. \n\t\tLászló Bélády demonstrated this in 1969")

        input("\n\nPress Enter To Continue")
    if choice == 'c':
        print("\n\n\n\t_________PARAMETERS_______________")
        print("\t\t\t\tp| Change # of Page Frames     ")
        print("\t\t\t\tm| Change # of VM Pages   ")
        print("\t\t\t\tb| Change # of Pages inBuffer  ")
        print("\t\t\t\ti| See Pages inBuffer     ")
        print("\n\tPress your choice and enter:\n\n\t", end="")
        choice = input()
    if choice == 'f':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("________________FIFO________________")
        print("\n\nFIFO stands for 'First In, First Out. This FIFO simulation replaces the page that is the oldest.")

        printpages(pages)
        fifo(pages)
        sleep(1)
        print(input("\nPress Enter for the menu.."), end="")
    if choice == 's':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("____________Second Chance___________")
        print(
            "\n\nSecond Chance gives each page a reference value of 1 when the page is used. It cycles through and marks 1's to be 0 until it finds a 0 and replaces that page frame ")
        printpages(pages)
        second(pages)
        sleep(1)
        print(input("\nPress Enter for the menu.."), end="")
    if choice == 'a':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("_______________Aging________________")
        print(
            "\n\nAging algorithm gives each page a value and each pass of iteration that vaule is decreased, the page with the lowest value will be replaced"
            "\nEach page starts it/'s life with 2 and decreases each time by 0.4, when the page is referenced again it gets 1 added")
        printpages(pages)
        aging(pages)
        sleep(1)
        print(input("\nPress Enter for the menu.."), end="")
    if choice == 'q':
        printpages(pages)
        print("\n\t_____Quick Page Fault Results______", end="")
        quick_fifo(pages)
        quick_optimal(pages)
        quick_second(pages)
        quick_lru(pages)
        quick_aging(pages)
        quick_random(pages)
        quick_nfu(pages)
        sleep(1)
        print(input("\nPress Enter for the menu.."), end="")
    if choice == 'o':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("______________Optimal_______________")
        print(
            "\n\nBélády's Optimal simulation looks into the future and replaces the page that won't be used for the longest time and replaces that page")
        printpages(pages)
        optimal(pages)
        sleep(1)
        print(input("\nPress Enter for the menu.."), end="")
    if choice == 'i':
        printpages(pages)
    if choice == 'b':
        pages.clear()
        bufflist = int(input(
            "\n\n\tNOTE: Buffering in 100,000+ pages will take considerably more computing time\n\n\tHow many pages do you want to buffer in?: "))
        inBuffer(bufflist)

    if choice == 'r':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("______________Random_______________")
        print("\n\nRandom replacement algorithm replaces a random page in memory")
        printpages(pages)
        Random(pages)
        sleep(1)
        print(input("\nPress Enter for the menu.."), end="")
    if choice == 'n':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("________________NFU_________________")
        print(
            "\n\nNot Frequently Used simulation counts the amount of times the page has been used and replaces the page with the lowest count")
        printpages(pages)
        nfu(pages)
        sleep(1)
    if choice == 'u':
        print(
            "\n\n\n\n\n\n\n\n\n\n\n\n____________________________________")
        print("________________LRU_________________")
        print("\n\nLeast Recently Used simulation replaces the page that hasn't been used for the longest time")
        printpages(pages)
        lru(pages)
        sleep(1)

        print(input("\nPress Enter for the menu.."), end="")
    if choice == "v":
        vmi()

    if choice == "m":
        totvm = int(input("\n\n\tWhat size would you like the program to be? "))
    if choice == "p":
        pgframe = int(input("\n\tHow many frames would you like?: "))

    if choice == 'e':
        break








