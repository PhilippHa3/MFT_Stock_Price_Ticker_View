## Stock Price Ticker View

You're tasked with making a "frontend/client" and "backend/server" application, which displays Stock Prices. 
You should not spend more than 1-2 hours on this, as it only serves as a common talking point. Furthermore, there will be no penalty for not finishing the assignment completely, as mentioned before, its just a common talking point.

We would prefer you solve the excercise using C# and .NET Core or Python.

# Requirements are as follows:

- Stock Price Model:
  - Should have a price with decimal support
  - Should have a Name, eg: Google, Apple, Microsoft, Berkshire etc.
  - Extend with extra information, if you have the time, but not needed.
  - Generated Prices do not need to look "real"(random prices are sufficient).

- Frontend/Client:
  - Should receive "Stock Price Models" from the backend.
  - These prices should be displayed in a human readable format
  - This can just be something as simple as a console application

- Backend/Server
  - Generate "Stock Price Models" every 1-2 seconds.
  - The generated "Stock Price Models" should be the same set of Stocks (Apple, Google, Microsoft etc.) every time
  - Send the generated prices to the frontend using network communication
