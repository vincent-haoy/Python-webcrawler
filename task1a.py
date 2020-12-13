{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import csv\n",
    "import json\n",
    "import requests\n",
    "import unicodedata\n",
    "import textdistance\n",
    "import pandas as pd\n",
    "from numpy import arange\n",
    "from bs4 import BeautifulSoup\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.pyplot as plts\n",
    "\n",
    "\n",
    "output = open(\"task1a.csv\",\"w\",newline='')\n",
    "google_small = open(\"google_small.csv\", \"r\")\n",
    "amazon_small = open(\"amazon_small.csv\", \"r\")\n",
    "amazon = csv.DictReader(amazon_small)\n",
    "google = csv.DictReader(google_small)\n",
    "\n",
    "with open('task1a.csv', 'w+', newline='') as csv_file:\n",
    "    writer = csv.writer(csv_file)\n",
    "    writer.writerow(['idAmazon','idGoogleBase'])\n",
    "    for gitem in google:\n",
    "        amazon_small.seek(0)\n",
    "        stripedg = re.sub('(){<-:}','',gitem['name'])\n",
    "        for aitem in amazon:\n",
    "            stripeda = re.sub('(){<>[-:]}','', aitem['title'])         \n",
    "            if (textdistance.cosine.normalized_distance(stripeda.split(' '),stripedg.split(' ')) < 0.5):\n",
    "                   writer.writerow([aitem['idAmazon'],gitem['idGoogleBase']])\n",
    "output.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
