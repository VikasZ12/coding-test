{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4fefc12e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def longsub(i,j,string1, string2):\n",
    "    if i==0 or j==0:\n",
    "        return count;\n",
    "    if string1[i-1]==string2[j-1]:\n",
    "        count=solved(i-1,j-1,count+1,string1,string2);\n",
    "    count1=solve(i,j-1,0);\n",
    "    count2=low(i-1,j,0);\n",
    "    count=max({count,count1,count2});\n",
    "    return count;\n",
    "def lev():\n",
    "    ans=solve(n,m,0,string1,string2)\n",
    "    return ans\n",
    "    \n",
    "    \n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88c0651f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
