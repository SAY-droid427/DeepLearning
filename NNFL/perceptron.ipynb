{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled3.ipynb",
      "provenance": [],
      "collapsed_sections": []
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
      "metadata": {
        "id": "Va3L2kNLW9ba"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "r9prsG5fZpeg"
      },
      "source": [
        "# Implementation of AND gate"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MhShXxCLtkh8"
      },
      "source": [
        "def perceptron(Input, Expected_Output):\n",
        "  \n",
        "  # Initial Weights \n",
        "  Weights = np.array([0, 0, 0])\n",
        "\n",
        "  # Training \n",
        "  history, Weights, threshold = training(Input, Expected_Output, Weights)\n",
        "  \n",
        "  # Printing Output\n",
        "  Final_Output=printoutput(Input, Weights, threshold)\n",
        "\n",
        "  return history, Final_Output"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "abHIfO4uhTf2"
      },
      "source": [
        "def training(Input, Expected_Output, Weights):\n",
        "\n",
        "  num_iters = 10\n",
        "  threshold = 2\n",
        "  history = []\n",
        "\n",
        "  for _ in range(num_iters):\n",
        "    history.append(0)\n",
        "    for i in range(len(Input)):\n",
        "\n",
        "      ## Calculate the output and error.\n",
        "      ## Output = 1 if weighted sum crosses threshold, else 0.\n",
        "      ## Error = Expected Ouput - Calculated Output\n",
        "      sum = np.dot(Input[i],Weights)\n",
        "      Calculated_Output = sum > threshold    \n",
        "\n",
        "      ## Add error to the history and update weights.\n",
        "      Error = Expected_Output[i] - Calculated_Output\n",
        "      history[-1] +=abs(Error)\n",
        "      Weights = Weights + Error*Input[i]\n",
        "      \n",
        "  \n",
        "  return history, Weights, threshold"
      ],
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RYcawCBuj3aT"
      },
      "source": [
        "def printoutput(Input, Weights, threshold):\n",
        "\n",
        "    Final_Output = np.zeros(len(Input))\n",
        "    for i in range(len(Input)):\n",
        "      sum = np.dot(Input[i], Weights)\n",
        "      Calculated_Output = sum > threshold\n",
        "      Final_Output[i] = Calculated_Output\n",
        "\n",
        "    print(Final_Output == Expected_Output)\n",
        "\n",
        "    return Final_Output"
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 329
        },
        "id": "SOQscH-VZ7mW",
        "outputId": "e8d36249-7be0-4527-8243-ed774cb14f36"
      },
      "source": [
        "# Calling the function perceptron\n",
        "Input = np.array([[1,0,0],\n",
        "                 [1,0,1],\n",
        "                 [1,1,0],\n",
        "                 [1,1,1]])\n",
        "\n",
        "Expected_Output = np.array([0,0,0,1])\n",
        "history, Final_Output = perceptron(Input, Expected_Output)\n",
        "\n",
        "print(Final_Output)\n",
        "plt.plot(history)\n",
        "plt.title(\"Iterations vs Error\")\n",
        "plt.xlabel(\"Iteration no.\")\n",
        "plt.ylabel(\"Error\")\n",
        "plt.show()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[ True  True  True  True]\n",
            "[0. 0. 0. 1.]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "A7TCMVYca4Z2"
      },
      "source": [
        "# Implementation of XOR gate"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_eIlqF81bzAc"
      },
      "source": [
        "def perceptron(Input, Expected_Output):\n",
        "  \n",
        "  # Initial Weights \n",
        "  Weights = np.array([0, 0, 0])\n",
        "\n",
        "  # Training \n",
        "  history, Weights, threshold = training(Input, Expected_Output, Weights)\n",
        "  \n",
        "  # Printing Output\n",
        "  Final_Output=printoutput(Input, Weights, threshold)\n",
        "\n",
        "  return history, Final_Output"
      ],
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5vzUkAWFb4t5"
      },
      "source": [
        "def training(Input, Expected_Output, Weights):\n",
        "\n",
        "  ## Number of times to iterate through all training samples and update the weights. Enter values of num_iters, threshold and initialise history\n",
        "  # Write Code Here\n",
        "  num_iters = 10\n",
        "  threshold = 1\n",
        "  history = []\n",
        "  # Code Ends Here\n",
        "\n",
        "  for _ in range(num_iters):\n",
        "    history.append(0)\n",
        "    for i in range(len(Input)):\n",
        "\n",
        "      ## Calculate the output and error.\n",
        "      ## Output = 1 if weighted sum crosses threshold, else 0.\n",
        "      ## Error = Expected Ouput - Calculated Output\n",
        "      # Write Code Here\n",
        "      sum = np.dot(Input[i],Weights)\n",
        "      Calculated_Output = sum > threshold    \n",
        "      # Code Ends Here\n",
        "\n",
        "      ## Add error to the history and update weights.\n",
        "      Error = Expected_Output[i] - Calculated_Output\n",
        "      history[-1] +=abs(Error)\n",
        "      Weights = Weights + Error*Input[i]\n",
        "      # Write Code Here\n",
        "    \n",
        "      # Code Ends Here\n",
        "  \n",
        "  return history, Weights, threshold"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fMU0cjnHlPlv",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 346
        },
        "outputId": "a4bd00e9-a9cb-4a21-9311-792ab7efb6ac"
      },
      "source": [
        "# All possible binary input for a 2 input gates with X0 representing Bias\n",
        "Input = np.array([[1,0,0],\n",
        "                  [1,0,1],\n",
        "                  [1,1,0],\n",
        "                  [1,1,1]])\n",
        "\n",
        "# Corresponding Output\n",
        "Expected_Output = np.array([0,1,1,0])\n",
        "\n",
        "history, Final_Output = perceptron(Input, Expected_Output)\n",
        "print(Final_Output)\n",
        "print(Final_Output == Expected_Output)\n",
        "plt.plot(history)\n",
        "plt.title(\"Iterations vs Error\")\n",
        "plt.xlabel(\"Iteration no.\")\n",
        "plt.ylabel(\"Error\")\n",
        "plt.show()"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[False  True False  True]\n",
            "[1. 1. 0. 0.]\n",
            "[False  True False  True]\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    }
  ]
}