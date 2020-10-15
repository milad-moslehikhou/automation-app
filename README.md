# Automation App

## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Startup](#startup)
* [Usage](#usage)


<!-- ABOUT THE PROJECT -->
## About The Project
This program helps you to perform predefined tasks automatically by receiving alerts from other programs 
such as Zabbix, Prometheus, etc.

<!-- BUILD WITH -->
### Built With
* [Django]()


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

<!-- PREREQUISITES -->
### Prerequisites

* Docker [v19.03.8]
* docker-compose [v3.7]

<!-- STARTUP -->
### Startup
1. Clone project
```sh
git clone https://github.com/milad-moslehikhou/automation-app.git
```
2. Use the following command to build and up project
```sh
docker-compose up -d --build
```

<!-- USAGE -->
## Usage
This program provides a rest api to communicate with other programs.
For more information you can see api documents page in `/swagger`