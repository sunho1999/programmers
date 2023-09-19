from collections import deque


def solution(skill, skill_trees):
    # skill 선행스킬트리
    # skill_trees 스킬트리 순서
    answer = 0
    task = []

    for i in skill_trees:
        a = deque(i.strip(""))
        task.append(a)
    # print(task)
    for i in range(len(task)):
        check = True
        new_skill = deque(skill)  # C B D
        for j in task[i]:  # B A C D E
            if j not in new_skill:
                pass
            else:
                alpha = new_skill.popleft()
                if alpha != j:
                    new_skill = deque(skill)
                    check = False
                    break
                elif alpha == j:
                    if len(new_skill) == 0:
                        break
        if check == True:
            answer += 1
    return answer