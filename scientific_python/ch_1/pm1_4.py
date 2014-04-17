"""Convert from meters to British length units"""

#pm1_4.py

length_in_meters = 640

inches_to_meters = 39.37007874 #inches per meter
feet_to_meters = inches_to_meters/12 #feet per meter
yards_to_meters = feet_to_meters/3 #yards per meter
miles_to_meters = yards_to_meters/1760 #miles per meter

print "%.2f inches per %.2f meters" % (length_in_meters*inches_to_meters, length_in_meters)
print "%.2f feet per %.2f meters" % (length_in_meters*feet_to_meters, length_in_meters)
print "%.2f yards per %.2f meters" % (length_in_meters*yards_to_meters, length_in_meters)
print "%.4f miles per %.2f meters" % (length_in_meters*miles_to_meters, length_in_meters)