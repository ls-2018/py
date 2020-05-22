import re
import datetime

if (n := len([1, 2, 3])) < 10:
    print(f"List is too long ({n} elements, expected <= 10)")
discount = 0.0
if (mo := re.search(r'(\d+)% discount', "12321312312% discount")):
    discount = float(mo.group(1)) / 100.0
    print(discount)

user = 'eric_idle'
member_since = datetime.date(1975, 7, 31)
print(f'{user=} {member_since=}')
# delta = datetime.date.today() - member_since
#
# print(f'{user!s}  {delta.days:,d}')
# from math import *
#
# print(f'{30}  {cos(radians(30)):.3f}')
