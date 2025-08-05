import nltk
nltk.data.path.append('C:\\Users\\IDEAP3 R5\\AppData\\Roaming\\nltk_data')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

texto = """¿Cómo funciona la IA?
Las Inteligencias artificiales utilizan algoritmos y modelos matemáticos para procesar grandes cantidades de datos y tomar decisiones basadas en patrones y reglas establecidas a través del aprendizaje automático, que es la capacidad de una máquina para aprender de forma autónoma a partir de datos sin ser programada específicamente para hacerlo. De esta manera la IA puede mejorar su precisión y eficiencia con el tiempo.
Espero que esta información sobre la IA sea de gran apoyo para su formación y aprendizaje"""

palabras = word_tokenize(texto, language='spanish')
print(palabras)
stop_words = set(stopwords.words('spanish'))
palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words and palabra.isalpha()]
print(palabras_filtradas)
frecuencia_de_las_palabras = FreqDist(palabras_filtradas)
print(frecuencia_de_las_palabras.most_common(10))
