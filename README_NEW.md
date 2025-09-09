# AgroUSSD - Agricultural Marketplace USSD Simulation

## Overview

AgroUSSD is a text-based command-line application that simulates a USSD phone system for connecting farmers and buyers directly, eliminating middlemen and ensuring fair prices for agricultural products.

## Problem Statement

1. **Farmers** sell their crops for very low prices because they don't know market prices in big cities
2. **Middlemen** buy cheap from farmers and sell high to buyers, keeping most of the profit
3. **Buyers** pay high prices for produce that isn't even fresh

## Solution

AgroUSSD provides:
- **For Farmers**: Real-time market prices and ability to list crops with their own asking prices
- **For Buyers**: Access to farmers selling crops they need
- **Direct Connection**: Farmers and buyers can connect directly, cutting out middlemen

## Features

### For Farmers
- ✅ User registration and authentication
- ✅ Check current market prices
- ✅ List harvests for sale with custom pricing
- ✅ View their active listings
- ✅ Update profile information
- ✅ Track farm details and primary crops

### For Buyers
- ✅ User registration and authentication
- ✅ Check current market prices
- ✅ Browse available crops
- ✅ Search by crop type
- ✅ Search by location
- ✅ Connect with farmers
- ✅ View connection history
- ✅ Update profile information

### System Features
- ✅ USSD-style text interface
- ✅ Data persistence using JSON files
- ✅ Input validation
- ✅ Session management
- ✅ Object-oriented design with inheritance

## Project Structure

```
AgroUSSD/
├── src/                     # Main source code
│   ├── models/              # Data models
│   │   ├── user.py         # Abstract base user class
│   │   ├── farmer.py       # Farmer user class
│   │   ├── buyer.py        # Buyer user class
│   │   ├── harvest.py      # Harvest listing model
│   │   └── __init__.py
│   ├── services/           # Business logic
│   │   ├── user_service.py      # User management
│   │   ├── market_service.py    # Market price data
│   │   ├── harvest_service.py   # Harvest listings
│   │   ├── connection_service.py # Farmer-buyer connections
│   │   └── __init__.py
│   ├── interfaces/         # User interface
│   │   ├── base_interface.py    # Abstract interface class
│   │   ├── main_menu.py         # Main menu
│   │   ├── farmer_menu.py       # Farmer dashboard
│   │   ├── buyer_menu.py        # Buyer dashboard
│   │   ├── session_manager.py   # Session management
│   │   └── __init__.py
│   ├── utils/              # Utility functions
│   │   ├── data_handler.py      # JSON file operations
│   │   ├── validators.py        # Input validation
│   │   ├── helpers.py           # Helper functions
│   │   └── __init__.py
│   └── main.py             # Application entry point
├── data/                   # Data storage
│   ├── users.json          # User accounts
│   ├── harvests.json       # Harvest listings
│   ├── market_prices.json  # Market price data
│   └── connections.json    # Farmer-buyer connections
├── test/                   # Test files
│   └── test_models.py      # Unit tests
├── run.py                  # Application launcher
├── test_app.py             # Test script
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Installation & Setup

1. **Clone or download** the project to your local machine
2. **Install Python 3.7+** if not already installed
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Method 1: Using the launcher script
```bash
python run.py
```

### Method 2: Direct execution
```bash
python src/main.py
```

### Method 3: Test the application
```bash
python test_app.py
```

## Usage

1. **Start the application** using one of the methods above
2. **Choose your role**:
   - Register as a Farmer
   - Register as a Buyer
   - Login if you already have an account
3. **Navigate through menus** using number selections
4. **Follow the prompts** to complete actions

## Sample Data

The application comes with pre-loaded market price data for common crops:
- Rice: ₦450.00/kg
- Maize: ₦320.00/kg
- Wheat: ₦380.00/kg
- Cassava: ₦180.00/kg
- Yam: ₦250.00/kg
- And many more...

## Technical Details

### Architecture
- **Object-Oriented Design**: Uses inheritance with abstract base classes
- **MVC Pattern**: Models, Services, and Interfaces are separated
- **Data Persistence**: JSON files for simple data storage
- **Session Management**: Tracks user state and navigation

### Key Classes
- `User`: Abstract base class for all users
- `Farmer`: Inherits from User, adds farm-specific properties
- `Buyer`: Inherits from User, adds buyer-specific properties
- `Harvest`: Represents crop listings
- `SessionManager`: Manages user sessions and navigation
- `BaseInterface`: Abstract base for all menu interfaces

### Data Flow
1. User interacts with interface
2. Interface calls appropriate service
3. Service validates data and updates models
4. Data is persisted to JSON files
5. Results are displayed to user

## Testing

Run the test suite to verify functionality:
```bash
python test_app.py
```

This will test:
- Module imports
- Service instantiation
- Validator functions
- Market service functionality

## Requirements

- Python 3.7 or higher
- No external dependencies (uses only standard library)

## Future Enhancements

Potential improvements for future versions:
- Real-time price updates
- SMS notifications
- Payment integration
- Mobile app interface
- Database integration
- Advanced search filters
- Price history tracking
- Farmer verification system

## Contributing

This project follows a structured approach with clear separation of concerns. When contributing:
1. Follow the existing code structure
2. Add appropriate validation
3. Update tests as needed
4. Maintain the USSD-style interface

## License

This project is created for educational purposes as part of a programming assignment.

---

**AgroUSSD** - Connecting Farmers and Buyers Directly! 🌾📱
