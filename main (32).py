def compute_mpg(miles_travelled, gallons_used):
  if gallons_used == 0:
      return 0.0
  return miles_travelled / gallons_used

def main():
  trip_count = 0
  print("Enter the destination city, miles travelled, and gallons used for a trip (press Ctrl+Z to stop):")

  while True:
      try:
          destination_city = input("Destination City: ")
          miles_travelled = float(input("Miles Travelled: "))
          gallons_used = float(input("Gallons Used: "))
          mpg = compute_mpg(miles_travelled, gallons_used)

          print(f"Destination City: {destination_city}, Miles: {miles_travelled}, MPG: {mpg:.2f}")
          trip_count += 1

      except EOFError:
          print("\nInput stopped.")
          break
      except ValueError:
          print("Please enter valid numeric values for miles travelled and gallons used.")

  print(f"Total number of trips entered: {trip_count}")

if __name__ == "__main__":
  main()