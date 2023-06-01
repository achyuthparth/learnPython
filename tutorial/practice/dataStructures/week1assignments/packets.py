# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = [None] * self.size

    def process(self, request):
        # write your code here
        if request[0] is not None:
            self.finish_time.insert(request[0], request[1])
        else: return (False, -1)
        sumTime = sum(time for time in self.finish_time if time is not None) - request[1]
        return (sumTime, request[1])


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(Buffer.process(buffer, request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
