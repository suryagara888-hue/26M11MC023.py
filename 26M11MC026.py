{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOJZQwUvjW6iGf8gDOmUXOi",
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
        "<a href=\"https://colab.research.google.com/github/suryagara888-hue/26M11MC023.py/blob/main/26M11MC026.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "KMogt9tyWEaA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "pattern = r\"^[\\w.+-]+@[w-]+\\.[a-zA-Z]{2,}$\"\n",
        "def is_valid_email(email):\n",
        "    return bool(re.match(pattern, email))\n",
        "print(is_valid_email(\"surya.@college.com\"))\n",
        "print(is_valid_email(\"sai-email@@x\"))\n",
        "print(is_valid_email(\"yes-at-symbol.com\"))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NZaH9W1SWJJ1",
        "outputId": "59653a1d-16b5-4ac3-a777-5b4a6b3f4e87"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n",
            "False\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#Email Validation using Regex#\n",
        "import re\n",
        "\n",
        "email = input(\"Enter Email : \")\n",
        "\n",
        "pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'\n",
        "\n",
        "if re.fullmatch(pattern, email):\n",
        "    print(\"Valid Email\")\n",
        "else:\n",
        "    print(\"Invalid Email\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jHiFr7vfZ0a0",
        "outputId": "155887bf-4f00-4d5b-b075-db7c5d2599f1"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Email : suryagara@gmail.com\n",
            "Valid Email\n"
          ]
        }
      ]
    }
  ]
}