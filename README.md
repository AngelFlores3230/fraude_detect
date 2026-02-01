# 🕵️‍♂️ Detección de Fraude Financiero en Redes Sociales con NLP

Este proyecto aborda la **detección de fraude financiero e ingeniería social en mensajes de redes sociales**, utilizando técnicas de **Procesamiento de Lenguaje Natural (NLP)** y **Machine Learning**. El enfoque cubre todo el pipeline: **extracción de datos reales desde Telegram**, **etiquetado débil**, **entrenamiento de modelos clásicos y basados en Transformers**, y **evaluación con métricas avanzadas**.

---

## 📌 Objetivo

Desarrollar y evaluar modelos capaces de **identificar mensajes potencialmente fraudulentos** en texto en español, típicos de redes sociales (promesas de inversión, captación, estafas financieras), priorizando un alto *recall* sin perder precisión.

---

## 🗂️ Estructura del repositorio

```
├── Extractor_Temas.py
├── PrepararDataset.ipynb
├── Detectar_fraude_financiero_TF_IDF+LR.ipynb
├── Detectar_fraude_roberta.ipynb
└── README.md
```

---

## 🔹 1. Extracción de datos desde Telegram

**Archivo:** `Extractor_Temas.py`

Script en Python basado en **Telethon** para extraer mensajes reales desde grupos o canales de Telegram (incluyendo foros con temas).

* Se conecta a la API de Telegram
* Detecta si el chat es grupo, canal o foro
* Extrae mensajes y los guarda en CSV con las columnas:

  * `Fecha`
  * `Sender_ID`
  * `Topic_ID`
  * `Mensaje`

📄 Salida típica:

```
-100XXXXXXXXXX_blindado.csv
```

Este archivo constituye el **dataset crudo** del proyecto.

---

## 🔹 2. Preparación y etiquetado del dataset

**Archivo:** `PrepararDataset.ipynb`

Notebook encargado de:

* Limpieza básica de texto
* **Etiquetado débil (weak supervision)** mediante reglas heurísticas (R1–R9), que capturan:

  * Promesas de ganancia
  * Captación implícita
  * Llamados a contacto privado
  * Lenguaje persuasivo
  * Spam coordinado entre usuarios
* Cálculo de:

  * `fraud_score`
  * `fraud_label`

📄 Salida:

```
dataset_etiquetado_v2.csv
```

Este dataset es la base para el entrenamiento de los modelos.

---

## 🔹 3. Modelo clásico: TF-IDF + Logistic Regression

**Archivo:** `Detectar_fraude_financiero_TF_IDF+LR.ipynb`

Implementa un baseline sólido y explicable:

* Vectorización **TF-IDF (word n-grams)**
* Clasificación con **Logistic Regression**
* Ajuste fino del **umbral de decisión**
* Métricas:

  * Precision
  * Recall
  * F1-score
  * ROC-AUC
  * PR-AUC
* Matriz de confusión
* Pruebas interactivas con nuevos mensajes

Este modelo sirve como **referencia interpretativa** y comparativa.

---

## 🔹 4. Modelo avanzado: RoBERTa (XLM-RoBERTa)

**Archivo:** `Detectar_fraude_roberta.ipynb`

Implementa un modelo basado en Transformers:

* Fine-tuning de **XLM-RoBERTa**
* Tokenización y entrenamiento en GPU (Google Colab)
* Ajuste fino de umbral para maximizar F1
* Evaluación completa con métricas y matriz de confusión
* Modo prueba interactivo con frases nuevas

Este modelo captura **patrones semánticos complejos** que el modelo clásico no detecta.

---

## 📊 Resultados (resumen)

* Modelos con **alto poder discriminativo** (PR-AUC > 0.95 en pruebas)
* Buen equilibrio entre precisión y recall
* Detección efectiva de fraude explícito e implícito
* Pipeline reproducible y extensible

---

## 🚀 Tecnologías utilizadas

* Python
* Telethon
* pandas, scikit-learn
* HuggingFace Transformers
* PyTorch
* Google Colab
* Jupyter Notebook

---

## 📌 Notas finales

Este repositorio está orientado a:

* Investigación académica
* Sistemas antifraude basados en texto
* Análisis de ingeniería social en redes sociales

El enfoque **weak-supervised + NLP** permite trabajar con datos reales sin necesidad de anotación manual masiva.

---


