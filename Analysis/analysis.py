class AnalysisTypesClass:

    def monthly_analysis(df, st, pd, go, selected_param):
        df['monthsofyear'] = pd.Categorical(df.Date.dt.month, categories=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], ordered=True)
        monthly_data_mean = df[[selected_param, 'monthsofyear']].groupby('monthsofyear').mean()
        fig = go.Figure()
        fig.add_trace(go.Line(x=monthly_data_mean.index, y=df[selected_param]))
        fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=False, width=750, height=600)
        st.plotly_chart(fig)

    def annual_analysis(df, st, go, selected_param):
        df['year'] = df.Date.dt.year
        yearly_data_mean = df[[selected_param, 'year']].groupby('year').mean()
        fig = go.Figure()
        fig.add_trace(go.Line(x=yearly_data_mean.index, y=df[selected_param]))
        fig.layout.update(title_text=selected_param, xaxis_rangeslider_visible=False, width=750, height=600)
        st.plotly_chart(fig)