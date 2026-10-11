{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM0D9319m5wHq+79TLsEBiu",
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
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "znPtLlkKIxK6",
        "outputId": "49367e86-4b16-4c6f-e6db-784e93309f9e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "surya\n",
            "22\n",
            "MCA\n",
            "Not Found\n",
            "{'name': 'surya', 'city': 'Kaviti'}\n",
            "name\n",
            "age\n",
            "course\n",
            "name surya\n",
            "age 22\n",
            "course MCA\n"
          ]
        }
      ],
      "source": [
        "student = {\n",
        "    \"name\": \"surya\",\n",
        "    \"age\": 22,\n",
        "    \"course\": \"MCA\"\n",
        "    }\n",
        "+\n",
        "print(student[\"name\"])\n",
        "print(student.get(\"age\"))\n",
        "print(student.get(\"course\"))\n",
        "print(student.get(\"city\", \"Not Found\"))\n",
        "\n",
        "\n",
        "student = {\"name\": \"surya\", \"age\" : 22}\n",
        "student[\"city\"] = \"Kaviti\"\n",
        "student.update({\"age\":22})\n",
        "student.pop(\"age\")\n",
        "print(student)\n",
        "\n",
        "d = {\"name\": \"surya\", \"age\": 22, \"course\": \"MCA\"}\n",
        "\n",
        "# Print only keys\n",
        "for key in d.keys():\n",
        "    print(key)\n",
        "\n",
        "# Print keys and values\n",
        "for key, value in d.items():\n",
        "    print(key, value)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 18\n",
        "if age<=20:\n",
        "    print(\"eligible\")\n",
        "num = [x for x in range(1,7)]\n",
        "print(num)\n",
        "\n",
        "cube = [x * x for x in range(1, 10)]\n",
        "print(cube)\n",
        "\n",
        "even = [x for x in range(1,10) if x % 2 == 0]\n",
        "print(even)\n",
        "\n",
        "odd  = [x for x in range(1,5) if x % 2 != 0]\n",
        "print(odd)\n",
        "\n",
        "\n",
        "name = [\"surya\",\"sai\",\"raju\"]\n",
        "result = [name.upper() for name in name]\n",
        "print(result)\n",
        "\n",
        "\n",
        "name = [\"surya\", \"vasu\",\"raju\"]\n",
        "result = [name.lower() for name in name]\n",
        "print(result)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s9gL7RLNJtWR",
        "outputId": "9c1cd0c8-23dc-4c29-84ef-59d142196024"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "eligible\n",
            "[1, 2, 3, 4, 5, 6]\n",
            "[1, 4, 9, 16, 25, 36, 49, 64, 81]\n",
            "[2, 4, 6, 8]\n",
            "[1, 3]\n",
            "['SURYA', 'SAI', 'RAJU']\n",
            "['surya', 'vasu', 'raju']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "friut = [\"apple\",\"Mango\",\"Kiwi\",\"Grape\"]\n",
        "marks = [88,25,67,89]\n",
        "mixed = [\"MCA\", 1, 9.4, True]\n",
        "print(friut[1])\n",
        "print(friut[-1])\n",
        "print(marks[2])\n",
        "print(mixed)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ekXrRxl8KABj",
        "outputId": "f4bb145f-a9d1-4597-9a66-a64f499920a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mango\n",
            "Grape\n",
            "67\n",
            "['MCA', 1, 9.4, True]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "name =  [\"Surya\",\"sai\",\"vasu\",\"nani\"]\n",
        "age = [12,18,19,21,22]\n",
        "course = [\"MCA\", 2, 8.3, True]\n",
        "print(name[0])\n",
        "print(age[-1])\n",
        "print(course)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pjRPW3TzKMmP",
        "outputId": "77bb1599-c44e-4964-c652-f537fda742c6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Surya\n",
            "22\n",
            "['MCA', 2, 8.3, True]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = [10,20,30,40,50]\n",
        "print(num[1:4])\n",
        "print(num[:3])\n",
        "print(num[::2])\n",
        "print(num[::-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L8_Gjoq8KVXi",
        "outputId": "e2aaa2af-de4f-4c16-e01f-728537e91cfe"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[20, 30, 40]\n",
            "[10, 20, 30]\n",
            "[10, 30, 50]\n",
            "[50, 40, 30, 20, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = [10,20,30,40,50]\n",
        "reverse = (num[::-1])\n",
        "print(reverse)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "io0NlV1XKj1b",
        "outputId": "bc8f2170-a60c-4670-bb25-f92f7d622e88"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[50, 40, 30, 20, 10]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fruit = [\"apple\", \"mango\"]\n",
        "\n",
        "fruit.append(\"Grape\")\n",
        "print(fruit)\n",
        "\n",
        "fruit.insert(1, \"Kiwi\")\n",
        "print(fruit)\n",
        "\n",
        "fruit.append(\"Banana\")\n",
        "print(fruit)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VOADcocGKq1M",
        "outputId": "845adeed-0102-4c05-b9a0-d3b35559f9f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['apple', 'mango', 'Grape']\n",
            "['apple', 'Kiwi', 'mango', 'Grape']\n",
            "['apple', 'Kiwi', 'mango', 'Grape', 'Banana']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "1##if Statement##\n",
        "avg = 10\n",
        "if avg >=0:\n",
        "    print(\" Eligible\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zXtP0qUlKzCl",
        "outputId": "20c23c7e-49ed-4393-ba70-8e3d16ff4cb0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Eligible\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "3##if-elif-else Ladder ##\n",
        "marks = 75\n",
        "if marks >= 80:\n",
        "    print(\"Grade A\")\n",
        "elif marks >= 75:\n",
        "    print(\"Grade B\")\n",
        "elif marks <= 40:\n",
        "    print(\"Grade c\")\n",
        "else:\n",
        "    print(\"Fail\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QYLrar6OLUYP",
        "outputId": "bd007bef-7e2e-46ea-8c02-523af10d9f04"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Grade B\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "age = 20\n",
        "\n",
        "if age >= 18 and age <= 30:\n",
        "    print(\"Eligible\")\n",
        "\n",
        "#2.or\n",
        "    marks = 80\n",
        "\n",
        "if marks >= 90 or marks >= 75:\n",
        "    print(\"Good marks\")\n",
        "#3.n\n",
        "is_raining = False\n",
        "if not is_raining:\n",
        "        print(\"You can go outside\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XOCbhDrJLglY",
        "outputId": "7b084d0a-d465-464f-dda6-a7a05e24ca9c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Eligible\n",
            "Good marks\n",
            "You can go outside\n"
          ]
        }
      ]
    }
  ]
}