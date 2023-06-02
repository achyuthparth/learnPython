# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.queue = []

    def process(self, request):
        # write your code here
        startTime = 0 if self.finish_time == [] else self.finish_time[-1]
        endTime = request[1] + max(startTime, request[0])
        if self.queue != []:
            while self.queue[0] < startTime:
                del self.queue[0]
        if len(self.queue) < self.size:
            self.queue.append(endTime)
        else: return (-1, None)
        return (startTime, request[1])



def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    for request in requests:
        Buffer.process(buffer, request)

    for each in buffer.finish_time:
        print(each)


if __name__ == "__main__":
    main()
