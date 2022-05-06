
import random
import sys
def Str(): return sys.stdin.readline().rstrip()
def Int(): return int(sys.stdin.readline().rstrip())
def Map(): return map(int, sys.stdin.readline().strip().split())
def LstInt(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LstStr(): return list(sys.stdin.readline().rstrip().split())

"""
入力例(総数とグループ数)
10 3
1 8 9 2
3 4 5
6 7 8
⇛5 6 9 3 8 4 1 7 2
"""


def randam_sort(N,group_num):
    lst = [LstInt() for i in range(group_num)]
    random_lst_copy = lst.copy()
    random_list = []
    ans_lst = [-1]
    # shuffle
    for i in range(group_num):
        shuffled = lst[i].copy()
        random.shuffle(shuffled)
        random_list.append(shuffled)
    while len(ans_lst) < N:
        w = [len(i) for i in random_list]
        # print('Before picked_lists',random_list)
        picked_lst = random.choices(random_list, weights=w)
        # print('After picked_lists',random_list)
        not_choice_num_lst = []
        # not_choice_num_lst=[[].extend(l) for l in random_lst_copy if ans_lst[-1] in l]
        for l in random_lst_copy:
            if ans_lst[-1] in l:
                not_choice_num_lst.extend(l)

        if ans_lst[-1] in picked_lst:
            continue
        else:
            picked_num = random.choice(picked_lst[0])
            if picked_num in not_choice_num_lst:
                continue
            else:
                ans_lst.append(picked_num)
                picked_lst[0].remove(picked_num)

    print(*ans_lst[1:])
    return ans_lst[1:]


def main():
    N,Group_num = map(int,input().split())
    lst = randam_sort(N,Group_num)


if __name__ == "__main__":
    main()
