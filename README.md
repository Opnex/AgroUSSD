            BREAK DOWN OF THE TASK

                    THE PROBLEM
1. Farmers like Adamu sell their crops for very low prices because they don't know what the price is in big cities.
2. Middlemen buy cheap from farmers and sell high to buyers, keeping most of the profit.
3. Buyers like Kemi pay high prices for produce that isn't even fresh.

                    WHAT TO DO
Build a text-based (command-line) program that simulates this USSD phone system. This system will:
1. Help Farmers: Let them check real-time market prices and list their crops for sale with their own price.
2. Help Buyers: Let them find farmers who are selling the crops they need.
3. Cut out the Middleman: Connect farmers and buyers directly so they can deal with each other.

                        WHAT TO BUILD
You are not building a real USSD system for phones. You are building a simulation that runs on a computer.

                        HOW IT WILL WORK
1. A user (farmer or buyer) will run your program.
2. The program will show a menu of options (e.g., "Press 1 for Prices", "Press 2 to List Your Crops").
3. The user will type a number to choose an option.
4. The program will ask for more info or show the results, just like a real USSD system.

                    MOST IMPORTANT THINGS TO FOLLOW
1. Use Object-Oriented Programming (OOP): You must structure your code using classes and inheritance. The instructions give you a specific list of abstract classes (like a blueprint) you must create (e.g., User, Farmer, Product).
2. Store Data in Files: Save user info, crop prices, etc., in simple JSON or CSV files (no complex databases).
3. Follow the Folder Structure: You must organize your code into the specific folders listed (like src/models/, src/services/, data/).

                    SUMMARRY OF PROJECT
WE are creating a text-menu program that acts like a marketplace for farmers and buyers, using specific Python programming rules (OOP and a given folder structure). The goal is to solve the problem of middlemen by providing information and direct connections.

                    PROJECT FILE STRUCTURE
The below structure is the folder and file structure to the task done

Step 1: Create the Main Project Folder
Folder Name: AgroUSSD


Step 2: Create the src Folder (for all your Python code)
Location: AgroUSSD/src/
What it is: This is the main folder for all your Python code.

Files to create inside SRC:
1. main.py (This is the main program that starts everything)


Step 3: Inside src, create the models Folder
Location: AgroUSSD/src/models/
What it is: This folder defines the "things" in your system (Users, Crops, etc.).

Files to create inside models:
1. user.py
2. farmer.py
3. buyer.py
4. product.py
5. crop.py
6. harvest.py
7. __init__.py (This is an empty file that tells Python this is a package)



Step 4: Inside src, create the services Folder
Location: AgroUSSD/src/services/
What it is: This folder contains the "doers" - the logic for actions like register, login, etc.

Files to create inside services:
1. user_service.p
2. market_service.py
3. harvest_service.py
4. connection_service.py
5. __init__.py


Step 5: Inside src, create the interfaces Folder
Location: AgroUSSD/src/interfaces/
What it is: This folder manages the USSD menus you see on the screen.

Files to create inside interfaces:
1. base_interface.py
2. main_menu.py
3. farmer_menu.py
4. buyer_menu.py
5. session_manager.py
6. __init__.py



Step 6: Inside src, create the utils Folder
Location: AgroUSSD/src/utils/
What it is: This folder contains helper tools used by everyone else.

Files to create inside utils
1. data_handler.py
2. validators.py
3. helpers.py
4. __init__.py



Step 7: Create the data Folder (for your JSON files)
Location: AgroUSSD/data/ (This is separate from src)
What it is: This is your simple database. It stores all your information in files.

Files to create inside data:
1. users.json
2. harvests.json
3. market_prices.json
4. connections.json



Step 8: Create the Top-Level Files
Location: AgroUSSD/ (The main folder)

Files to create here:
1. run.py (A simple launcher script)
2. requirements.txt (A list of Python libraries needed)
3. README.md (A document explaining your project)


            Final Folder Structure (Visual Summary)

AgroUSSD/                    # Main Project Folder
│
├── src/                     # Folder for all Python Code
    main.py                   file inside src
│   ├── models/              # Folder for Data Blueprints
│   │   ├── user.py
│   │   ├── farmer.py
│   │   ├── buyer.py
│   │   ├── product.py
│   │   ├── crop.py
│   │   ├── harvest.py
│   │   └── __init__.py
│   │
│   ├── services/            # Folder for Business Logic
│   │   ├── user_service.py
│   │   ├── market_service.py
│   │   ├── harvest_service.py
│   │   ├── connection_service.py
│   │   └── __init__.py
│   │
│   ├── interfaces/          # Folder for USSD Menus
│   │   ├── base_interface.py
│   │   ├── main_menu.py
│   │   ├── farmer_menu.py
│   │   ├── buyer_menu.py
│   │   ├── session_manager.py
│   │   └── __init__.py
│   │
│   ├── utils/               # Folder for Helper Tools
│   │   ├── data_handler.py
│   │   ├── validators.py
│   │   ├── helpers.py
│   │   └── __init__.py
│   │
│   └── main.py              # The Main Application Engine
│
├── data/                    # Folder for Data Storage (JSON Files)
│   ├── users.json
│   ├── harvests.json
│   ├── market_prices.json
│   └── connections.json
│
├── run.py                   # Launcher Script
├── requirements.txt         # Dependencies List
└── README.md               # Project Documentation


                        STEP BY STEP WORK
Phase 1: The Foundation (Data Blueprints) - src/models/
Start here. You must define your data structures before you can build logic around them.

1. src/models/__init__.py
Purpose: An empty file that tells Python this folder is a package. This allows you to import files from this folder using from models import user.

