# The code is built on the logic that in a chord starts after the start of an other chord but before it ends,
#and ends after the first chord ends then these chords definately intersect. Using this login a O(nlogn) appraoch is defined.
#The Complexity is defined by maily by thr sorting logic
def count_intersections(input_list):
    radians= list(input_list[0])
    identifiers=list(input_list[1])
    endpoints = []
    i=0
    #Extracting the start and end points and creating a end point list
    for rad in radians:
        if(identifiers[i][0] == "s"):
            start_id = identifiers[i]
            #creating an endpoint array in the form (radian,"start",id)
            endpoints.append((rad, 'start', start_id))
        else:
            end_id = identifiers[i]
             
            endpoints.append((rad, 'end', end_id))
        i=i+1

    # Sort by radian if radians are equal, sort 'end' before 'start'
    endpoints.sort(key=lambda x: (x[0], x[1] == 'start'))

    active_chords = set()
    intersections = 0

    for rad1, point_type, chord_id in endpoints:
        if point_type == 'start':
    # For each active chord, check if the new chord intersects with it.
            intersections += len(active_chords)
            active_chords.add(chord_id)
        elif point_type == 'end':
            active_chords.remove("s" + chord_id[1:])

    return intersections

input_list=[(0.78, 1.47, 1.77, 3.92),('s1','s2','e1','e2')]
print(count_intersections(input_list))
