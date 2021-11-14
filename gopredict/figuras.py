import plotly.figure_factory as ff
import plotly.express as px

#Crea la matriz de confusión de los datos

def matriz_confusion(data):
    z = data.tolist()[::-1]
    x = ['Negative','Positive']
    y = ['Positive','Negative']
    z_text = z

    fig = ff.create_annotated_heatmap(z, x, y, annotation_text=z_text, text=z,hoverinfo='text',colorscale='Blackbody')
    fig.update_layout(font_family="IBM Plex Sans")

    return fig

#Crea una curva ROC con los 

def curva_roc(data):
    fig = px.line(data, x="False Positive", y="True Positive")#, title='ROC Curve')
    fig.update_layout(font_family="IBM Plex Sans")
    
    return fig