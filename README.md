# FIFA Data Visualization


## About the project

This is the final project for the [DCC030 - Data Visualization](https://homepages.dcc.ufmg.br/~raquelcm/index.php?alias=visualizacao) class. It consists in different visualization using data from the EA Sports FIFA games. Using the data from FIFA games, we can make a comparison between games and reality, according to the players, their clubs and their market values. It is mainly based on FIFA 20 data, but previus versions of the game were considered in some visualizations. The database used can be found on Kaggle [here](https://www.kaggle.com/stefanoleone992/fifa-20-complete-player-dataset).

This database provides us all the players present in the games, from edition 15 to 20, making it possible to study several time series. Focusing our attention on FIFA 20, there are 104 different variables to be explored; among them:
- Personal characteristics of the players (dates of birth, salaries, nationalities)
- Information about clubs and national teams (country, value)
- Statistics of the players's attributes (skills, kicking power, launch accuracy)

### Built With

* [Plotly](https://plotly.com/)
* [Dash](https://dash.plotly.com/)
* [Bootstrap](https://dash-bootstrap-components.opensource.faculty.ai/)

## Usage

You can explore the visualizations in a web application [here](https://fifa-infovis.herokuapp.com/). The app is hosted on Heroku using a free plan, so it can take a couple seconds to the page be fully loaded (but it is free :smile:).

## Using a local server

If you want, you can explore the visualizations in a local server hosted in your own machine.

### Prerequisites

You will need Python3 and the packages used in the project.

### Installation

1. Clone the repo
```sh
$ git clone https://github.com/alvaro-rodrigues/fifa-infovis.git
```
2. Install Python packages
```sh
$ pip install -r requirements.txt
```
### Accessing the application

1. Run the application
```sh
$ python app.py
```
2. Open your browser and go to this adress: `http://127.0.0.1:5000/`

## Demonstration video

You can found more about the project watching the demonstration video.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1CaibmPOb8A/0.jpg)](https://www.youtube.com/watch?v=1CaibmPOb8A)

## Authors
* **Álvaro Rodrigues** - *Web application, plots 1 and 2* - [alvaro-rodrigues](https://github.com/alvaro-rodrigues)
* **Guilheme Miranda** - *Plots 9, 10 and 11* - [guilhermealbm](https://github.com/guilhermealbm)
* **Luiz Guilherme Leroy** - *Plots 3, 4 and 5* - [guilhermeleroy](https://github.com/guilhermeleroy)
* **Wesley Maciel** - *Plots 6, 7 and 9* - [WesleyM2510](https://github.com/WesleyM2510)

## License

Distributed under the MIT License. See `LICENSE` for more information.