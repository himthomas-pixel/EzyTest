mobility-platform/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── bookings.py
│   │   ├── tenants.py
│   │   ├── equipment.py
│   │   ├── delivery.py
│   │   ├── maintenance.py
│   │   └── invoice.py
│   ├── routes/
│   │   ├── public.py
│   │   ├── admin.py
│   │   ├── payments.py
│   │   ├── ndis.py
│   │   └── driver.py
│   ├── services/
│   │   ├── xero.py
│   │   ├── invoices.py
│   │   ├── sms.py
│   │   ├── email.py
│   │   └── availability.py
│   ├── migrations/
│   ├── requirements.txt
│   └── wsgi.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.jsx
│   │   ├── index.jsx
│   │   ├── api.js
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Booking.jsx
│   │   │   └── Checkout.jsx
│   │   └── components/
│   │       ├── Header.jsx
│   │       ├── Footer.jsx
│   │       └── BookingForm.jsx
│   └── vite.config.js
├── driver-app/
│   ├── App.jsx
│   ├── index.jsx
│   ├── pages/
│   │   ├── Dashboard.jsx
│   │   ├── Deliveries.jsx
│   │   └── Profile.jsx
│   └── api.js
├── scripts/
│   ├── deploy.sh
│   ├── seed_data.py
│   └── backup.sh
├── docker-compose.yml
├── .env.example
└── README.md
