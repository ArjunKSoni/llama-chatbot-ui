
Chatbot: Arjun Creation
=======================

This repository contains a chatbot application built using [Streamlit](https://streamlit.io/). The application interacts with various APIs to provide chat, Q&A, and search functionalities.

Features
--------

*   **Chat API:** Engage in a conversation with the chatbot. The API streams responses for a dynamic and real-time chat experience.
*   **Ask API:** Ask questions and receive direct answers from the chatbot.
*   **Search API:** Perform web searches using the chatbot to retrieve relevant information.

Setup and Installation
----------------------

To run this application locally, follow these steps:

1.  Clone the repository:

    git clone https://github.com/your-repo/chatbot-app.git

3.  Navigate to the project directory:

    cd chatbot-app

5.  Install the required packages:

    pip install -r requirements.txt

7.  Run the Streamlit application:

    streamlit run app.py

9.  Open your browser and navigate to [http://localhost:8501](http://localhost:8501) to view the app.

Usage
-----

After starting the application, you will be presented with a simple interface where you can choose between the Chat API, Ask API, and Search API.

1.  **Select API:** Use the sidebar to choose which API you want to interact with.
2.  **Enter your input:** Use the chat input at the bottom of the page to type your query or message.
3.  **Receive responses:** The chatbot will display responses in real-time as they are streamed from the selected API.

Available Endpoints
-------------------

The application provides the following endpoints:

*   **/chat**: Handles chat requests with conversation history. The chatbot will maintain context and provide responses accordingly.
*   **/ask**: Handles Q&A requests without maintaining conversation history. This is ideal for direct and one-time queries.
*   **/search**: Performs web searches based on user input and returns relevant information.

Testing the Application
-----------------------

For testing purposes, you can use the following test endpoint:

    https://llama-chatbot-ui.onrender.com/

Running the APIs Locally
------------------------

To test the APIs locally, you can use tools like [Postman](https://www.postman.com/) or [HTTPie](https://httpie.io/). Here’s how to make requests to each API:

1.  **Chat API:**

    
    POST http://localhost:8000/chat
    Content-Type: application/json
    {
        "input": "Your chat message here"
    }
        

3.  **Ask API:**

    
    POST http://localhost:8000/ask
    Content-Type: application/json
    {
        "input": "Your question here"
    }
        

5.  **Search API:**

    
    POST http://localhost:8000/search
    Content-Type: application/json
    {
        "input": "Your search query here"
    }
        
