def get_pay_rate(job_code):
  """Determine the pay rate based on the job code."""
  pay_rates = {
      'L': 25.00,  # $25 per hour for job code L
      'A': 30.00,  # $30 per hour for job code A
      'J': 50.00   # $50 per hour for job code J
  }
  return pay_rates.get(job_code, 0.0)  # Default to $0 if job code is invalid

def compute_gross_pay(pay_rate, hours_worked):
  """Compute the gross pay including overtime pay."""
  regular_hours = min(hours_worked, 40)  # Regular hours up to 40
  overtime_hours = max(hours_worked - 40, 0)  # Overtime hours beyond 40

  regular_pay = regular_hours * pay_rate
  overtime_pay = overtime_hours * pay_rate * 1.5  # Time and a half for overtime

  return regular_pay + overtime_pay

def main():
  total_gross_pay = 0
  print("Enter the employee's last name, job code, and hours worked (press Ctrl+Z to stop):")

  while True:
      try:
          last_name = input("Last Name: ")
          job_code = input("Job Code (L, A, J): ").upper()
          hours_worked = float(input("Hours Worked: "))

          pay_rate = get_pay_rate(job_code)
          if pay_rate == 0.0:
              print("Invalid job code. Please enter L, A, or J.")
              continue

          gross_pay = compute_gross_pay(pay_rate, hours_worked)
          total_gross_pay += gross_pay

          print(f"Last Name: {last_name}, Gross Pay: ${gross_pay:.2f}")

      except EOFError:
          print("\nInput stopped.")
          break
      except ValueError:
          print("Please enter valid numeric values for hours worked.")

  print(f"Total of all gross pay: ${total_gross_pay:.2f}")

if __name__ == "__main__":
  main()