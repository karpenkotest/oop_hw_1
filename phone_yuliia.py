class Phone():
  _calls_counter = 0
  def __init__(self):
   phone_number=None

  
  def set_number(self,phone_number):
    self.number = phone_number
    return f'Your phone number is: {self.number}'

  
  def get_accepted_calls(self):
   return self._calls_counter


  def accept_calls(self):
    self._calls_counter += 1


my_phone1 = Phone()
print(f' Please input phone number')
my_phone1.phone_number = input()
print(my_phone1.set_number(my_phone1.phone_number))


my_phone2 = Phone()
print(f' Please input phone number')
my_phone2.phone_number = input()
print(my_phone2.set_number(my_phone2.phone_number))


my_phone3 = Phone()
print(f' Please input phone number')
my_phone3.phone_number = input()
print(my_phone3.set_number(my_phone3.phone_number))


my_phone1.accept_calls()
my_phone1.accept_calls()
my_phone2.accept_calls()
my_phone3.accept_calls()
my_phone3.accept_calls()
my_phone3.accept_calls()
my_phone3.accept_calls()

my_phones = [my_phone1,my_phone2,my_phone3]

def total_accepted_calls(my_phones):
  total_calls = 0
  for my_phone in my_phones:
      total_calls += my_phone.get_accepted_calls()
  return total_calls

print(f'Total accepted calls: {total_accepted_calls(my_phones)}')

f = open('Сalls.csv', 'w')
s = (f'Total accepted calls: {total_accepted_calls(my_phones)}')
f.write(s)
f.close()


