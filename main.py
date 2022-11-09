from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 500

PROBABILITY_SCORE_CHANGED = 0.1

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
                             PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    # median_offset_increase = (OFFSET_MAX_STEP + 1) / 2
    #
    # search_pointer = math.floor(offset / median_offset_increase)
    # print(search_pointer)
    # if game_stamps[search_pointer]["offset"] == offset:
    #     return (game_stamps[search_pointer]["score"]["home"],
    #             game_stamps[search_pointer]["score"]["away"])
    # else:
    #     return game_stamps[search_pointer]

    arr = list(filter(lambda item: (abs(item['offset']-offset) <= OFFSET_MAX_STEP), game_stamps))
    print(arr)
    offset_index = 0
    offset_delta = offset - arr[0]['offset']
    for index, item in enumerate(arr):
        if abs(item['offset']-offset) < offset_delta:
            offset_delta = abs(item['offset']-offset)
            offset_index = index
    return arr[offset_index]
    # return home, away


print(get_score(game_stamps, 990))
