{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPxINd0InNkyQhKW/rB5aAu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/suryagara888-hue/26M11MC023.py/blob/main/26M11MC023.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "N8dJNxpUORWv",
        "outputId": "85f6620b-8670-429e-80a6-26e9d7bca7a7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Repeated words found: ['is']\n"
          ]
        }
      ],
      "source": [
        "import re\n",
        "text = \"This is is a simple text of regex\"\n",
        "pattern = r\"\\b(\\w+)\\s+\\1\\b\"\n",
        "repeats = re.findall(pattern, text, flags=re.IGNORECASE)\n",
        "print(\"Repeated words found:\", repeats)\n"
      ]
    }
  ]
}