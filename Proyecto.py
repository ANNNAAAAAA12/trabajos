{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNsisG9wgJkmaL3RjtmzWh7",
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
        "<a href=\"https://colab.research.google.com/github/ANNNAAAAAA12/trabajos/blob/main/Proyecto.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gIbsJgqW69NR"
      },
      "outputs": [],
      "source": [
        "def int_a_bin(valor):\n",
        "    if valor < 0:\n",
        "        return format((1 << 32) + valor, '032b')\n",
        "    return format(valor, '032b')\n",
        "\n",
        "def float_a_bin(valor):\n",
        "    signo = 0 if valor >= 0 else 1\n",
        "    valor = abs(valor)\n",
        "\n",
        "    exponente = 127\n",
        "    while valor < 1:\n",
        "        valor *= 2\n",
        "        exponente -= 1\n",
        "    while valor >= 2:\n",
        "        valor /= 2\n",
        "        exponente += 1\n",
        "\n",
        "    mantisa = valor - 1\n",
        "    bits_mantisa = ''\n",
        "    for _ in range(23):\n",
        "        mantisa *= 2\n",
        "        bit = int(mantisa)\n",
        "        bits_mantisa += str(bit)\n",
        "        mantisa -= bit\n",
        "\n",
        "    bits_exponente = format(exponente, '08b')\n",
        "    bits_mantisa = bits_mantisa[:23]\n",
        "\n",
        "    return f\"{signo}{bits_exponente}{bits_mantisa}\", signo, bits_exponente, bits_mantisa\n",
        "\n",
        "\n",
        "def evaluar_expresion(expresion):\n",
        "    try:\n",
        "        resultado = eval(expresion)\n",
        "        return resultado\n",
        "    except Exception as e:\n",
        "        print(\"Error en la operación:\", e)\n",
        "        return None\n",
        "\n",
        "print(\"Calculadora binaria de 32 bits (binario con punto flotante)\")\n",
        "print(\"Usa solo operaciones simples: +, -, *, /\")\n",
        "\n",
        "expresion = input(\"Ingresa la operación: \")\n",
        "resultado = evaluar_expresion(expresion)\n",
        "\n",
        "if resultado is not None:\n",
        "    print(f\"\\n Resultado decimal: {resultado}\")\n",
        "\n",
        "    if isinstance(resultado, int):\n",
        "        binario = int_a_bin(resultado)\n",
        "        print(f\" Binario de 32 bits (entero): {binario}\")\n",
        "\n",
        "    elif isinstance(resultado, float):\n",
        "        binario, signo, exponente, mantisa = float_a_bin(resultado)\n",
        "        print(f\" Resultado binario con punto flotante (32 bits): {binario}\")\n",
        "        print(f\" Signo: {signo}\")\n",
        "        print(f\" Exponente: {exponente}\")\n",
        "        print(f\" Mantisa: {mantisa}\")\n",
        "\n",
        "# debemos tener en uenta que si el signo es 1, quiere decir que es negativo y si es 0 es positivo\n",
        "\n",
        "else:\n",
        "    print(\"No se pudo calcular el resultado.\")"
      ]
    }
  ]
}