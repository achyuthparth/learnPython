# python3
#design o(n) algorithm instead of o(nm)

def max_sliding_window_naive(sequence, m):
    closeWindow = 0
    maximums = []
    maxQueue = []
    for i in range(len(sequence)):
        if maxQueue is not None:
            while sequence[maxQueue[-1]] < sequence[i]:
                del maxQueue[-1]
        maxQueue.append(sequence[i])
        if closeWindow > maxQueue[0]:
            del maxQueue[0]
        if closeWindow + i >= m:
            maximums.append(sequence[maxQueue[0]])
            closeWindow += 1
    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(max_sliding_window_naive(input_sequence, window_size))