# خودت و پانی رو جوری با دیکشنری مدل کن که ویژگی‌های مشترکتون تو اون دیکشنری باشه.



pani = {'Name': '', 'Kind': '','Age': '', 'Weight': ''}
print('Enter first group of informatins:')
for key in pani:
    pani[key] = input(str(key)+':')

sogand = {'Name': '', 'Kind': '','Age': '', 'Weight': ''}
print('Enter second group of informatins:')
for key in sogand:
    sogand[key] = input(str(key)+':')
    
print('informations for', pani['Name'],'is:',pani)
print('informations for', sogand['Name'],'is:',sogand)