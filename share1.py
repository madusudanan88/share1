share_name = input("Enter the Share Name:")
share_price = input("Enter the Share Price:")
share_qty = input("Enter the Share Quantity:")
#share_date = datetime(input("Enter the Purchase date in :"))

file1 = open("share_list.txt", "w")
comb1 = share_name+" "+share_price+" "+share_qty+""
file1.writelines(comb1)
file1.close()
