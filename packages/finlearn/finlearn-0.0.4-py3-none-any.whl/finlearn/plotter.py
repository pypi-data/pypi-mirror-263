import plotly.graph_objects as go 
from plotly.subplots import make_subplots
import yfinance as yf

class plotter:
    def __init__(self):
        pass

    
    def lineplot(self,name,start,end,volume=False, type='daily', tracker='Close'):
        '''In this function, the following inputs would be needed which are 
        symbol(as per yfinance ticker symbol), start(give the start date in the "YYYY-MM-DD" format, the duration in days), 
        end (give the end date in the YYYY-MM-DD) and type which in this version are of 4 types: "daily", "weekly", "monthly", "yearly"'''
        
        #Find the ticker of the company name given by the user
        data = yf.download(name,start=start,end=end)
        #The data is getting downloaded after this line is getting executed

        if type=="weekly":
            data=data.resample('W').mean()
        elif type=="monthly":
            data=data.resample('M').mean()
        elif type=="yearly":
            data=data.resample('Y').mean()


        #Making subplots with an option to add volume graph as well
        fig = make_subplots(rows=2 if volume else 1, vertical_spacing=0.3, shared_xaxes=True)
        
        '''Now, we want to add the interactive line plot along with the option to add the volume plots! Just need to write True in that case.
        So the following pieces of code exactly do that part.'''
       
        if tracker=="Open":
          if data['Close'].iloc[-1] >= data['Close'].iloc[0]:
            line_color = 'green'
            shadow_color = 'lightgreen'
          else:
            line_color = 'red'
            shadow_color = 'magenta'
          fig.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines+markers', name='Open Price Curve', line=dict(color=line_color, width=2)), row=1, col=1)
          #fig.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines+markers', name='Open Price Curve', line=dict(color=shadow_color, width=12, dash='solid')), row=1, col=1)        
          fig.update_yaxes(title_text='Open Price', row=1, col=1)

          if volume:
              fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name="Volume"), row=2, col=1)
              fig.update_yaxes(title_text='Volume', row=2, col=1)

          fig.update_layout(title=f'{name} Open Price and Volume' if volume else f'{name} Open Price', xaxis_title='Date', height=600)
          fig.update_xaxes(rangeslider_visible=True, row=1, col=1)

          fig.show()

        else:
          if data['Close'].iloc[-1] >= data['Close'].iloc[0]:
            line_color = 'green'
            shadow_color = 'lightgreen'
          else:
            line_color = 'red'
            shadow_color = 'magenta'
          #fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines+markers', name='Close Price Curve', line=dict(color=shadow_color, width=12, dash='solid')), row=1, col=1)
          fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines+markers', name='Close Price Curve', line=dict(color=line_color, width=2)), row=1, col=1)
          fig.update_yaxes(title_text='Close Price', row=1, col=1)

          if volume:
              fig.add_trace(go.Bar(x=data.index, y=data['Volume'], name="Volume"), row=2, col=1)
              fig.update_yaxes(title_text='Volume', row=2, col=1)

          fig.update_layout(title=f'{name} Close Price and Volume' if volume else f'{name} Close Price', xaxis_title='Date', height=600)
          fig.update_xaxes(rangeslider_visible=True, row=1, col=1)

          fig.show()
        

        