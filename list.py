def my_project():
    locations = [0, 0, 0]  
    weights = [0, 0, 0]    
    total_weight = 0          

    while total_weight != 713:
        print("\n Where the boxes could be buried?")

        for i in range(3):
            kilometer_mark = int(input(f"Box {i + 1}: "))
         
            locations[i] = (locations[i] + kilometer_mark) % 10
            if locations[i]>7:
                print('LOCATION is SO FAR, there may not be a box')
         
            weights[i] = int(input(f"Weight at {locations[i]} km: "))
            if weights[i]==0:
                print('TRY AGAIN!')
        total_weight = sum(weights)
        if total_weight == 713:
            print("\n You found all the boxes.")
            print("Cargo locations:", locations)
            print("Cargo weights:", weights)
        else:
            print("\n The total weight is incorrect. TRY AGAIN!.")
my_project()