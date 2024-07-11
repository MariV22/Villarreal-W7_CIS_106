def compute_batting_average(hits, at_bats):
  if at_bats == 0:
      return 0.0
  return hits / at_bats

def main():
  player_count = 0
  print("Enter the player's last name, number of hits, and at-bats (press Ctrl+Z to stop):")

  while True:
      try:
          last_name = input("Last Name: ")
          hits = int(input("Number of Hits: "))
          at_bats = int(input("Number of At-Bats: "))
          batting_average = compute_batting_average(hits, at_bats)

          print(f"Last Name: {last_name}, Batting Average: {batting_average:.3f}")
          player_count += 1

      except EOFError:
          print("\nInput stopped.")
          break
      except ValueError:
          print("Please enter valid numeric values for hits and at-bats.")

  print(f"Total number of players entered: {player_count}")

if __name__ == "__main__":
  main()