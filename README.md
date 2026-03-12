# AquaSense AI 🌊🤖

**AI-Powered Water Intelligence Platform**

AquaSense AI is an intelligent web platform designed to assist communities, researchers, and policymakers in understanding and managing water resources more effectively. The system combines **Generative AI, machine learning models, environmental data analysis, and interactive visualization** to provide insights about water conservation, pollution detection, and sustainable water usage.

This project integrates **IBM watsonx.ai**, **machine learning models**, and **interactive geospatial visualization** to create a unified AI assistant focused on water sustainability.

---

# 🚀 Project Overview

Water scarcity and pollution are critical global challenges. AquaSense AI aims to address these issues by providing an AI-driven platform capable of:

* Answering water-related questions using generative AI
* Predicting rainwater harvesting potential
* Estimating household water usage
* Detecting water pollution from uploaded images
* Visualizing pollution data through interactive heatmaps

The platform acts as a **domain-specific AI assistant for water management and sustainability**.

---

# 🧠 Core Technologies

The project combines several modern technologies across AI, web development, and data science.

### AI & Machine Learning

* IBM watsonx.ai (Granite Foundation Models)
* Retrieval Augmented Generation (RAG)
* Sentence Transformers
* FAISS Vector Database
* TensorFlow / CNN Model (pollution detection)
* Scikit-learn (water crisis prediction)

### Backend

* Python
* Flask Framework
* REST API architecture

### Frontend

* HTML5
* CSS3
* JavaScript
* Web Speech API (voice input)

### Visualization

* Leaflet.js
* Leaflet Heatmap plugin

### Deployment

* IBM Cloud Code Engine
* Docker (optional)
* GitHub

---

# ⚙️ System Architecture

The AquaSense AI system consists of multiple interconnected modules.

```
User Interface
      │
      ▼
Flask Backend API
      │
      ├── Watsonx AI (Generative AI)
      ├── RAG Knowledge Engine
      ├── Rainwater Harvesting Predictor
      ├── Water Usage Calculator
      ├── Image Pollution Detection Model
      └── Water Pollution Heatmap Visualization
```

---

# 🌟 Features

## 1️⃣ AI Water Assistant

Users can ask questions related to water safety, conservation, and environmental sustainability. The system uses **IBM watsonx.ai foundation models** combined with **RAG knowledge retrieval** to generate informed responses.

Example questions:

* How can cities reduce water pollution?
* What are the benefits of rainwater harvesting?
* How can households conserve water?

---

## 2️⃣ Rainwater Harvesting Prediction

The platform estimates how much rainwater can be collected from a rooftop based on:

* City rainfall data
* Roof surface area

This helps households understand potential water savings.

---

## 3️⃣ Water Usage Calculator

Users can estimate their household water consumption based on:

* Number of people
* Daily showers
* Laundry usage

The calculator provides both **daily and monthly usage estimates**.

---

## 4️⃣ AI-Based Water Pollution Detection

Users can upload images of water bodies. A trained **CNN model** analyzes the image and predicts whether the water appears clean or polluted.

---

## 5️⃣ Interactive Pollution Heatmap

A geospatial heatmap displays pollution intensity across different regions using **Leaflet.js**.

This visualization helps identify pollution hotspots.

---

## 6️⃣ Voice Input Assistant

Using the browser's Web Speech API, users can interact with the AI assistant through voice commands.

---

# 📂 Project Structure

```
aquasense-ai
│
├── app.py
├── requirements.txt
├── README.md
│
├── ai_modules
│   ├── watsonx_ai.py
│   ├── rag_engine.py
│   ├── rainwater_predictor.py
│   ├── crisis_model.py
│   └── image_detection.py
│
├── data
│   └── water_docs.txt
│
├── models
│   └── water_model.h5
│
├── templates
│   ├── index.html
│   └── map.html
│
├── static
│   ├── style.css
│   └── script.js
│
└── uploads
```

---

# 🧪 Installation & Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/mrdhirajpathak/aquasense-ai.git
cd aquasense-ai
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Linux/Mac

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Set environment variables

```
IBM_API_KEY=your_ibm_api_key
IBM_PROJECT_ID=your_project_id
```

---

### 5. Run the application

```
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

# ☁️ Deployment (IBM Cloud)

The project can be deployed using **IBM Cloud Code Engine**.

Steps:

1. Push the project to GitHub
2. Create an IBM Cloud Code Engine project
3. Deploy from GitHub repository
4. Configure environment variables
5. Build and deploy the application

Once deployed, the platform becomes publicly accessible through a web URL.

---

# 📊 Example Use Cases

AquaSense AI can support:

* Smart city water management
* Environmental monitoring
* Educational tools for sustainability
* Household water usage awareness
* Pollution detection studies

---

# 🔒 Security Considerations

* Uploaded images are stored temporarily
* API keys should be stored as environment variables
* User inputs should be validated before processing

---

# 📈 Future Improvements

Possible future enhancements include:

* Real-time rainfall API integration
* Satellite water quality monitoring
* Advanced pollution detection models
* Mobile Progressive Web App (PWA)
* IoT sensor integration

---

# 👨‍💻 Author

**Dhiraj Pathak**
Computer Science Engineering Student
AI & Web Development Enthusiast

---

# 📜 License

This project is open-source and available under the **MIT License**.

---

# 🌍 Vision

AquaSense AI demonstrates how artificial intelligence can be used to build tools that promote **environmental awareness, sustainability, and responsible water management**.

By combining AI, environmental data, and interactive visualization, the platform aims to make water intelligence accessible to everyone.
