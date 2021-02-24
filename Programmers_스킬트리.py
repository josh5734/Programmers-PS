def checkSkillTree(skill, skill_tree):
    # 선행스킬이 필요없는 스킬트리들은 그냥 True
    if len(skill_tree) == 0:
        return True
    # 처음 기술로 안 시작하면 False
    if skill[0] != skill_tree[0]:
        return False

    # 배운 스킬들을 체크하는 리스트
    skill_acquired = [False] * len(skill)
    cursor = 0
    for s in skill_tree:
        skill_idx = skill.find(s)
        # 스킬을 건너 뛰어서 배우는데, 이 상황이 이미 선행스킬들을 익혀놓은 상태가 아닌경우에는 False Ex. CBDCC는 가능함
        if skill_idx - cursor > 1 and not all(skill_acquired[:skill_idx]):
            return False
        # 배운 스킬은 체크
        skill_acquired[skill_idx] = True
    return True


def solution(skill, skill_trees):
    answer = 0

    # 선행 스킬들의 관계만 모아두는 새로운 skill_trees
    valid_skill_trees = []
    for st in skill_trees:
        temp = ""
        for s in st:
            if s in skill:
                temp += s
        valid_skill_trees.append(temp)

    for st in valid_skill_trees:
        if checkSkillTree(skill, st) == True:
            answer += 1
    return answer


if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "CD", "CBDBB", "CBBBB"]
    skill_trees2 = ["AECB"]

    # print(solution(skill, skill_trees))
    print(solution(skill, skill_trees2))
