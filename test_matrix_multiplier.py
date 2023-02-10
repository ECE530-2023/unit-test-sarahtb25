import matrix_multiplier
import cProfile
import tracemalloc
import linecache
import pstats

known_cases = (([['a', 1], [2, 3]], [[1, 2], [3, 4]], "Non-integer value given!"),
               ([[1, 2]], [[
                1, 2, 3]],
                "Number of columns of first matrix does not match number of rows of second matrix!"),
               ([[]], [[1, 2]], "Empty matrix!"),
               ([[1, 2]], [
                []], "Empty matrix!"),
               ([[]], [[1]], "Empty matrix!"),
               ([[1, 2], [], [2, 3]], [[1, 2], [3, 5]],
                "Length of rows in matrix are not equal!"),
               ([[1, 2], [[1]], [2, 3]], [[1, 2], [3, 5]],
                "Length of rows in matrix are not equal!"),
               ([[], [[1]], [2, 3]], [[1, 2], [3, 5]],
                "Length of rows in matrix are not equal!"),
               ([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]],
                [[21, 24, 27], [47, 54, 61]]),
               ([[1, 0.5]], [[2, 4], [6, 8]], [[5, 8]]))


def test_matrix_multiplier():
    for first_matrix, second_matrix, expected_result in known_cases:
        result = matrix_multiplier.matrix_multiplier(
            first_matrix, second_matrix)
        # print(result)

        assert expected_result == result


def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        print("#%s: %s:%s: %.1f KiB"
              % (index, frame.filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


if __name__ == '__main__':
    # tracemalloc.start()

    # Store 25 frames
    tracemalloc.start(25)
    # cProfile.run('test_matrix_multiplier()')

    profiler = cProfile.Profile()
    profiler.enable()
    test_matrix_multiplier()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    # stats = pstats.Stats(profiler).sort_stats('cumtime')
    stats.print_stats()

    snapshot = tracemalloc.take_snapshot()
    top_stats_lineno = snapshot.statistics('lineno')
    top_stats_traceback = snapshot.statistics('traceback')

    print("[ Top 10 ]")
    for stat in top_stats_lineno[:10]:
        print(stat)

    # pick the biggest memory block
    stat = top_stats_traceback[0]
    print("\n\n%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
    for line in stat.traceback.format():
        print(line)

    print("\n\n")
    display_top(snapshot)
