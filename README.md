# MangoCare: Mango Pest & Disease Management System

## Overview

MangoCare is a Django-based web application designed to assist mango farmers, agricultural students, and researchers in identifying and managing mango pests and diseases. The system combines two integrated databases to provide comprehensive information about common mango tree problems and their solutions.

## Features

### Core Functionalities
- **Comprehensive Database**: Information about 14 major mango pests and diseases
- **Dual Database System**: 
  - Modern pest & disease catalog with search functionality
  - Legacy database with detailed pest information
- **ID Mapping System**: Custom gateway for seamless navigation between databases

### Pest & Disease Information
Each entry includes:
- Scientific and common names
- Severity classification
- Life cycle details
- Symptoms and damage patterns
- Monitoring guidelines
- Control measures
- High-quality images
- Reference materials

### User Interface
- Clean, modern design
- Responsive layout for all devices
- Easy navigation between sections
- Advanced search with multiple filters

## Technical Stack

### Backend
- Django 5.2
- Python 3.x
- SQLite3 Database

### Frontend
- HTML5
- CSS3
- JavaScript
- Font Awesome 5.15.4
- Google Fonts (Inter)

## Project Structure

```
MangoChung/
├── MangoCare/              # Core project settings
├── home/                   # Homepage application
│   ├── templates/         # Homepage templates
│   └── static/           # Homepage assets
├── pest_disease/          # Modern pest database
│   ├── models/           # Database models
│   ├── templates/        # View templates
│   └── data/            # Pest & disease data
├── pest_disease_detail/   # Detail view handler
├── about_us/             # About page module
├── app_project1/         # Legacy pest database
│   ├── templates/        # Legacy templates
│   ├── static/          # Legacy assets
│   └── data.py         # Legacy data storage
└── static/              # Global static files
```

## Installation Guide

1. Set up Python environment:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize database:
```bash
python manage.py migrate
```

4. Start development server:
```bash
python manage.py runserver
```

5. Access the application:
```
http://127.0.0.1:8000/
```

## Key Components

### 1. Modern Pest & Disease Catalog (`pest_disease`)
- Advanced search functionality
- Filter by type and severity
- Sort by various attributes
- Clean, modern interface

### 2. Legacy Database (`app_project1`)
- Detailed pest information
- Image galleries
- Treatment recommendations
- Reference documentation

### 3. Gateway System
Maps between different ID formats:
- Modern catalog: Numerical IDs (1-14)
- Legacy system: Alphanumeric IDs (P01-P07, D01-D07)

## Database Structure

### Pest & Disease Categories
1. **Pests**:
   - Mango Seed Weevil (P01)
   - Fruitspotting Bug (P02)
   - Fruit Flies (P03)
   - Mango Leafhopper (P04)
   - Mango Fruit Borer (P05)
   - Redbanded Thrips (P06)
   - Tea Mosquito Bug (P07)

2. **Diseases**:
   - Mango Malformation Disease (D01)
   - Algal Leaf Spot (D02)
   - Stem End Rot (D03)
   - Bacterial Black Spot (D04)
   - Pink Disease (D05)
   - Anthracnose (D06)
   - Powdery Mildew (D07)

## Authors

- **Xuan Hung Doan** - s374988
- **Umme Salma Rumana** - s367994
- **Trinh Nguyen** - s375352
- **Melanie Bardoux** - s329560

## License

This project is licensed under the MIT License.

---
© 2024 MangoCare. All Rights Reserved.