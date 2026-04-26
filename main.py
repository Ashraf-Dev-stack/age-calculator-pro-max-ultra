{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO4Cns10BPkzVX13X9UxUkR"
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
      "cell_type": "code",
      "source": [
        "import sys\n",
        "import time\n",
        "from datetime import datetime\n",
        "from dateutil.relativedelta import relativedelta\n",
        "\n",
        "def slow_print(text, delay=0.03):\n",
        "    for char in text:\n",
        "        sys.stdout.write(char)\n",
        "        sys.stdout.flush()\n",
        "        time.sleep(delay)\n",
        "    sys.stdout.write('\\n')\n",
        "\n",
        "slow_print(\"--- Age Calculator Pro Max Ultra ---\")\n",
        "slow_print(\"Enter your birth date: YYYY-MM-DD\")\n",
        "slow_print(\"Or with time if you remember: YYYY-MM-DD HH:MM:SS\")\n",
        "\n",
        "user_input = input(\"Your birth date: \")\n",
        "\n",
        "try:\n",
        "    # If user entered date + time\n",
        "    birth = datetime.strptime(user_input, \"%Y-%m-%d %H:%M:%S\")\n",
        "except ValueError:\n",
        "    # If user entered date only, assume 00:00:00 midnight\n",
        "    birth = datetime.strptime(user_input, \"%Y-%m-%d\")\n",
        "\n",
        "now = datetime.now()\n",
        "diff = now - birth\n",
        "seconds = diff.total_seconds()\n",
        "delta = relativedelta(now, birth)\n",
        "\n",
        "slow_print(f\"You have been alive for:\")\n",
        "time.sleep(0.5)\n",
        "slow_print(f\"{delta.years} years, {delta.months} months, {delta.days} days\")\n",
        "time.sleep(0.5)\n",
        "slow_print(f\"That's about {seconds:,.0f} seconds\")\n",
        "time.sleep(0.5)\n",
        "slow_print(f\"Or {seconds * 1000:,.0f} milliseconds 🔥\")\n",
        "time.sleep(0.5)\n",
        "slow_print(f\"Or {seconds * 1000000:,.0f} microseconds... you're ancient 😂\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "okqDOS5qYox8",
        "outputId": "45d62766-f33f-448f-fdd3-637d805650d3"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "--- Age Calculator Pro ---\n",
            "Enter your birth date: YYYY-MM-DD\n",
            "Or with time if you remember: YYYY-MM-DD HH:MM:SS\n",
            "Your birth date: 2011-7-27\n",
            "You have been alive for:\n",
            "14 years, 8 months, 30 days\n",
            "That's about 465,470,971 seconds\n",
            "Or 465,470,971,043 milliseconds 🔥\n",
            "Or 465,470,971,043,369 microseconds... you're ancient 😂\n"
          ]
        }
      ]
    }
  ]
}