2. src/models/user.py (Abstract Base Class)
Purpose: The blueprint for every user. It defines the core attributes every user must have.
What it will do: It will create a class with properties like name, phone_number, pin, location.
Relationship: It is the parent class that Farmer and Buyer will inherit from.

3. src/models/farmer.py
Purpose: To represent a farmer user.
What it will do: It will inherit from User and add extra properties like farm_size and primary_crops.
Relationship: It is a User. It will be created by user_service.py and used by farmer_menu.py.

4. src/models/buyer.py
Purpose: To represent a buyer user.
What it will do: It will inherit from User and add an extra property like business_name.
Relationship: It is a User. It will be created by user_service.py and used by buyer_menu.py.

5. src/models/harvest.py
Purpose: To represent a farmer's crop listing on the marketplace.
What it will do: It will create a class that links a farmer_id (phone number) to a crop_name, along with quantity, quality, and asking_price.
Relationship: It is the core of the marketplace. It will be created by harvest_service.py and read by both farmer_menu.py and buyer_menu.py.



Phase 2: The Tools (Utilities) - src/utils/
Now, build the tools that the rest of the app will depend on.

1. src/utils/data_handler.py (THE MOST IMPORTANT FILE)
Purpose: To read from and write to the JSON files. This is your simple database.
What it will do: It will contain two key functions:
read_json(file_path): Opens a file (e.g., users.json) and returns the data as a Python list.
write_json(data, file_path): Takes a Python list and saves it to a file (e.g., users.json).
Relationship: EVERY SERVICE (user_service.py, harvest_service.py) will import and use this file to save and load data.

2. src/utils/validators.py
Purpose: To check if user input is valid.
What it will do: It will contain functions like:
validate_phone_number(phone): Checks if it's an 11-digit number starting with 0.
validate_pin(pin): Checks if it's 4 digits.
Relationship: It will be used by user_service.py during registration and by menu files when taking input.




Phase 3: The Doers (Business Logic) - src/services/
With your models and tools ready, you can now build the logic.

1. src/services/user_service.py
Purpose: To handle all user-related operations.
What it will do: Its functions will:
Register: Take user details, use validators.py, create a Farmer or Buyer object, and use data_handler.py to save it to users.json.
Login: Take a phone and PIN, use data_handler.py to search users.json, and return the user object if found.
Relationship: It uses models/ to create objects and utils/ to save them. It is called by main_menu.py.

2. src/services/harvest_service.py
Purpose: To manage all harvest listings
What it will do: Its functions will:
Create Listing: Take details from a farmer, create a Harvest object, and use data_handler.py to save it to harvests.json.
Get Listings: Use data_handler.py to read harvests.json and return available crops.
Relationship: It uses the Harvest model and the data_handler. It is called by farmer_menu.py and buyer_menu.py.

3. src/services/market_service.py
Purpose: To provide market price information.
What it will do: It will use data_handler.py to read pre-loaded price data from market_prices.json and return it.
Relationship: It is a simple service that will be called by both farmer and buyer menus.





Phase 4: The Brain (Session & Menus) - src/interfaces/
Now, build the user interface that ties everything together.

1. src/interfaces/session_manager.py
Purpose: To track the current state of the app.
What it will do: It will create a Session object that stores:
current_user: Who is logged in? (A Farmer or Buyer object)
is_authenticated: Are they logged in?
menu_history: The stack of menus for the "back" button.
Relationship: EVERY MENU will check the session to see who is logged in and what they can do.

2. src/interfaces/base_interface.py (Abstract Class)
Purpose: The blueprint for every menu.
What it will do: It will force every menu to have a display() method (to show options) and a handle_input() method (to process user choice).
Relationship: It is the parent class for all other menus.

3. src/interfaces/main_menu.py
Purpose: The first screen users see.
What it will do: Its display() method will show "1. Login, 2. Register...". Its handle_input() will call user_service.py functions and then switch to farmer_menu.py or buyer_menu.py.
Relationship: It is the entry point. It uses user_service.py and changes the session_manager.

4. src/interfaces/farmer_menu.py & buyer_menu.py
Purpose: The menus users see after logging in.
What they will do: Their display() method will show options like "Check Prices, List Harvest". Their handle_input() will call the appropriate service (market_service.py, harvest_service.py) and display the results.
Relationship: They are the core user experience. They use all the services and the session.




Phase 5: The Engine & Data - Final Files
1. src/main.py
Purpose: The core program that runs the USSD simulation.
What it will do: It will contain a while True: loop that:
Checks the session_manager for the current menu.
Displays that menu.
Takes user input.
Sends the input to the menu's handle_input() method.
Repeats.
Relationship: This file imports and runs everything. It is the heart of the application.

2. data/users.json, harvests.json, etc.
Purpose: Your simple database files.
What they will do: They will start as empty arrays []. As your app runs, the data_handler.py will fill them with data.
Relationship: They are the destination for all saved data and the source for all loaded data.

3. run.py (in the main folder)
Purpose: A simple launcher script.
What it will do: It will have 2 lines:



                                                        File Responsibility

Team Member 1: Project Structure & Base Model
Create the project structure with proper directories
Implement src/models/__init__.py
Implement src/models/user.py (Abstract Base Class)
Ensure proper package structure and imports

B. Integration & Testing
Create basic unit tests for all models
Verify relationships between models work correctly
Set up a simple script to test model instantiation
Ensure all team members' code integrates properly


Team Member 2: User Specializations
Implement src/models/farmer.py
Ensure proper inheritance from the User base class
Add appropriate validation for specialized attributes


Team Member 3: User Specializations
Implement src/models/buyer.py
Ensure proper inheritance from the User base class
Add appropriate validation for specialized attributes

Team Member 4: Core Marketplace Model
Implement src/models/harvest.py
Design the relationships between Harvest and other models
Implement proper data validation
