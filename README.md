# 🎯 Twitter Sentiment Analysis ML Pipeline with DVC

![Python](https://img.shields.io/badge/Python-3.11-blue)
![DVC](https://img.shields.io/badge/DVC-Enabled-orange)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📋 Overview
A robust machine learning pipeline for Twitter sentiment analysis, leveraging DVC (Data Version Control) for reproducible ML workflows. This project implements end-to-end MLOps practices with automated pipeline stages and containerized deployment.

## 🏗️ Project Structure
```
📦 MLOPS-Twitter_Sentiment_Analysis_DVC
├── 🐳 Dockerfile              # Docker configuration
├── 📂 src/                    # Source code
│   ├── 📥 data_ingestion.py     # Data collection
│   ├── 🧹 data_preprocessing.py  # Data cleaning
│   ├── ⚙️ feature_engineering.py # Feature creation
│   ├── 🤖 model_building.py      # Model training
│   ├── 📊 model_evaluation.py    # Model evaluation
│   └── 📂 data/                  # Dataset directory
│       └── 📁 raw/               # Raw data files
├── 📄 dvc.yaml                # DVC pipeline definition
├── 📝 requirements.txt        # Dependencies
└── 📖 README.md               # Documentation
```

## ⚡ Quick Start

### 🛠️ Environment Setup
```bash
# Create conda environment
conda create -n test python=3.11 -y

# Activate environment
conda activate test

# Install dependencies
pip install -r requirements.txt
```

### 🔄 Version Control Setup
```bash
# Initialize Git
git init

# Initialize DVC
dvc init
```

## 🚀 Pipeline Execution

### DVC Commands
```bash
# Run complete pipeline
dvc repro

# View pipeline DAG
dvc dag

# Check metrics
dvc metrics show
```

### 🐳 Docker Deployment
```bash
# Build image
docker build -t sentiment-analysis .

# Run container
docker run -p 8000:8000 sentiment-analysis
```

## 📊 Pipeline Stages

### 1️⃣ Data Ingestion
- 📥 Collects Twitter data
- 🔍 Validates data quality
- 📁 Source: `src/data_ingestion.py`

### 2️⃣ Data Preprocessing
- 🧹 Text cleaning
- 🔍 Data validation
- 📁 Source: `src/data_preprocessing.py`

### 3️⃣ Feature Engineering
- ⚙️ Text vectorization
- 🔍 Feature selection
- 📁 Source: `src/feature_engineering.py`

### 4️⃣ Model Building
- 🤖 Model training
- 🔄 Cross-validation
- 📁 Source: `src/model_building.py`

### 5️⃣ Model Evaluation
- 📊 Performance metrics
- 📈 Results visualization
- 📁 Source: `src/model_evaluation.py`

## ⚙️ Technical Details

### Port Configuration
- 🌐 Application runs on port: 8000
- 🔌 Streamlit interface: 8501

### DVC Integration
- 📊 Metrics tracking
- 🔄 Pipeline automation
- 💾 Model versioning
- 📦 Data versioning

## 📋 Prerequisites
- Python 3.11
- Docker
- Git
- DVC
- NLTK
- Scikit-learn


```

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Important Notes
- ✔️ Ensure data files are in `data/raw/`
- 📝 Keep `requirements.txt` updated
- ⚙️ Check `dvc.yaml` configuration
- 🔄 Run `dvc repro` after changes

