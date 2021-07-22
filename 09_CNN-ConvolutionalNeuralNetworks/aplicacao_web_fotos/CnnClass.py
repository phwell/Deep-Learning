import tensorflow as tf
import pandas as pd
from keras.models import model_from_json
import numpy as np

class Cnn:
  # construtor da classe
  def __init__(self, arquivo_json, arquivo_pesos, arquivo_mean, arquivo_var):
    self.arquivo_json = arquivo_json
    self.arquivo_pesos = arquivo_pesos
    
    pd_media = pd.read_csv(arquivo_mean)
    self.media = np.array(pd_media).reshape(1,-1)

    pd_variancia = pd.read_csv(arquivo_var)
    self.variancia = np.array(pd_variancia).reshape(1,-1)

    self.modelo = tf.keras.models.Sequential()

  def carregar_modelo(self):
    # consertar sementes aleatórias para reprodutibilidade
    np.random.seed(7)

    # carregar json e criar modelo
    arquivo_json_conf = open(self.arquivo_json, 'r')
    modelo_json_carregado = arquivo_json_conf.read()
    arquivo_json_conf.close()
    self.modelo = model_from_json(modelo_json_carregado)

    # carregar pesos no novo modelo
    self.modelo.load_weights(self.arquivo_pesos)

  def nomalizar_dados(self, array):
    std = self.variancia ** 0.5
    return (array-self.media)/std

  def normalizar(self, X_entrada):
    dados_normalizados = self.nomalizar_dados(X_entrada)
    return dados_normalizados

  def tratamento_resultado(self, x):
    if (x >= 0.5):
      return 1
    else: 
      return 0

  def predicao(self, X_entrada):
    X_entrada = self.normalizar(X_entrada.reshape(1,-1))
    y_pred = self.modelo.predict(X_entrada)
    #resposta_predicao = self.tratamento_resultado(y_pred)
    resposta_predicao = y_pred
    return resposta_predicao
