import time

# we use .time() method of time class, Python is so original
sec_since_epoch = time.time() # return a float (seconds since 1/1/1970)


date_of_day = time.asctime() # as a string 
month = date_of_day[4:7]
day = date_of_day[8:10]
year = date_of_day[20:24]
# easier would be t = time.localtime() ; print(t.tm_year) etc...


# after testing modifying a string created from the float obviously we should use the format of print.
# thanks geeksforgeeks.org ! print("{:.3e}".format(345000)), far more readable.
# good explaination : https://www.datacamp.com/tutorial/python-f-string?utm_cid=23340058065&utm_aid=192632748929&utm_campaign=230119_1-ps-dscia~dsa-tofu~python_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=9196043-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia~emea-en~dsa~tofu~tutorial~python&gad_source=1&gad_campaignid=23340058065&gclid=CjwKCAjwgO7RBhBKEiwAZNP85tP3U55LtHPvLcGsGI6oUj9wmv1RgMWf_-5kV4pqIIAYvnfYwMm_8BoCZqYQAvD_BwE
print("Seconds since January 1, 1970:", f"{sec_since_epoch:,}", "or", "{:.2e}".format(sec_since_epoch), "in scientific notation")
print(month, day, year)  
# "{:.2e}".format(sec_since_epoch)