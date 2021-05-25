from math import floor

def segment_speed_calculator(race_track):
    time_needed = 0
    for segment in race_track:
        if not segment == 0:
            time_needed += segment
        else:
            time_needed *= 0.8
    return time_needed

#RACE TRACK DEFINITION
track_segments_list = [int(i) for i in input().split()]
track_segments_list_reversed = track_segments_list[::-1]
segments_to_travel = floor(len(track_segments_list)/2)

track_segments_left = track_segments_list[:segments_to_travel]
track_segments_right = track_segments_list_reversed[:segments_to_travel]

#RACE

left_racer_time = segment_speed_calculator(track_segments_left)
right_racer_time = segment_speed_calculator(track_segments_right)

if right_racer_time < left_racer_time:
    racer = 'right'
    total_time = right_racer_time
else:
    racer = 'left'
    total_time = left_racer_time

print(f'The winner is {racer} with total time: {total_time:.1f}')


#TEST INPUT 29 13 9 0 13 0 21 0 14 82 12