def chnage_name(info, userid, name):
    for v in info[userid]:
        v[2] = name


def make_log(info):
    log = []
    for k in info.keys():
        for value in info[k]:
            order, action, name = value[0], value[1], value[2]
            log.append((order, action, name))
    log = sorted(log)

    result = []
    for l in log:
        if l[1] == "Enter":
            result.append(f'{l[2]}님이 들어왔습니다.')
        elif l[1] == 'Leave':
            result.append(f'{l[2]}님이 나갔습니다.')
    return result


def solution(record):
    info = {}
    order = 1

    for r in record:
        r = list(r.split())
        action = r[0]
        userId = r[1]
        if action == "Enter":
            userName = r[2]
            # 이미 방문 기록이 있을 때
            if info.get(userId):
                chnage_name(info, userId, userName)
                info[userId].append([order, action, userName])
            # 처음 방문
            else:
                info[userId] = []
                info[userId].append([order, action, userName])
        elif action == "Leave":
            # 이미 기록된 유저 이름을 사용
            name = info[userId][0][2]
            info[userId].append([order, action, name])

        # userId에 해당하는 모든 NAME의 기록을 변경
        elif action == "Change":
            changeName = r[2]
            for v in info[userId]:
                v[2] = changeName
        order += 1
    return make_log(info)
