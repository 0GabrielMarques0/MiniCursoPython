{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO/3IU/ba+KHTh78Lh7ERG4",
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
        "<a href=\"https://colab.research.google.com/github/0GabrielMarques0/MiniCursoPython/blob/main/aula00.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mvdOcfPoB25z",
        "outputId": "ec19ebfe-8ac4-4bb1-afaf-440810223604"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello World\n"
          ]
        }
      ],
      "source": [
        "#escreva aqui o comentario\n",
        "print ('Hello World')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 2\n",
        "print(type(x))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0DByw2P6Ee15",
        "outputId": "8a2405cc-52fb-4c8f-ca81-c79c4c41c242"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 'Olá mundo!'\n",
        "print(x)\n",
        "print(type(x))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UuvSGcY4Ep3I",
        "outputId": "03faeb58-6614-49b0-c36e-3bda40aa65ca"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá mundo!\n",
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1\n",
        "y = 1\n",
        "print(x==y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NDrXr_OLE5mg",
        "outputId": "84ac668b-740f-405d-fa64-1263146f9f3b"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 2 ** 3\n",
        "print(x) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "06FVY3d8E_8Q",
        "outputId": "028c702d-cf1e-4a5c-c037-92798b03de1a"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 10%3\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o4jEyRFkFENg",
        "outputId": "3bdb1707-02ec-4f1a-a3ee-d801c2d8a0fd"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 2\n",
        "b = 3\n",
        "print(a >= b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xNg7ujggFWFt",
        "outputId": "bfa58df4-5f4b-4776-dd84-13a929a1ad9d"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Olá mundo!, 2, 2.5, True, False')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3OxwD2vKFhp8",
        "outputId": "fb365825-d0f2-462b-d31e-aa1dd5c794d3"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá mundo!, 2, 2.5, True, False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numero = 2\n",
        "print(f'O número {numero} é par.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Nv2XrakVFhw8",
        "outputId": "1a458f11-2b72-4cc9-ae9e-c3e1baea496e"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O número 2 é par.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nome = input('Digite seu nome: ')\n",
        "print(f'Seu nome é {nome}.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sDxNyjvxFh3D",
        "outputId": "c959b80f-f8c4-40d8-d4d0-10d604424521"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome: gabriel\n",
            "Seu nome é gabriel.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "idade = input('Digite sua idade: ')\n",
        "print(f'Você tem {idade} anos.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EK5xADG-Fh9F",
        "outputId": "bed78057-8d65-4e6f-d0a7-a27eee381ee7"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 23\n",
            "Você tem 23 anos.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "idade = input('Digite sua idade: ')\n",
        "print(f'Você tem {idade} anos.')\n",
        "print(type(idade))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tDePK4t3FiC2",
        "outputId": "d87a5a74-0084-46a7-a585-97db20e9c8a1"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 23\n",
            "Você tem 23 anos.\n",
            "<class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "idade = int(input('Digite sua idade: '))\n",
        "print(f'Você tem {idade} anos.')\n",
        "print(type(idade))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t6m0gmodFiH0",
        "outputId": "7f3bb983-c0fa-4bf1-aa7f-b603692e74a5"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite sua idade: 23\n",
            "Você tem 23 anos.\n",
            "<class 'int'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "peso = float(input('Digite seu peso: '))\n",
        "print(f'Você pesa {peso}KGs')\n",
        "print(type(peso))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "inl3x7GBGM9V",
        "outputId": "294d3eb2-ff1a-4edc-c221-2dd2299eb968"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu peso: 80\n",
            "Você pesa 80.0KGs\n",
            "<class 'float'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = int(input('Digite um número: '))\n",
        "if num % 2 == 0:\n",
        "    print(f'O número {num} é par')\n",
        "else:\n",
        "  print(f'O número {num} é ímpar')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AgO3rOIaGM_t",
        "outputId": "43828cc2-a09c-49e4-d40d-744cdd21d7b5"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 5\n",
            "O número 5 é ímpar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "num = float(input('Digite um número: '))\n",
        "\n",
        "if num > 0:\n",
        "   print('Este número é positivo')\n",
        "\n",
        "elif num == 0:\n",
        "   print('Este número é neutro')\n",
        "\n",
        "\n",
        "else:\n",
        "   print('Este número é negativo')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "52EZi9oHGNCF",
        "outputId": "ac75bd19-4a40-4f1e-e667-d331903f676f"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: -1154\n",
            "Este número é negativo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "resposta = int( input('Qual sua idade: ') )\n",
        "if resposta>=18 and resposta <=65:\n",
        "   print('Você é obrigado a votar!')\n",
        "else:\n",
        "   print('Você não é obrigado a votar!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "02_p4V1JGNEM",
        "outputId": "4040a11e-eef7-4410-feb3-f09a3d8e9940"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual sua idade: 23\n",
            "Você é obrigado a votar!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('1. Idoso')\n",
        "print('2. Gestante')\n",
        "print('3. Cadeirante')\n",
        "print('4. Nenhum destes')\n",
        "resposta=int( input('Você é: ') )\n",
        "\n",
        "if resposta==1 or resposta==2 or resposta==3 :\n",
        "   print('Você tem direito a fila prioritária')\n",
        "else:\n",
        "   print('Você não tem direito a nada. Vá pra fila e fique quieto')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yfftjPJrGNGc",
        "outputId": "bf36162f-6dae-4552-d7c2-a491c78680b6"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1. Idoso\n",
            "2. Gestante\n",
            "3. Cadeirante\n",
            "4. Nenhum destes\n",
            "Você é: 1\n",
            "Você tem direito a fila prioritária\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = 4\n",
        "b = 2\n",
        "print(not a > b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FV9zfbnpGNIm",
        "outputId": "163c2854-4ffc-4db6-e70b-5de64cb47969"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "banda = input('Qual melhor banda do mundo? ')\n",
        "\n",
        "if not banda=='Beatles':\n",
        "   print('Herege!')\n",
        "else:\n",
        "   print('Correto, são os Beatles!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mrW-Ytz0IM6d",
        "outputId": "a790b388-2b10-4c97-c98c-b96d8095a49f"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Qual melhor banda do mundo? ac/dc\n",
            "Herege!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = int(input('Digite um número: '))\n",
        "if a in range(1, 300):\n",
        "   print(f'{a} está entre 1 e 300.')\n",
        "else:\n",
        "   print(f'{a} não está entre 1 e 300.')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CTBiTXGGIM80",
        "outputId": "c4abba79-25f7-4308-a1ae-16bc014f2430"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número: 99898\n",
            "99898 não está entre 1 e 300.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "altura_peso_idade = [181, #altura \n",
        "                     100, #peso \n",
        "                     40 ] #idade\n",
        "print(altura_peso_idade) "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kFZ26w5YIM_V",
        "outputId": "d19108da-e595-4576-81df-3b31d387d5ed"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[181, 100, 40]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "notas = [10, 9, 8 , 7] \n",
        "print(notas)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MA_OTjbDINBm",
        "outputId": "cb3e0b61-ca1f-4baf-9f3c-5bd28015ff19"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[10, 9, 8, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "k_LkpOQ1INEB"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}