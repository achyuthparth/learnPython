# python3
from binaryHeap import MinHeap
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    processedTime = 0
    currentTime = 0
    threads = {}
    for i in range(n_workers):
        threads[i] = None
    while jobs[0] != []:
        for j in range(len(threads)):
            if threads[j] is None:
                threads[j] = jobs[0]
                del jobs[0]
                result.append([j, currentTime])
        currentTime += 1
        for j in range(len(threads)):
            if threads[j] is not None and (processedTime + threads[j] <= currentTime):
                processedTime += threads[j]
                threads[j] = None
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
