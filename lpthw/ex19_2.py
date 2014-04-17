def thank_you_letter(first_name, spouse_fname, last_name, children, gift):
    print """Dear %s and %s %s,\n
I would like to personally thank you and your %s children for attending my party. It
was a great pleasure talking to you and I hope to see you again soon.
I would also like to thank you for the %s, I will cherish it.\n
Sincerely,
Michael Whitten""" % (first_name, spouse_fname, last_name, children, gift)

thank_you_letter('John', 'Lisa', 'Smith', 2, 'CD')


fname = raw_input("Please enter your first name:")
s_fname = raw_input("Please enter your spouse's first name:")
lname = raw_input("Please enter your last name:")
num_child = raw_input("Please enter the number of children:")
gift = raw_input("Enter gift:")

thank_you_letter(fname, s_fname, lname, num_child, gift)