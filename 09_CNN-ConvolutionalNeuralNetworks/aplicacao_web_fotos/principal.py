from bokeh.layouts import row, column, widgetbox
from bokeh.models import TextInput, Button,  Div
from bokeh.plotting import curdoc
from CnnClass import Cnn
import numpy as np
from bokeh.io import show
from bokeh.models import FileInput
from pybase64 import b64decode
import matplotlib.pyplot as plt
import tensorflow as tf
import base64
from PIL import Image
from base64 import decodebytes
import pandas as pd
import io

str_resultado = " " 

def upload_fit_data(attr, old, new):
    print("fit data upload succeeded")
    decoded = b64decode(new)
    f = io.BytesIO(decoded)
    img = Image.open(f)
    img.save("/opt/data/out.jpg", "JPEG")
    print("fit data upload succeeded")
    img.close()

    

def predicao():
  cnn = Cnn("modelo.json","modelo.h5", "mean.csv", "var.csv")
  cnn.carregar_modelo()

  valores_passados_pelo_cliente=np.array([float(texto.value)])

  resultado = "resultado: {}".format(str_resultado)
  div_widget.text = resultado


imagem = FileInput(accept=".png,.jpg")
imagem.on_change('value', upload_fit_data)

texto = TextInput(title="Informe texto", value="")

div_widget = Div(text="", width=400, height=100)
botao = Button(label="Predicao", button_type="success")
botao.on_click(predicao)  
controls = widgetbox([imagem, texto, botao], width=200)
layout = row(column(controls), column(div_widget))
curdoc().add_root(layout)
curdoc().title = "Rede Neural Artificial aplicada a previsão de diabetes"
