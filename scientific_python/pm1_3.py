"""Convert second to years"""

#pm1_3.py

seconds = 1*10**9
seconds_per_year = 60.0*60*24*7*52

years = seconds/seconds_per_year

print "If the baby can live %.1f years it can live %.1E seconds" % (years, seconds)