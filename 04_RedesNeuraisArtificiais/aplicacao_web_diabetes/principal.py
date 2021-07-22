from bokeh.layouts import row, column, widgetbox
from bokeh.models import TextInput, Button,  Div
from bokeh.plotting import curdoc
from DiabeteClass import Diabete
import numpy as np

def predicao():
  diabetes = Diabete("modelo.json","modelo.h5", "mean.csv", "var.csv")
  diabetes.carregar_modelo()

  valores_passados_pelo_cliente=np.array([float(gravidez.value),float(glicose.value),float(pressaoArterial.value),float(espessuraPele.value),float(insulina.value),float(imc.value), float(funcaolinguagemDiabetes.value), float(idade.value)])
  
  resultado_predicao_diabetes = diabetes.predicao(valores_passados_pelo_cliente)

  resultado_predicao_diabetes = resultado_predicao_diabetes[0][0] * 100.0
  
  if (resultado_predicao_diabetes>50.0):
    str_resultado = "Diabetes com probabilidade de {:0.3f} %  ".format(resultado_predicao_diabetes)
  else:
    str_resultado = "Sem Diabetes com probabilidade de {:0.3f} %  ".format(resultado_predicao_diabetes)

  resultado = "resultado: {}".format(str_resultado)

  div_widget.text = resultado

gravidez = TextInput(title="Informe Gravidez", value="")
glicose = TextInput(title="Informe Glicose", value="")
pressaoArterial = TextInput(title="Informe Pressão arterial", value="")
espessuraPele = TextInput(title="Informe Espessura da pele", value="")
insulina = TextInput(title="Informe Insulina", value="")
imc = TextInput(title="Informe IMC", value="")
funcaolinguagemDiabetes = TextInput(title="Informe Função de Linhagem de Diabetes", value="")
idade = TextInput(title="Informe Idade", value="")
div_widget = Div(text="", width=400, height=100)
botao = Button(label="Predicao", button_type="success")
botao.on_click(predicao)  
controls = widgetbox([gravidez, glicose, pressaoArterial, espessuraPele, insulina, imc, funcaolinguagemDiabetes, idade, botao], width=200)
layout = row(column(controls), column(div_widget))
curdoc().add_root(layout)
curdoc().title = "Rede Neural Artificial aplicada a previsão de diabetes"
