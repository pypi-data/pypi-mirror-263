

'''
	from datetime import datetime, timedelta
	import rollercoaster.clouds.Yahoo.retrieve as Yahoo_retrieve
	treasure_DF = Yahoo_retrieve.start (
		symbol = "TAN",
		end_orbit = datetime.today (),
		start_orbit = datetime.today () - timedelta (days = 10),
		interval = "1h"
	)
'''

'''
	retrieves a pandas DataFrame
'''

from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd

'''
	This seems to attach something to yfinance globals,
	so that stuff like this can be called:
	
		share_data.ta.rsi (append = True)
'''
import pandas_ta as ta


def start (
	symbol = "TAN",
	end_orbit = datetime.today (),
	start_orbit = None,
	interval = "1h",
	
	return_kind = "DF"
):
	if (start_orbit == None):
		start_orbit = end_orbit - timedelta (days = 10)

	treasure_DF = yf.download (
		symbol, 
		start = start_orbit, 
		end = end_orbit,
		interval = interval
	)
	
	if (return_kind == "DF"):
		return treasure_DF
		
	elif (return_kind == "list"):
		return treasure_DF.to_dict ('records');
	
	raise Exception (f"The return kind { return_kind } was not found.")
	
	'''
		print (treasure_df.ta.indicators())
	'''
	
	'''
		treasure_df.ta.rsi (append = True)
		treasure_df.ta.ema (append = True)
	'''
	
	'''
		parsing into JSON:
			result = treasure_df.to_json (orient = "split")
			parsed = json.loads (result)
			print (json.dumps (parsed, indent=4))
	'''