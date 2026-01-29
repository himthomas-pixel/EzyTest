from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .tenants import Tenant
from .admin import User
from .equipment import Equipment
from .bookings import Booking
from .delivery import Delivery
from .maintenance import MaintenanceLog
from .invoice import Invoice
