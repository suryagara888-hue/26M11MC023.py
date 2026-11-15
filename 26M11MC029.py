{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNXl1RMiZA3OyxzYchkgA4M",
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
        "<a href=\"https://colab.research.google.com/github/suryagara888-hue/26M11MC023.py/blob/main/26M11MC029.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t87CPIGvgy8z",
        "outputId": "474bf16c-5b0c-4633-9e71-511c61a9863d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['cat', 'dog']\n",
            "<re.Match object; span=(0, 3), match='cat'>\n",
            "<re.Match object; span=(16, 19), match='cow'>\n"
          ]
        }
      ],
      "source": [
        "import re\n",
        "text = \"cat and dog and cow\"\n",
        "print(re.findall(r\"cat|dog\",text))\n",
        "print(re.search(r\"^cat\",text))\n",
        "print(re.search(f\"cow$\",text))"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#password Strength Checker#\n",
        "import re\n",
        "\n",
        "password = input(\"Enter Password : \")\n",
        "\n",
        "pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@#$%^&+=!]).{8,}$'\n",
        "\n",
        "if re.fullmatch(pattern, password):\n",
        "    print(\"Strong Password\")\n",
        "else:\n",
        "    print(\"Weak Password\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aUVcGUWMtLID",
        "outputId": "f016fe3e-aa79-41cb-f2c8-82c0d34cb0f4"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Password : Adityacollege@344.gmail.com\n",
            "Strong Password\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#moblie Number Validation#\n",
        "import re\n",
        "moblie = input(\"Enter Moblie Number :\")\n",
        "\n",
        "if re.fullmatch(r'[6-9]\\d{9}',moblie):\n",
        "    print(\"Valid mobile Number\")\n",
        "else:\n",
        "    print(\"Invalid Moblie Number\")\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rJmtdq1mxqJ6",
        "outputId": "610d3c5a-a139-4ff3-f201-b858b0e76d1f"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter Moblie Number :9398418467\n",
            "Valid mobile Number\n"
          ]
        }
      ]
    }
  ]
}