Print ("Welcome to Weather Map Station!")
def ask_for_weather():
	zip_code_city=input("What is your current city/zipcode? \nTo quit, press 'q'. ")
ask_for_weather()
def var_unirest():
	require("unirest");
def var_req():
		unirest("GET", "https://community-open-weather-map.p.rapidapi.com/find")
		


		

if ask_for_weather=='q':
	break;
else:
	var_req()

req.query({
	"q": "london",
	"cnt": "0",
	"mode": "null",
	"lon": "0",
	"type": "link, accurate",
	"lat": "0",
	"units": "imperial, metric"
});

req.headers({
	"x-rapidapi-key": "a3f00c2c5emshefb2b4ca12423c8p185f1ejsn52845d24875c",
	"x-rapidapi-host": "community-open-weather-map.p.rapidapi.com",
	"useQueryString": true
});


req.end(function (res) {
#https://github.com/YaffaB/Yaffa-Goldberger-Week-8/blob/main/Yaffa%20Goldberger%20CIS%20245-O851%20A8.1.py	if (res.error) throw new Error(res.error);

#console.log(res.body); });
#elif:
#	print("We are sorry, that was an invalid response.")
#ask_for_weather()
#ask_for_weather() ALL THIS LAST STUFF I PUT WITH # BEC I WASNT SURE HOW TO DO IT