# Time:        55     82     64     90
# Distance:   246   1441   1012   1111
from functools import cache


@cache
def distance(time_remaining: int, seconds_to_hold: int, speed: int) -> int:
    if time_remaining == 0:
        return 0
    elif seconds_to_hold == 0:
        return speed * time_remaining
    else:
        return distance(time_remaining - 1, seconds_to_hold - 1, speed + 1)


print(
    [
        len(
            (
                list(
                    filter(
                        lambda dist: dist > race_distance,
                        map(
                            lambda time_to_hold: distance(race_time, time_to_hold, 0),
                            range(race_time + 1),
                        ),
                    )
                )
            )
        )
        for race_distance, race_time in [(246, 55), (1441, 82), (1012, 64), (1111, 90)]
    ]
)


# lol this hits max recursion depth
# print(
#     [
#         len(
#             (
#                 list(
#                     filter(
#                         lambda dist: dist > race_distance,
#                         map(
#                             lambda time_to_hold: distance(race_time, time_to_hold, 0),
#                             range(race_time + 1),
#                         ),
#                     )
#                 )
#             )
#         )
#         for race_distance, race_time in [(246144110121111, 55826490)]
#     ]
# )

# (seconds spent holding) * (race_time - (seconds spent holding))

race_time = 55826490
race_distance_record = 246144110121111

ways_to_win = 0
for seconds_spent_holding in range(race_time):
    if (
        seconds_spent_holding * (race_time - seconds_spent_holding)
        > race_distance_record
    ):
        ways_to_win += 1

print(ways_to_win)
