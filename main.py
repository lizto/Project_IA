# Vamos a importar NLTK (Natural Language Toolkit) que nos va a ayudar a trabajar con lenguaje natural
import nltk
nltk.download('punkt_tab')
# Definir la ruta donde se almacenarán los datos descargados de NLTK
nltk.data.path.append(r'C:\Users\IDEAP3 R5\AppData\Roaming\nltk_data')

# Descargamos la lista de palabras vacías stopwords que son palabras comunes como el, la, los, etc.
nltk.download('stopwords')

# Importar la función que divide un texto en palabras
from nltk.tokenize import word_tokenize

# Importar la lista de palabras vacías stopwords en español
from nltk.corpus import stopwords

# Imporar la herramienta para calcular la frecuencia de palabras en un texto
from nltk.probability import FreqDist

# Definimos un texto en español que queramos analizar

texto = """
Soy Liz Torres ingeniera de sistemas, me gusta la tecnologia y aprender nuevas cosas.
Me enfoco en gestión de proyectos, para el programa de IA mi compañero es Andres.
"""

# Tokenización: Convertimos el texto en una lista de palabras individuales
palabras = word_tokenize(texto, language= 'spanish')

# Mostramos la lista de palabras obtenidas
print(palabras)

# Obtenemos la lista de palabras vacías en español, es decir, cargamos las stopwords en español. Aquí obtenemos una lista de palabras comunes en español que normalmente no necesistamos para el análisis. 
stop_words = set(stopwords.words('spanish'))

# Filtramos las palabras: eliminamos las stopwords y los signos de puntuación
# Recorremos cada palabra en una lista llamada palabras. Si la palabra no está en las stopwords y es una palabra real (sin números ni símbolos), la guardamos.

palabras_filtradas = [palabras for palabras in palabras if palabras.lower() not in stop_words and palabras.isalpha()]

# Mostramos la lista de palabras después del filtrado.
# Resultado: Nos quedamos solo con las palabras importantes.
print(palabras_filtradas)

# Calculamos la frecuencia de cada palabra en la lista filtrada
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)

# Mostramos las 10 palabras más comunes y la cantidad de veces que aparecen
print(frecuencia_de_las_palabras.most_common(10))