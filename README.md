# counter web server
This is simple web server
## deploy
```shell
git clone https://github.com/mstankovic/counter_server.git
cd counter_server
pip install -r requirements.txt
gunicorn app:app 
```
## usage
There are 2 endopints:
1. /get ['GET'] - to get current counter value
2. /add ['POST'] - to increase counter for one, required body:
```json
{
    "increment": 1
}
```
You can "Refresh" counter to get current counter value or you can "Increment Counter" which will increase counter for 1. 