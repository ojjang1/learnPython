apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 
404]]

for floor in apart:
    for room in floor:
        if room == 203:
            continue
        print("Newspaper derivery: ", room) 
