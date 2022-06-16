class VisualizationTypesClass:

    def histogram_visualization(df, st, px, y_axis):
        df = df.resample('M').mean()
        # df = px.data
        fig = px.histogram(df, x=y_axis)
        fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=False, width=750, height=600)
        st.plotly_chart(fig)

    def line_visualization(df, st, go, y_axis):
        df = df.resample('M').mean()
        fig = go.Figure()
        fig.add_trace(go.Line(x=df.index, y=df[y_axis]))
        fig.layout.update(title_text=y_axis, xaxis_rangeslider_visible=False, width=750, height=600)
        st.plotly_chart(fig)