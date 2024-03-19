

'''
	import rollercoaster.clouds.CCXT.OHLCV.candles as CCXT_OHLCV_candles
	chart = CCXT_OHLCV_candles.show (
		DF = DF
	)
	
	chart.show ()
'''

from datetime import datetime

import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots


'''
	https://stackoverflow.com/questions/64689342/plotly-how-to-add-volume-to-a-candlestick-chart
'''
'''
themes = [
	"plotly", "plotly_white", "plotly_dark", 
	"ggplot2", "seaborn", "simple_white", "none"
]:
'''
def show (
	#
	#	df
	#
	intervals = None,
	DF = None
):
	#
	#	Utilize the intervals as the DF if intervals is provided.
	#
	if (type (intervals) == list):
		df = pd.DataFrame.from_dict (intervals)
	else:
		df = DF;

	


	# fig = make_subplots (rows = 2, cols = 1)
	# fig = make_subplots (rows = 2, cols = 1, row_heights = [ 0.7, 0.3 ])
	# fig = make_subplots (rows = 1, cols = 2, column_widths = [ 0.7, 0.3 ])

	fig = make_subplots (
		rows = 2, 
		cols = 1, 
		shared_xaxes = True, 
		vertical_spacing = 0.03, 
		subplot_titles = ('OHLC', 'Volume'), 
		row_width = [ 
			0.2, 
			0.7
		]
	)
	
	

	candle_stick_chart = go.Candlestick (
		x = df ['UTC date string'],
		
		open = df ['open'],
		high = df ['high'],
		low = df ['low'],
		close = df ['close']
	)

	'''
	candle_stick_chart.add_annotation (
		x = "2024-01-03T03:00:00+00:00",
		y = 45279.3,
		
		text = 'text?',
		showarrow = False,
		yshift = 10
	)
	'''

	fig.append_trace ( 
		candle_stick_chart,
		row = 1,
		col = 1
	)

	'''
		https://stackoverflow.com/questions/59442383/moving-average-for-plotly
	'''
	'''
	fig = go.Figure (
		data = [
			go.Candlestick (
				x=df.time,
				open=df.open, 
				high=df.high,
				low=df.low,
				close=df.close
			), 
			go.Scatter (
				x = df.time, 
				y=df.MA5, 
				line=dict(color='orange', width=1)
			),			
			go.Scatter (
				x=df.time, 
				y=df.MA20, 
				line=dict(color='green', width=1)
			)
		]
	)
	'''

	fig.add_trace (
		go.Bar (
			x = df ['UTC date string'], 
			y = df ['volume'], 
			showlegend = False
		), 
		row = 2, 
		col = 1
	)

	# Do not show OHLC's rangeslider plot 
	fig.update_layout (
		template = 'plotly_dark'
	)
	fig.update (
		layout_xaxis_rangeslider_visible = False
	)

	#fig.data[1].increasing.fillcolor = color_hi_fill
	fig.data[0].increasing.line.color = 'rgba (200,0,130,1)'
	
	#fig.data[1].decreasing.fillcolor = 'rgba(0,0,0,0)'
	fig.data[0].decreasing.line.color = 'rgba (200,130,0,1)'

	

	#fig.update_layout (height=600, width=600, title_text="Stacked Subplots")
	
	
	return fig;