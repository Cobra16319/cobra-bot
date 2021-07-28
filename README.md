[![CodeQL](https://github.com/Cobra16319/cobra-bot/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Cobra16319/cobra-bot/actions/workflows/codeql-analysis.yml)


# Cobra-Bot


Project to run a discord bot that can pull Coin Market Cap (Cryptocurrency) data into discord. Project also comes with scale to run it in AWS for global scale to provision, connect, secure & run as many bots and servers as you want.


# Setup a Python IDE or your local shell, get it working locally on your machine with our API keys.

# You need the Following 

* discord account 
* application 
* a bot and a guild or a server
* An AWS account if you want to run it full time (If not skip provision portion) 
* This provision script deployes 42 resources but can run up to 2 million servers. Scale as you need. 

## Set it up and allow your bot first. Then get we can code follow below for my code and cobra-bot

Setting up
------------
Assuming your project (Virtual Env)  named "Discord" on your Desktop. (I will be adding a section to use Vault for keys.) Ensure you use your discord keys in a safe way for dev.

### Starting from scratch
	$ easy_install pip
	
	$ pip install virtualenv
	
	$ git clone "this url"
	
	$ discord python3 -m venv discord
        
	$ discord source discord/bin/activate

	$ pip install -U discord.py

	$ python bot.py 

	$ export COINMARKETCAP_API_KEY='yourkey'  (Don't worry using vault later)

	$ python cmtest.py

## This is assuming you know how to setup a normal discord bot in the GUI. If not google it.  



## Links below for documentation on discord API, CMC API, and some HashiCorp Learn links I found useful.

* https://discordpy.readthedocs.io/en/latest/api.html#
* https://coinmarketcap.com/api/documentation/v1/#section/Introduction
* https://learn.hashicorp.com/collections/terraform/aws-get-started
* https://learn.hashicorp.com/tutorials/consul/get-started-create-datacenter
* https://learn.hashicorp.com/tutorials/nomad/consul-service-mesh
