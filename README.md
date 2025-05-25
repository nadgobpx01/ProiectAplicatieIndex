# Money Manager

A Django-based personal finance tracker for income, expenses, and reports.

## Features

- User registration and authentication
- Transaction and category management
- Monthly financial overview
- PDF report export
- Admin-only blog section

## File Structure

ProiectAplicatieIndex/
├── accounts/
│ ├── views.py
│ ├── forms.py
│ └── urls.py
├── blog/
│ ├── views.py
│ ├── forms.py
│ ├── models.py
│ └── urls.py
├── config/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── core/
│ ├── views.py
│ └── urls.py
├── moneymanager/
│ ├── views.py
│ ├── forms.py
│ ├── models.py
│ └── urls.py
├── static/
├── templates/
│ ├── core/
│ ├── accounts/
│ ├── blog/
│ └── moneymanager/
├── media/
├── manage.py
└── .env

## Setup

1. Clone the repo
2. Create a virtual environment
3. Install dependencies
4. Set up `.env` and run migrations
5. Start the server

## License

MIT
