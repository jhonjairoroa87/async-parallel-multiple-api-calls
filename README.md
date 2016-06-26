# Async parallel multiple api calls
Show a simple way do multiple parallel calls to api's using Queue and Threads in python  2.7

## Configuring the application

1. Clone the project:
`$ git clone https://github.com/jhonjairoroa87/async-parallel-multiple-api-calls`
2. Install project requirements:
`pip install -r requirements.txt`

## Running the application
Run the following command
`python runserver.py`

## Verifying the application is up
Call one of the following urls in your browser:
 - http://0.0.0.0:5000/
 
# Execute synchronous call
Call the following api call, that would take between 2.10 and 2.11 seconds
 - http://0.0.0.0:5000/sync
 
You will get a string like this:
`I just called users, posts and photos in --- 2.11214399338 seconds ---`
 
This is an example of the time that takes to every call that is done sequentially:
```
    --- 0.000169038772583 seconds --- init photos download
    --- 0.90238904953 seconds --- end photos download
    --- 0.902453184128 seconds --- init posts download
    --- 1.60568118095 seconds --- end posts download
    --- 1.60580420494 seconds --- init users download
    --- 2.11058807373 seconds --- end users download
```

   

# Execute asynchronous call
Call the following api call, that would take between 0.9 and 1 seconds
 
 - http://0.0.0.0:5000/async
 
You will get a string like this:
`I just called users, posts and photos in --- 0.904438972473 seconds ---`
 
This is an example of the time that takes to every call that is done sequentially:
```
    --- 0.000602960586548 seconds --- init photos download
    --- 0.000463962554932 seconds --- init posts download
    --- 0.000311136245728 seconds --- init users download
    --- 0.50043296814 seconds --- end users download
    --- 0.700552940369 seconds --- end posts download
    --- 0.900881052017 seconds --- end photos download
```

Useful links:
 - [Queue – A thread-safe FIFO implementation](https://pymotw.com/2/Queue/)
 - [8.10. Queue — A synchronized queue class](https://docs.python.org/2.7/library/queue.html#Queue.Queue.join)
 - [Python Threading and Queues – and why it’s awesome](http://lonelycode.com/2011/02/04/python-threading-and-queues-and-why-its-awesome/)