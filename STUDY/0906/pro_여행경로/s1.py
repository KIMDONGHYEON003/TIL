def solution(tickets):
    answer = []
    answer.append(tickets[0][0])
    answer.append(tickets[0][1])
    while len(answer) != len(tickets) + 1:
        for ticket in tickets:
            if answer[-1] == ticket[0]:
                answer.append(ticket[1])

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))