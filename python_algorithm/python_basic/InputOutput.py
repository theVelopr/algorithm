{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f814c13c",
   "metadata": {},
   "source": [
    "## Print String"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d543392",
   "metadata": {},
   "source": [
    "### Exercise 1. Print \"Hello World\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2e77dfcd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "print (\"Hello World\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d8ba824e",
   "metadata": {},
   "source": [
    "### Exercise 2. Print \"Mary's cosmetics\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cceaf6a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mary' cosmetics\n"
     ]
    }
   ],
   "source": [
    "print (\"Mary\\' cosmetics\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf13523f",
   "metadata": {},
   "source": [
    "### Exercise 3. Format Operator"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1824d2c",
   "metadata": {},
   "source": [
    "print 3.141592 rounding up to two decimal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "edf42fe5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.14\n"
     ]
    }
   ],
   "source": [
    "number = 3.141592\n",
    "print (\"%.2f\" % number)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "740e036d",
   "metadata": {},
   "source": [
    "### Exercise 4. Input\n",
    "Print adding two numbers.\n",
    "\n",
    "this is the same with Scanner in Java"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "805c9276",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "a = input()\n",
    "b = input()\n",
    "\n",
    "print (int(a) + int(b))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "186f7e6a",
   "metadata": {},
   "source": [
    "### Exercise 5. For loop\n",
    "Code a program that repeats 4 times."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c6b324fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "What's up\n",
      "What's up\n",
      "What's up\n",
      "What's up\n"
     ]
    }
   ],
   "source": [
    "count = input()\n",
    "for i in range (int(count)):\n",
    "    print(\"What's up\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a4f0d22",
   "metadata": {},
   "source": [
    "### Exercise 6. Casting\n",
    "Change String \"720\" to Integer & Integer 100 to String \"100\".\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "5cb6de2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "720\n",
      "100\n"
     ]
    }
   ],
   "source": [
    "string1 = \"720\"\n",
    "integer1 = 100\n",
    "\n",
    "print (int(string1))\n",
    "print (str(integer1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec903e5e",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
