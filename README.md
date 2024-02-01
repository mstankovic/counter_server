# counter web server
This is simple web server
## deploy
```shell
git clone https://github.com/mstankovic/counter_server.git
cd counter_server
pip install -r requirements.txt
gunicorn app:app 
```
## api usage
There are 3 endopints:
1. /get ['GET'] - to get current counter value
2. /add ['POST'] - to increase counter for 1, required body:
```json
{
    "increment": 1
}
```
3. /reset ['POST'] - to reset counter value to 0
## web usege
1. You can "Increment Counter" which will increase counter for 1.
2. "Refresh" the counter and get current value
3. "Reset" counter value to 0 (zero)