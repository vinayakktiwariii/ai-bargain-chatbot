\# 🤖 AI Bargain Chatbot



<div align="center">



!\[Django](https://img.shields.io/badge/Django-5.2.7-green?logo=django)

!\[Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)

!\[License](https://img.shields.io/badge/License-MIT-yellow)

!\[Status](https://img.shields.io/badge/Status-Active-success)



\*\*An intelligent price negotiation chatbot powered by game theory algorithms\*\*



Developed by \*\*Vinayak Tiwari\*\* | \*\*ArqonX AI Technologies\*\*



\[Demo](#-demo) • \[Features](#-features) • \[Installation](#-installation) • \[Usage](#-usage)



</div>



---



\## 📖 About



AI Bargain Chatbot simulates realistic price negotiation conversations using advanced algorithms inspired by game theory. Built with Django and vanilla JavaScript, it provides an engaging shopping experience where users can negotiate prices with an intelligent AI assistant.



\### 🎯 Key Highlights



\- \*\*Smart Negotiation Engine\*\* - Progressive concession algorithms that adapt to user offers

\- \*\*Real-time Interaction\*\* - Smooth chat interface with typing indicators and animations

\- \*\*Visual Feedback\*\* - Confetti animations on successful deals

\- \*\*Session Management\*\* - HTTP-based negotiation tracking with history

\- \*\*Responsive Design\*\* - Modern glassmorphism UI that works on all devices



---



\## ✨ Features



\### Core Features

\- 🤝 \*\*Intelligent Negotiation\*\* - AI adapts to user offers with realistic counteroffers

\- 📊 \*\*Negotiation History\*\* - Track the entire bargaining journey

\- 🎨 \*\*Beautiful UI\*\* - Modern gradient design with smooth animations

\- ⚡ \*\*Quick Offers\*\* - One-click discount suggestions (30%, 20%, 10% off)

\- 🎉 \*\*Success Animations\*\* - Celebratory confetti on deal closure

\- 🔄 \*\*Dynamic Pricing\*\* - Threshold-based auto-accept/decline logic



\### Technical Features

\- \*\*Game Theory Algorithm\*\* - Progressive concessions with bounded rationality

\- \*\*Threshold-based Decisions\*\* - Auto-accept/decline logic

\- \*\*Round Limiting\*\* - Prevents infinite negotiations (max 5 rounds)

\- \*\*Session Persistence\*\* - HTTP-based session management

\- \*\*Responsive Design\*\* - Mobile-friendly interface



---



\## 🚀 Installation



\### Prerequisites

\- Python 3.10 or higher

\- pip package manager

\- Virtual environment (recommended)



\### Quick Start



1\. Clone the repository

git clone https://github.com/vinayakktiwariii/ai-bargain-chatbot.git

cd ai-bargain-chatbot



2\. Create virtual environment

python -m venv venv



3\. Activate virtual environment

Windows:

venv\\Scripts\\activate



Mac/Linux:

source venv/bin/activate



4\. Install dependencies

pip install -r requirements.txt



5\. Run migrations

python manage.py migrate



6\. Create superuser (for admin access)

python manage.py createsuperuser



7\. Load sample products

python load\_products.py



8\. Run development server

python manage.py runserver





Visit `http://127.0.0.1:8000/products/` to see the application! 🎉



---



\## 📱 Usage



\### Adding Products



\*\*Option 1: Using Admin Panel\*\*

1\. Access admin panel: `http://127.0.0.1:8000/admin/`

2\. Log in with superuser credentials

3\. Go to \*\*Products\*\* → \*\*Add Product\*\*

4\. Fill in product details



\*\*Option 2: Using Load Script\*\*

python load\_products.py





\### Product Configuration



Configure these parameters for each product:



| Parameter | Description | Example |

|-----------|-------------|---------|

| \*\*List Price\*\* | Starting asking price | ₹10,995 |

| \*\*Min Price\*\* | Lowest acceptable price | ₹8,995 |

| \*\*Auto Accept\*\* | Instant accept threshold | ₹10,495 |

| \*\*Auto Decline\*\* | Instant reject threshold | ₹7,995 |

| \*\*Max Rounds\*\* | Maximum negotiation rounds | 5 |

| \*\*Concession Rate\*\* | How generous AI is (0-1) | 0.5 |



\### Negotiating with the Bot



1\. Browse products at `/products/`

2\. Click on any product

3\. Enter your offer in the chat

4\. Bot will counter, accept, or decline

5\. Use quick buttons for faster negotiation

6\. Complete the deal when both parties agree!



---



\## 🏗️ Project Structure



ai-bargain-chatbot/

├── bargain\_project/ # Main Django project

│ ├── settings.py # Project settings

│ ├── urls.py # URL routing

│ └── wsgi.py # WSGI config

├── products/ # Product catalog app

│ ├── models.py # Product model

│ ├── views.py # Product views

│ ├── urls.py # Product URLs

│ └── admin.py # Admin interface

├── chat/ # Negotiation engine

│ ├── negotiation\_engine.py # AI algorithm

│ ├── views.py # Chat API

│ └── urls.py # Chat URLs

├── templates/ # HTML templates

│ ├── base.html # Base template

│ └── products/

│ ├── product\_list.html

│ ├── product\_detail.html

│ └── about.html

├── load\_products.py # Sample product loader

├── .gitignore # Git ignore rules

├── requirements.txt # Dependencies

├── LICENSE # MIT License

└── README.md # This file





---



\## 🧠 How the Algorithm Works



The negotiation engine uses a \*\*bounded rationality\*\* approach inspired by game theory:



\### 1. Threshold-Based Decisions

if user\_offer >= auto\_accept\_threshold:

\# Accept immediately (great deal!)

elif user\_offer < auto\_decline\_threshold:

\# Decline immediately (too low)

else:

\# Enter negotiation phase



\### 2. Progressive Concessions

Each round, the bot becomes more generous:

round\_factor = 1 + (current\_round \* 0.2) # 20% more generous per round

effective\_concession = concession\_rate \* round\_factor



\### 3. Smart Counteroffers

price\_gap = list\_price - user\_offer

concession\_amount = price\_gap \* effective\_concession

counter\_price = list\_price - concession\_amount

counter\_price = max(min\_price, counter\_price) # Floor at min\_price



\### 4. User Acceptance Detection

if user\_offer >= last\_bot\_offer:

\# User accepted bot's offer!

accept\_deal()



---



\## 🛠️ Technology Stack



\- \*\*Backend\*\*: Django 5.2.7

\- \*\*Frontend\*\*: HTML5, CSS3, JavaScript (Vanilla)

\- \*\*Database\*\*: SQLite (development), PostgreSQL (production-ready)

\- \*\*Algorithm\*\*: Game Theory-based Negotiation Logic



---



\## 🤝 Contributing



Contributions are welcome! Please follow these steps:



1\. Fork the repository

2\. Create a feature branch (`git checkout -b feature/AmazingFeature`)

3\. Commit your changes (`git commit -m 'Add some AmazingFeature'`)

4\. Push to the branch (`git push origin feature/AmazingFeature`)

5\. Open a Pull Request



---



\## 📄 License



This project is licensed under the \*\*MIT License\*\* - see the \[LICENSE](LICENSE) file for details.



Copyright (c) 2025 Vinayak Tiwari - ArqonX AI Technologies



---



\## 👨‍💻 Author



\*\*Vinayak Tiwari\*\*  

AI Engineer | Full-Stack Developer | Founder @ ArqonX AI technologies

ArqonX AI Technologies



\- GitHub: \[@vinayakktiwariii](https://github.com/vinayakktiwariii)

\- LinkedIn: \[Vinayak Tiwari](https://linkedin.com/in/vinayak-tiwari-311546393)

\- Email: arqonxaitechnologies@gmail.com

\- Website: \[ArqonX AI](https://arqonx.ai)



---



\## 🙏 Acknowledgments



\- Django community for the excellent framework

\- Game theory research for negotiation algorithms

\- Open source contributors worldwide



---



\## 📞 Support



For support, email vinayak@arqonx.ai or open an issue on GitHub.



---



<div align="center">



\*\*Made with ❤️ by Vinayak Tiwari | ArqonX AI Technologies\*\*



⭐ Star this repository if you find it helpful!



</div>



