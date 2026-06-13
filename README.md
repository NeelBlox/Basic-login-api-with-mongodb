## Live Demo

https://basic-login-api-with-mongodb.onrender.com/docs

# Basic Login API with MongoDB

A simple FastAPI authentication API using:

- FastAPI
- MongoDB Atlas
- Argon2 password hashing
- Login cooldown protection
- Environment variable support

## Features

- User login endpoint
- Password hashing with Argon2
- MongoDB Atlas integration
- 10-second login cooldown
- Deployable on Render

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## MongoDB Setup

Create a MongoDB Atlas cluster and database.

Update the collection names in the code if necessary.

### Environment Variables

Create a `.env` file:

```env
MONGO_URI=your_mongodb_connection_string
```

Or configure the environment variable through your hosting provider.

## Running Locally

Add the following to the bottom of `main.py`:

```python
if __name__ == "__main__":
    uvicorn.run(app)
```

Start the API:

```bash
python main.py
```

## API Endpoints

### GET /

Returns API status.

### POST /login

Request body:

```json
{
  "username": "user1",
  "password": "password"
}
```

Example response:

```json
{
  "success": true,
  "message": "Successfully logged in!"
}
```

## Deployment

This project can be deployed for free on platforms such as:
( if help required kindly ask it in the discussions or issues tab! )

- Render
- Railway
- Fly.io

## License

Open source and available under the MIT License.
