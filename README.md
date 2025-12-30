## FastAPI E-commerce Backend
---
## Features
### Authentication
- Signup with email + password
- Login with JWT token generation
- Password hashing using bcrypt

### Authorization
- Protected routes using JWT
- Only logged-in users can:
  - Create, update, delete products

### Products
- CRUD operations
- Public GET access
- Private access to POST, PUT, DELETE
---

## Getting Started

### 1. Clone the Repo
https://github.com/Aashutosh17/E-commerce_Backend.git

### 2.  Create Virtual Environment
python -m venv .venv   
source .venv/bin/activate 

### 3. Install Requirements
pip install -r requirements.txt

### 4. Set Up .env File
MONGO_URL=mongodb://localhost:27017
SECRET_KEY=your_secret_key_here

### 5. Run the Server
uvicorn app.main:app --reload

### 6. Test APIs
Go to: http://127.0.0.1:8000/docs  
Use Swagger UI or Postman to test endpoints.
---

### Learning Outcomes
FastAPI fundamentals  
MongoDB async operations  
JWT authentication  
API security best practices  
Git branching and collaboration workflow  
Real-world backend architecture
---




















