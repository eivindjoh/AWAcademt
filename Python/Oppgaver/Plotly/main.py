import pandas as pd
import plotly.express as px
import plotly.express.data
import plotly.graph_objects as go


'''data_dict = {
    'time': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'vannstand': [3, 6, 8, 6, 3, 1, 3, 5, -1],
    'vind': [4, 5, 6, 2, 1, 2, 3, 3, 5]
}

fig = px.scatter_3d(data_dict, x='time', y='vannstand', z='vind')
fig.show()'''

'''data_pd = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [[4, 2, 1, 2, 3], [1, 2, 3, 4, 5]]})
fig_pd = px.scatter(data_pd, x='x', y='y')
fig_pd.show()'''

'''fig_list = px.scatter(x=[1, 2, 3, 4, 5], y=[[7, 4, 6, 9, 3], [1, 2, 3, 4, 5]])
fig_list.show()'''

df = plotly.express.data.tips()
print(df)
tips = px.scatter(df,
                  x='total_bill', y='tip', title='Tips male/female',
                  trendline='ols', color='sex', marginal_x='box',
                  marginal_y='violin'
                  )
tips.show()

tips_if_smoker = px.scatter(df,
                            x='total_bill', y='tip', title='Tips if smoker',
                            trendline='ols', color='smoker', marginal_x='box',
                            marginal_y='violin'
                            )
tips_if_smoker.show()

revenue_day = px.histogram(df, x='day', y='total_bill', facet_col='sex', title='Revenue per day',
                           category_orders=dict(day=['Thur', 'Fri', 'Sat', 'Sun']))
revenue_day.show()

guest_day = px.treemap(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill', title='Guests')
guest_day.update_traces(root_color="lightgrey")
guest_day.update_layout(margin = dict(t=50, l=25, r=25, b=25))
guest_day.show()

ratio_m_f = px.pie(df, names='sex', title='Male vs Female ratio')
ratio_m_f.show()

count_sex = px.histogram(df, x='total_bill', color='sex')
count_sex.show()

trace1 = go.Scatter(x=[1, 2, 3, 4, 5], y=[5, 4, 2, 4, 7])
trace2 = go.Histogram(x=[1, 2, 3, 4, 5], y=[5, 20, 20, 2, 1])
data = [trace2, trace1]
layout = go.Layout(
    title=go.layout.Title(text='Scatter/Histogram', font=go.layout.title.Font(color='red', size=50))
)
fig_multiple = go.Figure(data=data, layout=layout)
fig_multiple.write_html('multiple_scatter.html', auto_open=True)




