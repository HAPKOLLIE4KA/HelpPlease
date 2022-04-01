import random

def numberTask(x):
    print(f'\nЗадание {x}')

def main():

    numberTask("a")
    list1 = [x for x in range(0,101,10)]
    list2 = [x for x in range(0,101,10)]
    print(list1)
    print(list2)

    numberTask("b")
    secondEl = list1[1]
    print(f"Второй элемент первого списка {secondEl}")

    numberTask("c")
    list2[-1] = 200
    print(list2)

    numberTask("d")
    unionList = list1+list2
    print(unionList)

    numberTask('e')
    sectionList = unionList[int(len(list1)/2):int(len(list2)/2)+len(list1)] #срез от второй половины первого списка до первой половины второго списка
    print(sectionList)

    numberTask('f')
    sectionList += [random.randint(0,100), random.randint(0,100)]
    print(sectionList)

    numberTask("g")
    maxUnionList = max(unionList)
    minUnionList = min(unionList)
    print(f"максимальный {maxUnionList} минимальный {minUnionList}")

if __name__ == "__main__":
    main()