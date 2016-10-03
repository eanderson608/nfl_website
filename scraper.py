from bs4 import BeautifulSoup
import urllib2

# extract home team lines from a beautifulsoup object where text is name
# of desired betting site on foxsports.com/nfl/odds
def get_home_run_lines(text):

	lines = bsObj.findAll("td", {"class":"wisbb_bookCol"},text=text)

	temp = []
	for line in lines:
		line = line.find_next_sibling("td", {"class":"wisbb_runLinePtsCol"})
		line = str(line)

		# split html at break and remove last five chars (</td>) to get home line
		line = line.split("<br/>")[1][:-5]
		temp.append(line)

	return temp

def get_val_lines(text):

	vals = bsObj.findAll("td", {"class":"wisbb_bookCol"},text=text)

	temp = []
	for val in vals:
		val = val.find_next_sibling("td", {"class":"wisbb_runLineValsCol"})
		val = val.get_text()
		temp.append(val[:4])
		temp.append(val[4:])

	return temp

html = urllib2.urlopen("http://www.foxsports.com/nfl/odds")
bsObj = BeautifulSoup(html, 'html.parser')

# get teams, records, dates, and extract text
teams = bsObj.findAll("span", {"class":"wisbb_teamName"})
records = bsObj.findAll("span", {"class":"wisbb_teamRecord"})
teams = [team.get_text() for team in teams]
records = [record.get_text() for record in records]
dates = bsObj.findAll("span", {"class":"wisbb_oddsGameDate"})
dates = [date.get_text() for date in dates]

# get home team lines
fivedimes_lines = get_home_run_lines("5Dimes.eu")
bovada_lines = get_home_run_lines("BOVADA.lv")
mybookie_lines = get_home_run_lines("MYBOOKIE.AG")

# get vals
fivedimes_vals = get_val_lines("5Dimes.eu")
bovada_vals = get_val_lines("BOVADA.lv")
mybookie_vals = get_val_lines("MYBOOKIE.AG")


games_list = []
games_bsObj = bsObj.findAll("div", {"class":"wisbb_gameWrapper"})

for game in games_bsObj:

	d = {} # dictionary to hold game info
	teams = game.findAll("span", {"class":"wisbb_teamName"})
	records = game.findAll("span", {"class":"wisbb_teamRecord"})

	temp = game.find("td", {"class":"wisbb_bookCol"}, text="5Dimes.eu")
	d['fivedimes_line'] = str(temp.find_next_sibling("td", {"class":"wisbb_runLinePtsCol"})).split("<br/>")[1][:-5]

	temp = game.find("td", {"class":"wisbb_bookCol"}, text="BOVADA.lv")
	d['bovada_line'] = str(temp.find_next_sibling("td", {"class":"wisbb_runLinePtsCol"})).split("<br/>")[1][:-5]

	temp = game.find("td", {"class":"wisbb_bookCol"}, text="MYBOOKIE.AG")
	d['mybookie_line'] = str(temp.find_next_sibling("td", {"class":"wisbb_runLinePtsCol"})).split("<br/>")[1][:-5]

	d['date'] = game.find("span", {"class":"wisbb_oddsGameDate"}).get_text()
	d['home_team_name'] = teams[0].get_text()
	d['away_team_name'] = teams[1].get_text()
	d['home_team_record'] = records[0].get_text()
	d['away_team_record'] = records[1].get_text()
	print d

