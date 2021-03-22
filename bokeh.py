from bokeh.plotting import figure, show, output_notebook

output_notebook()
p=figure(plot_width=500,plot_height=500)
x=[a,b,c]
y=[10,50,20]
p.line(x,y,line_width=2,color="green")

show(p) 