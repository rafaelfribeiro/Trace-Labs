# Trace-Labs Test
Welcome to Ethereum transactions crawler task
The project was a task for a interview for Trace Labs

# First steps
 - Clone / Download project
 - Go to the path and (setup your enviorment if you want) run ```pip install -r requirements.txt``` to download dependencies.
 
# Run the project!
 - Open terminal/cmd in path
 - I recommend to run in development to raise errors in case that occur. So:
 - - ( Windows ) - run ```SET FLASK_ENV=development```
 - - ( linux ) - run ```export FLASK_ENV=development```
 - Then just run the project ```flask run --host=0.0.0.0 --port=80```

 OBS.: In case you have Apache runnig or other program using ```port 80``` you can just try run in ```--port=801``` or another one.


## Usage of Pages
Since wasn't anything to store in task I decided to don't use any database.
### In ```Home``` you can:
- Check the current price of Ethereum and Bitcoin in USD
- Check the latest Blocks of Ethereum and Miner responsable
- Check an Ethereum Address by inserting an address and starting Block (optional)

- Check an Bitcoin Address by clicking in Bitcoin price section and inserting the address

### ```Default Address```
- Current balance of your Address
- List of transactions/contracts
- Select a block, transaction or address to check by clicking on list

### ```Default Block```
- Check informations about Block like transactions, Miner, difficult and more...


