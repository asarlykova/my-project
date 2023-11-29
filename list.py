import random

cargo_locations = []  
cargo_weights = []  

for i in range(3):
  location = random.randint(1, 7)
  weight = random.randint(100, 300)

  cargo_locations.append(location)
  cargo_weights.append(weight) 

total_weight_found = 0
correct_guesses = 0
while correct_guesses < 3:
  kilometer_mark = int(input("Enter a kilometer mark (1-7): "))
  for i in range(3):
    if kilometer_mark == cargo_locations[i]:
      total_weight_found += cargo_weights[i] 
      correct_guesses += 1  

      for j in range(3):
        if j != i:
          cargo_locations[j] = random.randint(1, 7)

      print("Cargo found at kilometer mark", kilometer_mark)
      break

if total_weight_found == 713:
  print("All cargo found!")
else:
  print("Not all cargo found. Try again.")