time_p1 = ['59', '68', '82', '74']
distance_p1 = ['543', '1020', '1664', '1022']

time_p2 = [''.join(time_p1)]
distance_p2 = [''.join(distance_p1)]


def naive(times, distances):
    ans = 1
    for time, dist in zip(times, distances):
        time, dist= int(time), int(time)
        count = (sum(((time - sec) * sec > dist) for sec in range(time)))
        ans = ans * count
    return ans

def naive_opt(times, distances):
    ans = 1
    for time, dist in zip(times, distances):
        time, dist= int(time), int(dist)
        half = time // 2
        time_odd = 1 + time % 2
        count = 0
        for i in range(half):
            if i * (time - i) > dist:
                count += 2
        ans *= count + (half * (time - half) > dist) * time_odd
    return ans



print(naive_opt(time_p1, distance_p1))
print(naive_opt(time_p2, distance_p2))
