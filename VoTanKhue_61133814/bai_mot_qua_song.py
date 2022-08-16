import time 

names = {"N": "Nông dân",
         "T": "Thỏ",
         "C": "Cáo",
         "B": "Bắp cải"}

forbidden_states = [{"C", "T"}, {"T", "B"}, {"C", "B", "T"}]


def print_story():
    input("Nhấn enter để bắt đầu")


def clear():
    print("*" * 60, "\n")  


def print_state(state):
    left_bank, right_bank = state
    print("#### QUA SÔNG ####")
    print()
    left_bank_display = [names[item] for item in left_bank]
    right_bank_display = [names[item] for item in right_bank]
    print(left_bank_display, "|", right_bank_display if right_bank else "[]")
    print()


def get_move():
    print("Bạn sẽ qua sông cùng với")
    answer = ""
    while answer.upper() not in ["N", "T", "C", "B"]:
        answer = input("Nông dân (N), Thỏ (T), Cáo (C) hoặc Bắp cải (B)? ")

    return answer.upper()


def process_move(move, state):
    temp_state = [state[0].copy(), state[1].copy()]
    containing_set = 0 if move in state[0] else 1
    if "N" not in state[containing_set]:
        print("Di chuyển sai")
        print()
        time.sleep(1)
        return state
    if containing_set == 0:
        temp_state[0].difference_update({move, "N"})
        temp_state[1].update([move, "N"])
    elif containing_set == 1:
        temp_state[1].difference_update({move, "N"})
        temp_state[0].update([move, "N"])
    if temp_state[0] not in forbidden_states and temp_state[1] not in forbidden_states:
        state = [temp_state[0].copy(), temp_state[1].copy()]
    else:
        print("Di chuyển sai.")
        print()
        time.sleep(1)
    print()
    return state


def is_win(state):
    return state[1] == {"N", "T", "C", "B"}


def main():
    left_bank = {"N", "T", "C", "B"}
    right_bank = set()
    state = [left_bank, right_bank]
    print_story()
    while not is_win(state):
        clear()
        print_state(state)
        move = get_move()
        state = process_move(move, state)

    print("Chúc mừng bạn qua sông thành công")


main()