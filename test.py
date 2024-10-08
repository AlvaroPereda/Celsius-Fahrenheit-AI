import tensorflow as tf
import numpy as np
import os

celsius = np.array([-40,-10,0,8,15,22,38,60,70],dtype=float)
fahrenheit = np.array([-40,14,32,46,59,72,100,140,158],dtype=float)

capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)

os.system("cls") #Se limpia la pantalla

print("Comenzando el entrenamiento")
historial = modelo.fit(celsius,fahrenheit,epochs = 1000, verbose = False)
print("Modelo entrenado")

while(True):
    valor = float(input("Valor en celsius: "))
    resultado = modelo.predict(np.array([valor]))
    print("El resultado es " + str(resultado) + " fahrenheit")
