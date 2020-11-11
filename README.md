# Yahoo Finance Stock Reporter
Hi! Welcome.

**TLDR;** This is a python program that takes in stock tickers as input and scrapes data from Yahoo finance.  It generates reports that automatically open in the browser on program completion.

*Please note that this project is very early in development, it's quite featureless currently.  It will likely remain this way forever*

### Current Functionality
* Takes single stock ticker as input
  * Right now just edit the stock ticker const in `main.py` and then run this from any CLI
    ```shell
    > python main.py
    ```
* Upon successful program completion this will open several tabs in a chrome browser containing html tables with a stocks quarterly/annual Balance Sheet/Income Statement/Cash Flow
  * Aka stuff you can see [on this page](https://finance.yahoo.com/quote/MSFT/financials)
    ![Image of program output](https://lh3.googleusercontent.com/B1ISBEo0PbM6xf_2o7LYdvGLzxduVG52SsvCoZHDyqbeU9Lgy9_Gbjz0ojyI-dniV14Fpx2KkBASE5WgmxOh062_amkeA6OBO5hdBHozlCRDMuEjZvwzQLISP2qT8KgeyM-D0vD00W6NfYz4NEMzAthTHM6kNlSA7Rrm7eHWL4SsGsJvuJxT2nIFxoRYyDvJ2ANSxysApSwCoJ0rQgMDiTyGgAfupbQMxXW8iODPXligMi3zXZTaXTnE_B95bSw4Ddtxs_9XLe_3fZjxb8noOWGSc7C2lU2IjYitwiWGfAguO5OsuCVJ1d6626U1mYnL65BL3BWLppr5-ZhTyxI4v7Us-BcB1yyV7uuTxkBSwYCABHtHKYpL9TogpneBCLuVW_3TeirxxEJX3kPmuyoPiMsnVdnJh6B6P89J8-IBM_K2eGgYWYMKX56KayA8EqOOHsqVotyC7Obij5dkyq9MIVwiRhzEQYlk77DkZ2Ekr3pNzaS7xeDw3RgGGt_-0SL4VG0wpCfqmlTOaEkqe42Lyj9EjhbgbZ6zWzO5q4N6bjvFM-IkGPB19Vg7KPrHEvvV9zkOYghTAU7YMMdljyyZd4-Gs-MWg3l9j0LQzrvDiYtg3BkOaqjn9Hma7G6uQzwJXhMt7oeorJuZwgQMQf_HI7mu0f-7UgZ1yTHpc3n_0IbBunN0Kaa0DQIoVOKISJWyrEPykjbAS-ko-3ZsHsvOKbINHS_ZeVXtaRlfQ17WhJoVhO2qmamYEIcc=w694-h537-no?authuser=0)
* Copies a list of seemingly random meta data (in JSON format) about the stock to your clipboard
  * This is done since the Chrome plugin I use to render JSON is only there when logged in
  * It's unlikely this exact functionality will be long lived as the program get's more scoped to only grab data it cares about

### Requirements
* Chrome
* Python 3
  * Look at the top of main.py and pip install all those libs to run this program
* A stock ticker

### Beware!
* As with any web crawler, your IP could get banned/suspended for scraping
* This program is not *yet* optimized to attempt to avoid this (I do plan on adding that at some point once this is ready to crank on lots of stock tickers)
* So, be careful.  Don't run this in a loop or anything unless you understand the script/underlying libs enough to add proxies

### The Future...
I have big plans for this script.  My goal is to have it run on an array of stock tickers and run calculations on their financials/stock price to print out growth %'s, rations like p/e, basically any data that can be used to determine a stocks value/flag it for further investigation
At this point you may have guessed I am into investing, specifically long term hold value based investing.  I want to find growing undervalued companies in sectors/industries that I want to bet on for big growth in the next 5/10 years

Feel free to reach out to me with any question here on Github :)
