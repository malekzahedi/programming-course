# توی یه دیکشنری نگه دار که هر کاراکتر توی یه استرینگ چند بار تکرار شده



the_srting = str(input('Enter a string:'))

the_analyze = {}
for i in the_srting:
    the_analyze[i] = the_srting.count(i)
print(the_analyze)