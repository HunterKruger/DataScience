{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pandas\n",
      "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/39/90/c2cac34acd673ceddf5beaa1a8375dc32e0c2399fa09363917148adeefdb/pandas-0.25.2-cp37-cp37m-macosx_10_9_x86_64.whl (10.2MB)\n",
      "\u001b[K     |████████████████████████████████| 10.2MB 2.2MB/s eta 0:00:01\n",
      "\u001b[?25hCollecting numpy>=1.13.3\n",
      "  Using cached https://files.pythonhosted.org/packages/ea/f4/acaa005b20777fc56a1dc0cae228ab2cb5a7f09a7e7fcb6d4619ce24a1b7/numpy-1.17.3-cp37-cp37m-macosx_10_9_x86_64.whl\n",
      "Collecting pytz>=2017.2\n",
      "  Using cached https://files.pythonhosted.org/packages/e7/f9/f0b53f88060247251bf481fa6ea62cd0d25bf1b11a87888e53ce5b7c8ad2/pytz-2019.3-py2.py3-none-any.whl\n",
      "Requirement already satisfied: python-dateutil>=2.6.1 in /usr/local/lib/python3.7/site-packages (from pandas) (2.8.0)\n",
      "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/site-packages (from python-dateutil>=2.6.1->pandas) (1.12.0)\n",
      "Installing collected packages: numpy, pytz, pandas\n",
      "Successfully installed numpy-1.17.3 pandas-0.25.2 pytz-2019.3\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd.",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-4ea23bb9f38d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mfileXLSX\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_excel\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'pokemon_data.xlsx'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/usr/local/lib/python3.7/site-packages/pandas/util/_decorators.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    206\u001b[0m                 \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    207\u001b[0m                     \u001b[0mkwargs\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mnew_arg_name\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnew_arg_value\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 208\u001b[0;31m             \u001b[0;32mreturn\u001b[0m \u001b[0mfunc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    209\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    210\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.7/site-packages/pandas/io/excel/_base.py\u001b[0m in \u001b[0;36mread_excel\u001b[0;34m(io, sheet_name, header, names, index_col, usecols, squeeze, dtype, engine, converters, true_values, false_values, skiprows, nrows, na_values, keep_default_na, verbose, parse_dates, date_parser, thousands, comment, skip_footer, skipfooter, convert_float, mangle_dupe_cols, **kwds)\u001b[0m\n\u001b[1;32m    308\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    309\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mio\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mExcelFile\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 310\u001b[0;31m         \u001b[0mio\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mExcelFile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mio\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mengine\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    311\u001b[0m     \u001b[0;32melif\u001b[0m \u001b[0mengine\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0mengine\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mio\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    312\u001b[0m         raise ValueError(\n",
      "\u001b[0;32m/usr/local/lib/python3.7/site-packages/pandas/io/excel/_base.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, io, engine)\u001b[0m\n\u001b[1;32m    817\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_io\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_stringify_path\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mio\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    818\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 819\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_reader\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engines\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mengine\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_io\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    820\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    821\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__fspath__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.7/site-packages/pandas/io/excel/_xlrd.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, filepath_or_buffer)\u001b[0m\n\u001b[1;32m     18\u001b[0m         \"\"\"\n\u001b[1;32m     19\u001b[0m         \u001b[0merr_msg\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"Install xlrd >= 1.0.0 for Excel support\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 20\u001b[0;31m         \u001b[0mimport_optional_dependency\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"xlrd\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mextra\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0merr_msg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     21\u001b[0m         \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     22\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/usr/local/lib/python3.7/site-packages/pandas/compat/_optional.py\u001b[0m in \u001b[0;36mimport_optional_dependency\u001b[0;34m(name, extra, raise_on_missing, on_version)\u001b[0m\n\u001b[1;32m     91\u001b[0m     \u001b[0;32mexcept\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     92\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mraise_on_missing\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 93\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mImportError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mextra\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mextra\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     94\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     95\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mImportError\u001b[0m: Missing optional dependency 'xlrd'. Install xlrd >= 1.0.0 for Excel support Use pip or conda to install xlrd."
     ]
    }
   ],
   "source": [
    "fileXLSX = pd.read_excel('pokemon_data.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting xlrd\n",
      "  Using cached https://files.pythonhosted.org/packages/b0/16/63576a1a001752e34bf8ea62e367997530dc553b689356b9879339cf45a4/xlrd-1.2.0-py2.py3-none-any.whl\n",
      "Installing collected packages: xlrd\n",
      "Successfully installed xlrd-1.2.0\n"
     ]
    }
   ],
   "source": [
    "!pip install xlrd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "fileXLSX = pd.read_excel('pokemon_data.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>#</th>\n",
       "      <th>Name</th>\n",
       "      <th>Type 1</th>\n",
       "      <th>Type 2</th>\n",
       "      <th>HP</th>\n",
       "      <th>Attack</th>\n",
       "      <th>Defense</th>\n",
       "      <th>Sp. Atk</th>\n",
       "      <th>Sp. Def</th>\n",
       "      <th>Speed</th>\n",
       "      <th>Generation</th>\n",
       "      <th>Legendary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Bulbasaur</td>\n",
       "      <td>Grass</td>\n",
       "      <td>Poison</td>\n",
       "      <td>45</td>\n",
       "      <td>49</td>\n",
       "      <td>49</td>\n",
       "      <td>65</td>\n",
       "      <td>65</td>\n",
       "      <td>45</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Ivysaur</td>\n",
       "      <td>Grass</td>\n",
       "      <td>Poison</td>\n",
       "      <td>60</td>\n",
       "      <td>62</td>\n",
       "      <td>63</td>\n",
       "      <td>80</td>\n",
       "      <td>80</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Venusaur</td>\n",
       "      <td>Grass</td>\n",
       "      <td>Poison</td>\n",
       "      <td>80</td>\n",
       "      <td>82</td>\n",
       "      <td>83</td>\n",
       "      <td>100</td>\n",
       "      <td>100</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>VenusaurMega Venusaur</td>\n",
       "      <td>Grass</td>\n",
       "      <td>Poison</td>\n",
       "      <td>80</td>\n",
       "      <td>100</td>\n",
       "      <td>123</td>\n",
       "      <td>122</td>\n",
       "      <td>120</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Charmander</td>\n",
       "      <td>Fire</td>\n",
       "      <td>NaN</td>\n",
       "      <td>39</td>\n",
       "      <td>52</td>\n",
       "      <td>43</td>\n",
       "      <td>60</td>\n",
       "      <td>50</td>\n",
       "      <td>65</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   #                   Name Type 1  Type 2  HP  Attack  Defense  Sp. Atk  \\\n",
       "0  1              Bulbasaur  Grass  Poison  45      49       49       65   \n",
       "1  2                Ivysaur  Grass  Poison  60      62       63       80   \n",
       "2  3               Venusaur  Grass  Poison  80      82       83      100   \n",
       "3  3  VenusaurMega Venusaur  Grass  Poison  80     100      123      122   \n",
       "4  4             Charmander   Fire     NaN  39      52       43       60   \n",
       "\n",
       "   Sp. Def  Speed  Generation  Legendary  \n",
       "0       65     45           1      False  \n",
       "1       80     60           1      False  \n",
       "2      100     80           1      False  \n",
       "3      120     80           1      False  \n",
       "4       50     65           1      False  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fileXLSX.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'a' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-10-3f786850e387>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0ma\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'a' is not defined"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
