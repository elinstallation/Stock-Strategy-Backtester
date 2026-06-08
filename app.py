import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("backtest_results.csv")

all_tickers = df["Name"].unique().tolist()

if "AAPL" in all_tickers:
    all_tickers.remove("AAPL")
    tickers = ["AAPL"] + all_tickers
else:
    tickers = all_tickers

fig = go.Figure()

for ticker in tickers:
    stock_data = df[df["Name"] == ticker]
    
    fig.add_trace(go.Scatter(x=stock_data['date'], y=stock_data['Buy and Hold'], name='Buy and Hold', visible=False))
    fig.add_trace(go.Scatter(x=stock_data['date'], y=stock_data['SMA returns'], name='SMA returns', visible=False))
    fig.add_trace(go.Scatter(x=stock_data['date'], y=stock_data['Bollinger Bands returns'], name='Bollinger Bands returns', visible=False))



fig.data[0].visible = True
fig.data[1].visible = True
fig.data[2].visible = True

buttons = []
for i, ticker in enumerate(tickers):
    visibility_mask = [False] * (len(tickers) * 3)
    visibility_mask[i*3] = True      # Buy and Hold
    visibility_mask[i*3 + 1] = True  # SMA
    visibility_mask[i*3 + 2] = True  # Bollinger Bands
    
    buttons.append(
        dict(
            method="update",
            label=str(ticker),
            args=[{"visible": visibility_mask}, 
                  {"title": {"text":"Strategy Performance vs Buy and Hold:"}}]
        )
    )

fig.update_layout(
    updatemenus=[
        dict(
            buttons=buttons,
            direction="down",
            showactive=True,
            x=0.52,
            y=1.14,
            xanchor="left",
            yanchor="top",
            font=dict(color="#000000")
        )
    ],
    legend=dict(
        x=1.0,
        y=1.0,
        xanchor="right",
        yanchor="top",
    ),
    template='plotly_dark',
    hovermode='x unified',
    yaxis_tickformat='$.2f',
    title=f"Strategy Performance vs Buy and Hold:"
)

fig.show()
