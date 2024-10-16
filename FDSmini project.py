{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d99050cb",
   "metadata": {
    "papermill": {
     "duration": 0.027908,
     "end_time": "2024-01-10T11:35:01.263163",
     "exception": false,
     "start_time": "2024-01-10T11:35:01.235255",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Importing Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "125d601e",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "papermill": {
     "duration": 2.943021,
     "end_time": "2024-01-10T11:35:04.231236",
     "exception": false,
     "start_time": "2024-01-10T11:35:01.288215",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn import metrics, preprocessing\n",
    "from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.neural_network import MLPClassifier\n",
    "from sklearn.svm import SVC\n",
    "from kmodes.kmodes import KModes\n",
    "from sklearn.metrics import classification_report\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e9b583e2",
   "metadata": {
    "papermill": {
     "duration": 0.026856,
     "end_time": "2024-01-10T11:35:04.284214",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.257358",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Reading the data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "30a87f1b",
   "metadata": {
    "_cell_guid": "b1076dfc-b9ad-4769-8c92-a6c4dae69d19",
    "_uuid": "8f2839f25d086af736a60e9eeb907d3b93b6e0e5",
    "papermill": {
     "duration": 0.234422,
     "end_time": "2024-01-10T11:35:04.545000",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.310578",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>18393</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>20228</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>18857</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>17623</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>17474</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id    age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  \\\n",
       "0   0  18393       2     168    62.0    110     80            1     1      0   \n",
       "1   1  20228       1     156    85.0    140     90            3     1      0   \n",
       "2   2  18857       1     165    64.0    130     70            3     1      0   \n",
       "3   3  17623       2     169    82.0    150    100            1     1      0   \n",
       "4   4  17474       1     156    56.0    100     60            1     1      0   \n",
       "\n",
       "   alco  active  cardio  \n",
       "0     0       1       0  \n",
       "1     0       1       1  \n",
       "2     0       0       1  \n",
       "3     0       1       1  \n",
       "4     0       0       0  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\rohil\\Desktop\\archive\\cardio_train.csv\", sep=';')\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f8fe590d",
   "metadata": {
    "papermill": {
     "duration": 0.059846,
     "end_time": "2024-01-10T11:35:04.630123",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.570277",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 70000 entries, 0 to 69999\n",
      "Data columns (total 13 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   id           70000 non-null  int64  \n",
      " 1   age          70000 non-null  int64  \n",
      " 2   gender       70000 non-null  int64  \n",
      " 3   height       70000 non-null  int64  \n",
      " 4   weight       70000 non-null  float64\n",
      " 5   ap_hi        70000 non-null  int64  \n",
      " 6   ap_lo        70000 non-null  int64  \n",
      " 7   cholesterol  70000 non-null  int64  \n",
      " 8   gluc         70000 non-null  int64  \n",
      " 9   smoke        70000 non-null  int64  \n",
      " 10  alco         70000 non-null  int64  \n",
      " 11  active       70000 non-null  int64  \n",
      " 12  cardio       70000 non-null  int64  \n",
      "dtypes: float64(1), int64(12)\n",
      "memory usage: 6.9 MB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "50bf0743",
   "metadata": {
    "papermill": {
     "duration": 0.024101,
     "end_time": "2024-01-10T11:35:04.680210",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.656109",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Checking for missing values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "853462a4",
   "metadata": {
    "papermill": {
     "duration": 0.036451,
     "end_time": "2024-01-10T11:35:04.741184",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.704733",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id             0\n",
      "age            0\n",
      "gender         0\n",
      "height         0\n",
      "weight         0\n",
      "ap_hi          0\n",
      "ap_lo          0\n",
      "cholesterol    0\n",
      "gluc           0\n",
      "smoke          0\n",
      "alco           0\n",
      "active         0\n",
      "cardio         0\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(df.isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3fcb6872",
   "metadata": {
    "papermill": {
     "duration": 0.043662,
     "end_time": "2024-01-10T11:35:04.874441",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.830779",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "#drop id\n",
    "df = df.drop('id', axis=1)\n",
    "\n",
    "# print(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e997bfd0",
   "metadata": {
    "papermill": {
     "duration": 0.025932,
     "end_time": "2024-01-10T11:35:04.925798",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.899866",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "550bffe6",
   "metadata": {
    "papermill": {
     "duration": 0.024867,
     "end_time": "2024-01-10T11:35:04.976350",
     "exception": false,
     "start_time": "2024-01-10T11:35:04.951483",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **Removing Outliers:**\n",
    "\n",
    "It is important to remove outliers to improve the performance of our prediction models. We have removed outliers that fall outside the range of 2.5% to 97.5% in all instances of ap_hi, ap_lo, weight, and height features. This process has decreased the entries in the data set from 70,000 to 60,142 records. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f80aca91",
   "metadata": {
    "papermill": {
     "duration": 0.095584,
     "end_time": "2024-01-10T11:35:05.097849",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.002265",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "60142"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(df[(df['height'] > df['height'].quantile(0.975)) | (df['height'] < df['height'].quantile(0.025))].index,inplace=True)\n",
    "df.drop(df[(df['weight'] > df['weight'].quantile(0.975)) | (df['weight'] < df['weight'].quantile(0.025))].index,inplace=True)\n",
    "df.drop(df[(df['ap_hi'] > df['ap_hi'].quantile(0.975)) | (df['ap_hi'] < df['ap_hi'].quantile(0.025))].index,inplace=True)\n",
    "df.drop(df[(df['ap_lo'] > df['ap_lo'].quantile(0.975)) | (df['ap_lo'] < df['ap_lo'].quantile(0.025))].index,inplace=True)\n",
    "len(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20ed4a53",
   "metadata": {
    "papermill": {
     "duration": 0.026348,
     "end_time": "2024-01-10T11:35:05.150141",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.123793",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "How many cases where diastolic pressure is higher than systolic?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "087fdca1",
   "metadata": {
    "papermill": {
     "duration": 0.040083,
     "end_time": "2024-01-10T11:35:05.215772",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.175689",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df['ap_lo']> df['ap_hi']].shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "aeb9c7bb",
   "metadata": {
    "papermill": {
     "duration": 0.108551,
     "end_time": "2024-01-10T11:35:05.352472",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.243921",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>19468.719979</td>\n",
       "      <td>1.347311</td>\n",
       "      <td>164.554854</td>\n",
       "      <td>73.426805</td>\n",
       "      <td>125.770526</td>\n",
       "      <td>81.046307</td>\n",
       "      <td>1.350953</td>\n",
       "      <td>1.220229</td>\n",
       "      <td>0.085631</td>\n",
       "      <td>0.051877</td>\n",
       "      <td>0.803648</td>\n",
       "      <td>0.488228</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2460.510296</td>\n",
       "      <td>0.476120</td>\n",
       "      <td>6.830174</td>\n",
       "      <td>11.614806</td>\n",
       "      <td>13.761847</td>\n",
       "      <td>8.239157</td>\n",
       "      <td>0.670076</td>\n",
       "      <td>0.567607</td>\n",
       "      <td>0.279820</td>\n",
       "      <td>0.221781</td>\n",
       "      <td>0.397241</td>\n",
       "      <td>0.499866</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>10798.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>150.000000</td>\n",
       "      <td>52.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>60.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>17677.250000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>160.000000</td>\n",
       "      <td>65.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>19705.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>165.000000</td>\n",
       "      <td>72.000000</td>\n",
       "      <td>120.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>21321.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>169.000000</td>\n",
       "      <td>80.000000</td>\n",
       "      <td>135.000000</td>\n",
       "      <td>90.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>23713.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>180.000000</td>\n",
       "      <td>106.000000</td>\n",
       "      <td>163.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        gender        height        weight         ap_hi  \\\n",
       "count  60142.000000  60142.000000  60142.000000  60142.000000  60142.000000   \n",
       "mean   19468.719979      1.347311    164.554854     73.426805    125.770526   \n",
       "std     2460.510296      0.476120      6.830174     11.614806     13.761847   \n",
       "min    10798.000000      1.000000    150.000000     52.000000    100.000000   \n",
       "25%    17677.250000      1.000000    160.000000     65.000000    120.000000   \n",
       "50%    19705.000000      1.000000    165.000000     72.000000    120.000000   \n",
       "75%    21321.000000      2.000000    169.000000     80.000000    135.000000   \n",
       "max    23713.000000      2.000000    180.000000    106.000000    163.000000   \n",
       "\n",
       "              ap_lo   cholesterol          gluc         smoke          alco  \\\n",
       "count  60142.000000  60142.000000  60142.000000  60142.000000  60142.000000   \n",
       "mean      81.046307      1.350953      1.220229      0.085631      0.051877   \n",
       "std        8.239157      0.670076      0.567607      0.279820      0.221781   \n",
       "min       60.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "25%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "50%       80.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "75%       90.000000      1.000000      1.000000      0.000000      0.000000   \n",
       "max      100.000000      3.000000      3.000000      1.000000      1.000000   \n",
       "\n",
       "             active        cardio  \n",
       "count  60142.000000  60142.000000  \n",
       "mean       0.803648      0.488228  \n",
       "std        0.397241      0.499866  \n",
       "min        0.000000      0.000000  \n",
       "25%        1.000000      0.000000  \n",
       "50%        1.000000      0.000000  \n",
       "75%        1.000000      1.000000  \n",
       "max        1.000000      1.000000  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#after removing outliers\n",
    "df.describe()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bed3c896",
   "metadata": {
    "papermill": {
     "duration": 0.026181,
     "end_time": "2024-01-10T11:35:05.406245",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.380064",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Transformation:\n",
    "Converting age from days to years"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "769ab176",
   "metadata": {
    "papermill": {
     "duration": 0.046285,
     "end_time": "2024-01-10T11:35:05.480238",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.433953",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  alco  \\\n",
      "0   50       2     168    62.0    110     80            1     1      0     0   \n",
      "1   55       1     156    85.0    140     90            3     1      0     0   \n",
      "2   52       1     165    64.0    130     70            3     1      0     0   \n",
      "3   48       2     169    82.0    150    100            1     1      0     0   \n",
      "4   48       1     156    56.0    100     60            1     1      0     0   \n",
      "\n",
      "   active  cardio  \n",
      "0       1       0  \n",
      "1       1       1  \n",
      "2       0       1  \n",
      "3       1       1  \n",
      "4       0       0  \n"
     ]
    }
   ],
   "source": [
    "df['age'] = (df['age'] / 365).round().astype('int')\n",
    "\n",
    "print(df.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de73ed2c",
   "metadata": {
    "papermill": {
     "duration": 0.027663,
     "end_time": "2024-01-10T11:35:05.535865",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.508202",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b1d2dd7",
   "metadata": {
    "papermill": {
     "duration": 0.026851,
     "end_time": "2024-01-10T11:35:05.589900",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.563049",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Categorizing features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "9d5e0702",
   "metadata": {
    "papermill": {
     "duration": 0.056497,
     "end_time": "2024-01-10T11:35:05.674648",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.618151",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>age_group</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>48</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  alco  \\\n",
       "0   50       2     168    62.0    110     80            1     1      0     0   \n",
       "1   55       1     156    85.0    140     90            3     1      0     0   \n",
       "2   52       1     165    64.0    130     70            3     1      0     0   \n",
       "3   48       2     169    82.0    150    100            1     1      0     0   \n",
       "4   48       1     156    56.0    100     60            1     1      0     0   \n",
       "\n",
       "   active  cardio age_group  \n",
       "0       1       0         3  \n",
       "1       1       1         4  \n",
       "2       0       1         4  \n",
       "3       1       1         3  \n",
       "4       0       0         3  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# # Define the bin edges and labels\n",
    "age_edges = [30, 35, 40, 45, 50, 55, 60, 65]\n",
    "age_labels = [0, 1, 2, 3, 4, 5, 6]\n",
    "\n",
    "#  bin in  5 years span\n",
    "df['age_group'] = pd.cut(df['age'], bins=7, labels=range(7), include_lowest=True,right=True)\n",
    "df.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c82e22e3",
   "metadata": {
    "papermill": {
     "duration": 0.026973,
     "end_time": "2024-01-10T11:35:05.729659",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.702686",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Attribute Combination**\n",
    "\n",
    "It is important to combine some attributes into more meaningful ones. For example, using Body Mass Index (BMI) instead of the features weight and height individually, is more useful. Therefore, we have added Body Mass Index (BMI) and Mean Arterial Pressure (MAP) to the data. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a912a03b",
   "metadata": {
    "papermill": {
     "duration": 0.055899,
     "end_time": "2024-01-10T11:35:05.815164",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.759265",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16 46\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "bmi\n",
       "1    0.461325\n",
       "2    0.330202\n",
       "3    0.133068\n",
       "0    0.038193\n",
       "4    0.033554\n",
       "5    0.003658\n",
       "Name: proportion, dtype: float64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['bmi'] = df['weight']/((df['height']/100)**2)\n",
    "df.head()\n",
    "\n",
    "bmiMin = int(df['bmi'].min())\n",
    "bmiMax = int(df['bmi'].max())\n",
    "\n",
    "print(bmiMin, bmiMax)\n",
    "\n",
    "df['bmi'] = pd.cut(df['bmi'], bins=6, labels=range(6), right=True, include_lowest=True)\n",
    "\n",
    "df.head()\n",
    "\n",
    "\n",
    "df[\"bmi\"].value_counts(normalize=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6ca17806",
   "metadata": {
    "papermill": {
     "duration": 0.07207,
     "end_time": "2024-01-10T11:35:05.920221",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.848151",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "73 121\n"
     ]
    },
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
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>height</th>\n",
       "      <th>weight</th>\n",
       "      <th>ap_hi</th>\n",
       "      <th>ap_lo</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>age_group</th>\n",
       "      <th>bmi</th>\n",
       "      <th>map</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>50</td>\n",
       "      <td>2</td>\n",
       "      <td>168</td>\n",
       "      <td>62.0</td>\n",
       "      <td>110</td>\n",
       "      <td>80</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>55</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>85.0</td>\n",
       "      <td>140</td>\n",
       "      <td>90</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>52</td>\n",
       "      <td>1</td>\n",
       "      <td>165</td>\n",
       "      <td>64.0</td>\n",
       "      <td>130</td>\n",
       "      <td>70</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>48</td>\n",
       "      <td>2</td>\n",
       "      <td>169</td>\n",
       "      <td>82.0</td>\n",
       "      <td>150</td>\n",
       "      <td>100</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>48</td>\n",
       "      <td>1</td>\n",
       "      <td>156</td>\n",
       "      <td>56.0</td>\n",
       "      <td>100</td>\n",
       "      <td>60</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  gender  height  weight  ap_hi  ap_lo  cholesterol  gluc  smoke  alco  \\\n",
       "0   50       2     168    62.0    110     80            1     1      0     0   \n",
       "1   55       1     156    85.0    140     90            3     1      0     0   \n",
       "2   52       1     165    64.0    130     70            3     1      0     0   \n",
       "3   48       2     169    82.0    150    100            1     1      0     0   \n",
       "4   48       1     156    56.0    100     60            1     1      0     0   \n",
       "\n",
       "   active  cardio age_group bmi map  \n",
       "0       1       0         3   1   2  \n",
       "1       1       1         4   3   4  \n",
       "2       0       1         4   1   2  \n",
       "3       1       1         3   2   5  \n",
       "4       0       0         3   1   0  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['map'] = ((2* df['ap_lo']) + df['ap_hi']) / 3\n",
    "\n",
    "mapMin = int(df['map'].min())\n",
    "mapMax = int(df['map'].max())\n",
    "\n",
    "print(mapMin, mapMax)\n",
    "\n",
    "df['map'] = pd.cut(df['map'], bins=6, labels=range(6), right=True, include_lowest=True)\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "604d11eb",
   "metadata": {
    "papermill": {
     "duration": 0.031667,
     "end_time": "2024-01-10T11:35:05.979574",
     "exception": false,
     "start_time": "2024-01-10T11:35:05.947907",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Print Null rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f531b547",
   "metadata": {
    "papermill": {
     "duration": 0.055764,
     "end_time": "2024-01-10T11:35:06.077731",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.021967",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rows with null values:\n",
      "Empty DataFrame\n",
      "Columns: [age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio, age_group, bmi, map]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "null_rows = df[df.isnull().any(axis=1)]\n",
    "print(\"Rows with null values:\")\n",
    "print(null_rows)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6081441a",
   "metadata": {
    "papermill": {
     "duration": 0.032483,
     "end_time": "2024-01-10T11:35:06.151727",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.119244",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Drop features**\n",
    "We only need categorical data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8012e42c",
   "metadata": {
    "papermill": {
     "duration": 0.0531,
     "end_time": "2024-01-10T11:35:06.232753",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.179653",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>gender</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>age_group</th>\n",
       "      <th>bmi</th>\n",
       "      <th>map</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   gender  cholesterol  gluc  smoke  alco  active  cardio age_group bmi map\n",
       "0       2            1     1      0     0       1       0         3   1   2\n",
       "1       1            3     1      0     0       1       1         4   3   4\n",
       "2       1            3     1      0     0       0       1         4   1   2\n",
       "3       2            1     1      0     0       1       1         3   2   5\n",
       "4       1            1     1      0     0       0       0         3   1   0"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_og=df\n",
    "\n",
    "df=df.drop(['height','weight','ap_hi','ap_lo','age'],axis=1)\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c8e6a6c2",
   "metadata": {
    "papermill": {
     "duration": 0.032231,
     "end_time": "2024-01-10T11:35:06.302087",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.269856",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Label Encoder**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d6314af2",
   "metadata": {
    "papermill": {
     "duration": 0.119999,
     "end_time": "2024-01-10T11:35:06.454564",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.334565",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>gender</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>age_group</th>\n",
       "      <th>bmi</th>\n",
       "      <th>map</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "      <td>60142.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>0.347311</td>\n",
       "      <td>0.350953</td>\n",
       "      <td>0.220229</td>\n",
       "      <td>0.085631</td>\n",
       "      <td>0.051877</td>\n",
       "      <td>0.803648</td>\n",
       "      <td>0.488228</td>\n",
       "      <td>4.042233</td>\n",
       "      <td>1.673440</td>\n",
       "      <td>2.359449</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>0.476120</td>\n",
       "      <td>0.670076</td>\n",
       "      <td>0.567607</td>\n",
       "      <td>0.279820</td>\n",
       "      <td>0.221781</td>\n",
       "      <td>0.397241</td>\n",
       "      <td>0.499866</td>\n",
       "      <td>1.377070</td>\n",
       "      <td>0.898707</td>\n",
       "      <td>1.186906</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>3.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>5.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             gender   cholesterol          gluc         smoke          alco  \\\n",
       "count  60142.000000  60142.000000  60142.000000  60142.000000  60142.000000   \n",
       "mean       0.347311      0.350953      0.220229      0.085631      0.051877   \n",
       "std        0.476120      0.670076      0.567607      0.279820      0.221781   \n",
       "min        0.000000      0.000000      0.000000      0.000000      0.000000   \n",
       "25%        0.000000      0.000000      0.000000      0.000000      0.000000   \n",
       "50%        0.000000      0.000000      0.000000      0.000000      0.000000   \n",
       "75%        1.000000      0.000000      0.000000      0.000000      0.000000   \n",
       "max        1.000000      2.000000      2.000000      1.000000      1.000000   \n",
       "\n",
       "             active        cardio     age_group           bmi           map  \n",
       "count  60142.000000  60142.000000  60142.000000  60142.000000  60142.000000  \n",
       "mean       0.803648      0.488228      4.042233      1.673440      2.359449  \n",
       "std        0.397241      0.499866      1.377070      0.898707      1.186906  \n",
       "min        0.000000      0.000000      0.000000      0.000000      0.000000  \n",
       "25%        1.000000      0.000000      3.000000      1.000000      2.000000  \n",
       "50%        1.000000      0.000000      4.000000      2.000000      2.000000  \n",
       "75%        1.000000      1.000000      5.000000      2.000000      3.000000  \n",
       "max        1.000000      1.000000      6.000000      5.000000      5.000000  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "le = preprocessing.LabelEncoder()\n",
    "df = df.apply(le.fit_transform)\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f21e65f0",
   "metadata": {
    "papermill": {
     "duration": 0.030827,
     "end_time": "2024-01-10T11:35:06.514627",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.483800",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **Clustering**\n",
    "\n",
    "Clustering is used in machine learning to find similarities between data by grouping.  The most common technique for clustering is K-means. However, it is not effective for categorical data. K-means uses a Euclidean distance measure differences between data points. For our data, we have used **K-modes** which is the appropriate clustering algorithm for categorical data because it uses mode-based distance between the categories, so it is more suitable for categorical data. To find the optimal number of clusters, we have utilized the **elbow curve method**. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ae432ba0",
   "metadata": {
    "papermill": {
     "duration": 931.735397,
     "end_time": "2024-01-10T11:50:38.279435",
     "exception": false,
     "start_time": "2024-01-10T11:35:06.544038",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "cost = []\n",
    "num_clusters = range(1,6) # 1 to 5\n",
    "for i in list(num_clusters):\n",
    "    kmode = KModes(n_clusters=i, init = \"Huang\", n_init = 5, verbose=0,random_state=1)\n",
    "    kmode.fit_predict(df)\n",
    "    cost.append(kmode.cost_)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a322587f",
   "metadata": {
    "papermill": {
     "duration": 0.031566,
     "end_time": "2024-01-10T11:50:38.342155",
     "exception": false,
     "start_time": "2024-01-10T11:50:38.310589",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Clusters graph**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "727e3d9d",
   "metadata": {
    "papermill": {
     "duration": 0.419582,
     "end_time": "2024-01-10T11:50:38.792409",
     "exception": false,
     "start_time": "2024-01-10T11:50:38.372827",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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SGhoqIiIhIaGCgDZvXu3WjNv3jwBIJcuXVKnjR07Vvz8/J7YT3JystjY2MhXX32V6/zHe1q9erU4OTkZ1GzZskWy/2+3QoUKEhwcnOvycnt/TEyMWFpays2bNw2md+/eXQIDA9X3AZDIyEh1/u3btwWA7N2794nrSURPh4cCichktWjRwuB11apVkZCQUORluLm5wd7eHnXr1jWYVpBlRkVFITU1Fd27dy/U5+dnypQpGD16NHx9fTF//nxcunQp3/pTp04hMzMTDRo0gIODg/rYt2+fwXutra0N1tvFxQUjR46En58fevfujaVLlyI2NtZo60FEjzBYEZHJsrKyMnit0+mQlZUFCwvlf10ios5LT09/4jJ0Ol2ey3wSOzu7AvcNABYWFgb95dbj3LlzcebMGfj7+yMkJARNmjTBli1b8lzmvXv3YGlpifDwcERGRqqPqKgoLF261KDXxw/zrV69GmFhYWjfvj1++OEHNGjQAIcPHy7UOhHRkzFYEZHZqVKlCgAY7HUp7vGj6tevDzs7O+zZs6dA9VWqVMHdu3dx//59dVpuPTZo0ABvvfUW/vjjD/Tv3x+rV68GoOx1yszMNKht1aoVMjMzkZCQgHr16hk83N3dn9hTq1atEBgYiEOHDqFZs2ZYt25dgdaFiAqOwYqIzI6dnR3+9a9/Yf78+YiKisK+ffvw3nvvFetn2traYsaMGZg+fTq+/fZbXLp0CYcPH8Z//vOfXOu9vb1hb2+Pd955B5cuXcK6desQHByszk9JScGECROwd+9exMTE4ODBgzh69CgaN24MAKhduzbu3buHPXv24NatW3jw4AEaNGiAYcOGYfjw4fjpp59w5coV/PXXX5g3bx5+//33PHu/cuUKAgMDERYWhpiYGPzxxx+4cOGC+llEZDwMVkRklr755htkZGTAy8sLAQEB+Oijj4r9M2fNmoWpU6di9uzZaNy4MQYNGpTn+VkuLi747rvvsG3bNjRv3hzr169Xh0wAAEtLS9y+fRvDhw9HgwYNMHDgQPTq1Qvvv/8+AKB9+/YYN24cBg0ahCpVqmDhwoUAlEN6w4cPx9SpU9GwYUP069cPR48eRc2aNfPs297eHufOncNLL72EBg0aYMyYMRg/fjzGjh1rvB8OEQEAdPL4SQBEREREVCTcY0VERERkJAxWREQArl27ZjCEweOPa9euad0iEZkBHgokIgKQkZGBq1ev5jm/du3aKFeON6sgovwxWBEREREZCQ8FEhERERkJgxURERGRkTBYERERERkJgxURERGRkTBYERERERkJgxURERGRkTBYERERERkJgxURERGRkfw/YBXsUAprc6sAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(num_clusters, cost, 'bo-')\n",
    "plt.xlabel('num_clusters')\n",
    "plt.ylabel('Cost')\n",
    "plt.title('Elbow Method For Optimal Number of Clusters')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53f296ef",
   "metadata": {
    "papermill": {
     "duration": 0.032587,
     "end_time": "2024-01-10T11:50:38.855481",
     "exception": false,
     "start_time": "2024-01-10T11:50:38.822894",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Building KModes model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "0e651789",
   "metadata": {
    "papermill": {
     "duration": 123.813292,
     "end_time": "2024-01-10T11:52:42.698076",
     "exception": false,
     "start_time": "2024-01-10T11:50:38.884784",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1, 0, 1, ..., 1, 0, 1], dtype=uint16)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "km = KModes(n_clusters=2, init = \"Huang\", n_init = 5,random_state=1)\n",
    "clusters = km.fit_predict(df)\n",
    "clusters"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1418994",
   "metadata": {
    "papermill": {
     "duration": 0.030745,
     "end_time": "2024-01-10T11:52:42.759043",
     "exception": false,
     "start_time": "2024-01-10T11:52:42.728298",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Adding clusters column in DF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4007adb7",
   "metadata": {
    "papermill": {
     "duration": 0.049854,
     "end_time": "2024-01-10T11:52:42.837540",
     "exception": false,
     "start_time": "2024-01-10T11:52:42.787686",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>clusters</th>\n",
       "      <th>gender</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>alco</th>\n",
       "      <th>active</th>\n",
       "      <th>cardio</th>\n",
       "      <th>age_group</th>\n",
       "      <th>bmi</th>\n",
       "      <th>map</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   clusters  gender  cholesterol  gluc  smoke  alco  active  cardio  \\\n",
       "0         1       1            0     0      0     0       1       0   \n",
       "1         0       0            2     0      0     0       1       1   \n",
       "2         1       0            2     0      0     0       0       1   \n",
       "3         0       1            0     0      0     0       1       1   \n",
       "4         1       0            0     0      0     0       0       0   \n",
       "\n",
       "   age_group  bmi  map  \n",
       "0          3    1    2  \n",
       "1          4    3    4  \n",
       "2          4    1    2  \n",
       "3          3    2    5  \n",
       "4          3    1    0  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.insert(0,\"clusters\",clusters,True)\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b01d9e41",
   "metadata": {
    "papermill": {
     "duration": 0.0291,
     "end_time": "2024-01-10T11:52:42.895542",
     "exception": false,
     "start_time": "2024-01-10T11:52:42.866442",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **Correlation Matrix**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "1d84235f",
   "metadata": {
    "papermill": {
     "duration": 0.857708,
     "end_time": "2024-01-10T11:52:43.781917",
     "exception": false,
     "start_time": "2024-01-10T11:52:42.924209",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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T09P+vfvX2q6diGEEI8GaTESQoiH5OPjw4oVK3j55ZcJDAykX79+1K5dm/z8fPbv38+qVasYMGAAAHXr1qV///789NNP2u5rhw4dYunSpfTo0YO2bdv+63wolUoWLFhA586dqVWrFgMHDsTd3Z0bN26we/dubGxs2Lhxo960zZs3x97env79+/Pee++hUChYtmyZ3i5sDRs25Ndff2XUqFE0btwYKysrnn/+eb3b/fLLL+ncuTMhISEMHjxYO123ra3tfbu4/VdKpZIJEyY8MK5bt25MnTqVgQMH0rx5c06dOsXy5cvx9vbWifPx8cHOzo558+ZhbW2NpaUlTZs2ve8YMH3CwsL4/vvvCQ0N1U4fvnjxYtq0acPEiRP54osv/tH2hBBCVIDKnRRPCCEeP+fPn9e8+eabGk9PT42pqanG2tpa06JFC83cuXN1prsuKCjQTJkyRePl5aUxMTHRVK9eXTN+/HidGI2meLrurl27lnqfO9N1r1q1Sm8+jh8/runVq5fG0dFRo1KpNB4eHpqXXnpJs2vXLm2Mvum6//77b02zZs005ubmGjc3N82HH36onVp69+7d2rjMzExN3759NXZ2dhpAO3W3vum6NRqNZufOnZoWLVpozM3NNTY2Nprnn39ec+bMGZ2YO9N1JyQk6KzXl0997p6uuyxlTdc9evRojaurq8bc3FzTokULTXh4uN5ptn///XdNUFCQxtjYWKecrVu31tSqVUvve969nfT0dI2Hh4emQYMGmoKCAp24kSNHapRKpSY8PPy+ZRBCCFHxFBrNPxjpKoQQQgghhBBPIBljJIQQQgghhHjqScVICCGEEEII8dSTipEQQgghhBDiqScVIyGEEEIIIYRB/fXXXzz//PO4ubmhUChYv379A9Ps2bOHBg0aoFKp8PX1ZcmSJQbNo1SMhBBCCCGEEAaVlZVF3bp1+e677x4qPjo6mq5du9K2bVsiIiJ4//33GTJkCNu2bTNYHmVWOiGEEEIIIUSFUSgUrFu3jh49epQZM3bsWDZt2sTp06e161555RVSU1PZunWrQfIlLUZCCCGEEEKIfywvL4/09HSdJS8vr1y2HR4eTocOHXTWdezYkfDw8HLZvj7GBtuyEEIIIYQQwqD691hWae/tVe8SU6ZM0VkXGhrK5MmT//O2b926RZUqVXTWValShfT0dHJycjA3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",
      "text/plain": [
       "<Figure size 1000x800 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set up figure\n",
    "plt.figure(figsize=(10, 8))\n",
    "\n",
    "# Draw correlation matrix\n",
    "sns.heatmap(df.corr(), annot=True, cmap='Spectral', fmt=\".2f\", linewidths=.5)\n",
    "\n",
    "# Show the figure\n",
    "plt.title('Correlation Matrix')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c43278a6",
   "metadata": {
    "papermill": {
     "duration": 0.031951,
     "end_time": "2024-01-10T11:52:43.847625",
     "exception": false,
     "start_time": "2024-01-10T11:52:43.815674",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "'gender' has a correlation of 0 to our target 'cardio', and 'smoke' has a correlation of '0.01'.\n",
    "We will remove those features to increase performance."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "90226722",
   "metadata": {
    "papermill": {
     "duration": 0.030873,
     "end_time": "2024-01-10T11:52:43.910539",
     "exception": false,
     "start_time": "2024-01-10T11:52:43.879666",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Distribution of cardio in clusters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "815f92c5",
   "metadata": {
    "papermill": {
     "duration": 0.356969,
     "end_time": "2024-01-10T11:52:44.298425",
     "exception": false,
     "start_time": "2024-01-10T11:52:43.941456",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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JIfLG7KzsxUREaHQ0FC99957Wr58uSZMmKDq1atr4MCB13yOnnrqKQUHB2vs2LHavHmzPv30U/n5+endd9+94mP27NmjXbt2qU+fPipbtuw1t3E94uLi1KNHD7Vt29Ze086dO7V27VoNHjxYrVq10osvvqgPPvhAr732murUqSNJ9n8L8hxevHhRERERatGihd577z2VKlXK8uuzWHB2akPBXWukyRhjvL29zX333We/f/lI08SJE40kc+TIkSuu4+eff853JMGYPz/BSDLTp0/Pd1l+I0133XWXwyemb775xkhy+KRoZaTpWrVd/ilq/vz5RpJ56623HPo98cQTxmazmb1799rbJBk3NzeHtl9++cVIMlOmTMmzrUtNmjTJSDJffvmlve38+fMmLCzMlClTxmHfq1atajp27HjV9RljzNChQ40ks2XLlmv2Ncbk+aRvjDEJCQlGkvniiy/sbbmvoRYtWjh8Wj5//rzx8/MzISEhJisry97+8ccfG0nXHGkKCQkxfn5+5tixY/a2X375xbi4uJhnn33W3tajRw/j5+fnsO3Dhw8bFxcXM2bMmKvuz7///W8jyaxZs8be5u3tbQYNGnTF43Lx4kUTHBxsqlatak6cOOGw7NIRiesZabreY38l1xppMsaYxx57zEgy6enpxpi8I01btmwxksycOXOuuI79+/cbV1dX8/bbbzu0b9261ZQoUcKhPb99HTt2rLHZbObAgQPGmD9Hgq5V96lTp4yPj4/p37+/Q3tKSorx9vbO0365QYMGOYwgRUdHm1atWhk/Pz8zbdo0Y4wxx44dMzabzeHnzOXP55EjR/I8n5f2leTwujTGmPvuu880btzYoe3ydeT+3O3Tp49Dv8cff9xUqFDhqvu2YMECI8lMnDjxqv1yXc9I0+DBg42Xl9dVX4+5I8SXji4ZU7DnMPdYvvrqqw59rbw+iwu+PXebKlOmzFW/RZf7iXHBggWFvmja3d1dvXv3ttz/2WefdfjE9MQTT6hSpUr6/vvvC7V9q77//nu5urraP43meumll2SM0eLFix3aw8PDVb16dfv9Bg0ayMvLS7/99ts1txMQEKAePXrY20qWLKkXX3xRp0+f1urVqwtce0ZGhiRZ/qR56YjdhQsXdOzYMdWoUUM+Pj7avHlznv79+/eXq6ur/f7GjRuVlpamAQMGOFyb1qtXr2t+2jt8+LASExPVq1cvlS9f3t7eoEEDPfTQQw7Pc7du3ZSWlubwbaW5c+cqJydH3bp1y3d/zp07p6NHj+qBBx6QJIf98fHx0U8//aRDhw7lW9uWLVuUlJSkIUOG2F/7uYpqKo7rPfbXI/cr8Vd6z+c+d0uXLtWZM2fy7fPdd98pJydHTz31lI4ePWq/BQQEqGbNmlq5cqW976X7mpmZqaNHj6pZs2YyxmjLli32Pm5ublq1apVOnDiR7zbj4uJ08uRJ9ejRw2Gbrq6uCg0Nddhmflq2bKnU1FTt3r1b0p8jSq1atVLLli31ww8/SPpz9MkYc8WRJqsGDBiQZ9vX+plwtcceO3bM/v7OT0Hf+9fDx8dHmZmZVx2tvJLCPIeXj85ZeX0WF4Sm29Tp06ev+mbr1q2bmjdvrn79+snf31/du3fXN998U6AAdddddxXoou+aNWs63LfZbKpRo8YN/wrrgQMHFBgYmOd45A4tHzhwwKG9SpUqedZRrly5K/7gv3Q7NWvWlIuL49vqStuxwsvLS9KVfxle7uzZs4qJiVFQUJDc3d1VsWJF+fr66uTJk0pPT8/TPzg4OM8+SHmfq5IlS+ruu+++6rZzH3vPPffkWVanTh0dPXrUfhqqXbt28vb21uzZs+19Zs+erZCQENWqVcvedvz4cQ0ePFj+/v7y9PSUr6+vveZL92fcuHHatm2bgoKC1LRpU40aNcrhF9q+ffskyX7a70a43mN/PU6fPi3pyr9gg4ODFR0drU8//VQVK1ZURESEPvzwQ4e69uzZI2OMatasKV9fX4fbzp07lZaWZu+bnJxsD8dlypSRr6+v/VRr7jrd3d317rvvavHixfL391erVq00btw4paSkOGxTktq0aZNnm8uWLXPYZn5yg9APP/ygzMxMbdmyRS1btlSrVq3soemHH36Ql5eX/SL5wvDw8MhzCt3Kz4Rcl/9MKVeunCRd9fEFfe9fj+eff161atVS+/btVblyZfXp00dLliyx9NiCPoclSpTI801fK6/P4oJrmm5Dv//+u9LT01WjRo0r9vH09NSaNWu0cuVKLVq0SEuWLNHs2bPVpk0bLVu2zNIn4IJch2TVlT71Z2dnF9mn8mu50naMMTdl+5eqXbu2JGnr1q2Wpn144YUXNGPGDA0ZMkRhYWHy9vaWzWZT9+7d8w3EN+I5tMLd3V2dO3fWvHnz9NFHHyk1NVVr167VO++849Dvqaee0rp16zRs2DCFhISoTJkyysnJUbt27Rz256mnnlLLli01b948LVu2TOPHj9e7776r7777Tu3bt7dcl81my/d5zs7OvuZjnXnst23bJj8/P/sv2vxMmDBBvXr10oIFC7Rs2TK9+OKLGjt2rNavX6/KlSsrJydHNptNixcvzvc9kDualZ2drYceekjHjx/X8OHDVbt2bZUuXVp//PGHevXq5bCvQ4YMUadOnTR//nwtXbpUb775psaOHasVK1bovvvus/edOXOmAgIC8mzzWt/4DQwMVHBwsNasWaNq1arJGKOwsDD5+vpq8ODBOnDggH744Qc1a9Ysz4eZgrjenz2F+Zly6Xu/sKy+nv38/JSYmKilS5dq8eLFWrx4sWbMmKFnn31Wn3/++VW3UdDn0N3dPd/n4lqvz+KC0HQbmjlzpiQpIiLiqv1cXFzUtm1btW3bVu+//77eeecdvf7661q5cqXCw8OLfAbx3E8kuYwx2rt3r8MFl+XKldPJkyfzPPbAgQMOIx0Fqa1q1apavny5Tp065fBJfNeuXfblRaFq1ar69ddflZOT4/BD4Xq20759e7m6uurLL7+0dDH43LlzFRkZqQkTJtjbzp07l+8xzU9ujXv27FGbNm3s7RcuXFBSUtJVP63nPjb3VMmldu3apYoVKzp8tbhbt276/PPPFR8fr507d8oY43Bq7sSJE4qPj9fo0aMVExNjb7/8dZSrUqVKev755/X8888rLS1NjRo10ttvv6327dvbT7du27ZN4eHhV9yHcuXK5XvKxcoo4fUe+8JKSEjQvn378kxHkJ/69eurfv36euONN7Ru3To1b95c06dP11tvvaXq1avLGKPg4GCH0b7Lbd26Vf/73//0+eef69lnn7W3X+nUTvXq1fXSSy/ppZde0p49exQSEqIJEyboyy+/tD8vfn5+V31erqZly5Zas2aNgoODFRISorJly6phw4by9vbWkiVLtHnzZvscTFdys/5aQkHUqlVL99xzjxYsWKDJkydbnpX8UgV5Pbu5ualTp07q1KmTcnJy9Pzzz+uf//yn3nzzTdWoUeOKx6gonsNcV3t9FhecnrvNrFixQv/4xz8UHBysnj17XrHf8ePH87TljmRkZWVJkv0XXFH90P/iiy8chprnzp2rw4cPO4wEVK9eXevXr9f58+ftbQsXLtTBgwcd1lWQ2jp06KDs7GxNnTrVoX3ixImy2WwFGom41nZSUlIcTjldvHhRU6ZMUZkyZfJ8U8yKoKAg9e/fX8uWLdOUKVPyLM/JydGECRP0+++/S/rzE+3lnyynTJliaaREkpo0aSJfX19Nnz7d4TmIjY295rGuVKmSQkJC9Pnnnzv03bZtm5YtW6YOHTo49A8PD1f58uU1e/ZszZ49W02bNnU4ZZX76fzy/Zk0aZLD/ezs7DzD+H5+fgoMDLS/lhs1aqTg4GBNmjQpz35cuv7q1atr165dOnLkiL3tl19+sX+r9Gqu99gXxoEDB9SrVy+5ublp2LBhV+yXkZGhixcvOrTVr19fLi4u9mPUpUsXubq6avTo0Xn2wxijY8eOScr/eTHGaPLkyQ6POXPmjM6dO+fQVr16dZUtW9a+zYiICHl5eemdd97Jd76hS5+HK2nZsqX279+v2bNn20/Xubi4qFmzZnr//fd14cKFa17PlPvNxhsdcAtq9OjROnbsmPr165fn+ZP+nEh44cKFV3y81ddz7nOby8XFxf5h9lq/D4riObTy+iwuGGm6hS1evFi7du3SxYsXlZqaqhUrViguLk5Vq1bVf/7zn6tOtDZmzBitWbNGHTt2VNWqVZWWlqaPPvpIlStXVosWLST9+Ybz8fHR9OnTVbZsWZUuXVqhoaGFvhajfPnyatGihXr37q3U1FRNmjRJNWrUcJgWoV+/fpo7d67atWunp556Svv27XP4RJqrILV16tRJDz74oF5//XXt379fDRs21LJly7RgwQINGTIkz7oL67nnntM///lP9erVS5s2bVK1atU0d+5crV27VpMmTSr0BZ0TJkzQvn379OKLL+q7777TI488onLlyik5OVlz5szRrl277LNBP/LII5o5c6a8vb1Vt25dJSQkaPny5VedKuFSJUuW1FtvvaW///3vatOmjbp166akpCTNmDHjmtc0SdL48ePVvn17hYWFqW/fvvYpB7y9vfP8Ta6SJUuqS5cu+vrrr5WZman33nvPYbmXl5f9OpgLFy7orrvu0rJly5SUlOTQ79SpU6pcubKeeOIJNWzYUGXKlNHy5cv1888/20d9XFxcNG3aNHXq1EkhISHq3bu3KlWqpF27dmn79u1aunSpJKlPnz56//33FRERob59+yotLU3Tp0/Xvffee9WLdqXrP/bXsnnzZn355ZfKycnRyZMn9fPPP+vbb7+VzWbTzJkzHUZsL7dixQpFRUXpySefVK1atXTx4kXNnDlTrq6u6tq1q6Q/31NvvfWWRowYof3796tz584qW7askpKSNG/ePD333HN6+eWXVbt2bVWvXl0vv/yy/vjjD3l5eenbb7/Nc33O//73P7Vt21ZPPfWU6tatqxIlSmjevHlKTU21v169vLw0bdo0PfPMM2rUqJG6d+8uX19fJScna9GiRWrevHmeDzuXyw1Eu3fvdji926pVKy1evFju7u66//77r7oOT09P1a1bV7Nnz1atWrVUvnx51atX74ZeA2dFt27dtHXrVr399tvasmWLevToYZ8RfMmSJYqPj9esWbOu+Hirr+d+/frp+PHjatOmjSpXrqwDBw5oypQpCgkJsV+TGRISIldXV7377rtKT0+Xu7u72rRpIz8/v+t+Dq28PouNm/tlPRSFyycay5007qGHHjKTJ0/OdyK0y6cciI+PN4899pgJDAw0bm5uJjAw0PTo0cP873//c3jcggULTN26dU2JEiXyndwyP1eacuDf//63GTFihPHz8zOenp6mY8eO9q8nX2rChAnmrrvuMu7u7qZ58+Zm48aN+X519kq15ff18FOnTpmhQ4eawMBAU7JkSVOzZs2rTm55uStNhXC51NRU07t3b1OxYkXj5uZm6tevn++0CFanHMh18eJF8+mnn5qWLVsab29vU7JkSVO1alXTu3dvh+kITpw4Yd9+mTJlTEREhNm1a1ee+q81bcVHH31kn1CySZMmBZrccvny5aZ58+bG09PTeHl5mU6dOjlMbnmpuLg4I8nYbDZz8ODBPMt///138/jjjxsfHx/j7e1tnnzySXPo0CGHr3ZnZWWZYcOGmYYNG5qyZcua0qVLm4YNG5qPPvooz/p+/PFH89BDD9n7NWjQIM9UEl9++aW5++67jZubmwkJCTFLly61NOVAUR37y10++WKJEiVM+fLlTWhoqBkxYkS+76HLpxz47bffTJ8+fUz16tXtE28++OCDZvny5Xke++2335oWLVqY0qVLm9KlS5vatWubQYMGmd27d9v77Nixw4SHh5syZcqYihUrmv79+9un5sh9PRw9etQMGjTI1K5d25QuXdp4e3ub0NBQ88033+Rbb0REhPH29jYeHh6m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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x='clusters', hue='cardio', data=df)\n",
    "plt.title('Distribution of Cardiovascular Disease within Clusters')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "274f86fc",
   "metadata": {
    "papermill": {
     "duration": 0.03417,
     "end_time": "2024-01-10T11:52:44.365956",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.331786",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "\n",
    "\n",
    "# **Split Data**\n",
    "\n",
    "Training set: 80%\n",
    "\n",
    "Test set: 20%\n",
    "\n",
    "According to the correlation table, gender has 0 correlation with our target. Moreover, ‘alco’ has 0.01 correlation. Therefore, we dropped those two features and saw an increase in the performance of our models. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "75abe610",
   "metadata": {
    "papermill": {
     "duration": 0.055236,
     "end_time": "2024-01-10T11:52:44.456803",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.401567",
     "status": "completed"
    },
    "tags": []
   },
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
       "      <th>clusters</th>\n",
       "      <th>cholesterol</th>\n",
       "      <th>gluc</th>\n",
       "      <th>smoke</th>\n",
       "      <th>active</th>\n",
       "      <th>age_group</th>\n",
       "      <th>bmi</th>\n",
       "      <th>map</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   clusters  cholesterol  gluc  smoke  active  age_group  bmi  map\n",
       "0         1            0     0      0       1          3    1    2\n",
       "1         0            2     0      0       1          4    3    4\n",
       "2         1            2     0      0       0          4    1    2\n",
       "3         0            0     0      0       1          3    2    5\n",
       "4         1            0     0      0       0          3    1    0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x = df.drop(['cardio','gender','alco'], axis=1)\n",
    "y = df['cardio']\n",
    "\n",
    "x.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "7d144e65",
   "metadata": {
    "papermill": {
     "duration": 0.054268,
     "end_time": "2024-01-10T11:52:44.544974",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.490706",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "04c73650",
   "metadata": {
    "papermill": {
     "duration": 0.053914,
     "end_time": "2024-01-10T11:52:44.634472",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.580558",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Index: 48113 entries, 20655 to 38356\n",
      "Data columns (total 8 columns):\n",
      " #   Column       Non-Null Count  Dtype \n",
      "---  ------       --------------  ----- \n",
      " 0   clusters     48113 non-null  uint16\n",
      " 1   cholesterol  48113 non-null  int64 \n",
      " 2   gluc         48113 non-null  int64 \n",
      " 3   smoke        48113 non-null  int64 \n",
      " 4   active       48113 non-null  int64 \n",
      " 5   age_group    48113 non-null  int64 \n",
      " 6   bmi          48113 non-null  int64 \n",
      " 7   map          48113 non-null  int64 \n",
      "dtypes: int64(7), uint16(1)\n",
      "memory usage: 3.0 MB\n"
     ]
    }
   ],
   "source": [
    "x_train.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e90276dc",
   "metadata": {
    "papermill": {
     "duration": 0.034675,
     "end_time": "2024-01-10T11:52:44.701261",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.666586",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **Random Forest**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "696bbdb6",
   "metadata": {
    "papermill": {
     "duration": 0.032602,
     "end_time": "2024-01-10T11:52:44.768268",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.735666",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Without CV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "6eddab32",
   "metadata": {
    "papermill": {
     "duration": 2.825652,
     "end_time": "2024-01-10T11:52:47.628158",
     "exception": false,
     "start_time": "2024-01-10T11:52:44.802506",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy without CV: 87.49\n"
     ]
    }
   ],
   "source": [
    "# build the model\n",
    "rfModel = RandomForestClassifier(random_state=1)\n",
    "\n",
    "# Fit the model\n",
    "rfModel.fit(x_train, y_train)\n",
    "\n",
    "# Make predictions\n",
    "rf_pred = rfModel.predict(x_test)\n",
    "\n",
    "# accuracy\n",
    "rf_accuracy = metrics.accuracy_score(y_test, rf_pred)*100\n",
    "print(f\"Accuracy without CV: {rf_accuracy:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "182f3b02",
   "metadata": {
    "papermill": {
     "duration": 0.031842,
     "end_time": "2024-01-10T11:52:47.693304",
     "exception": false,
     "start_time": "2024-01-10T11:52:47.661462",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "GridsearchCV\n",
    "cross-validation technique that finds the optimal parameter values for a model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "18fe3960",
   "metadata": {
    "papermill": {
     "duration": 0.035865,
     "end_time": "2024-01-10T11:52:47.762929",
     "exception": false,
     "start_time": "2024-01-10T11:52:47.727064",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Original *param_grid* processed on faster machine:\n",
    "> param_grid = {\n",
    ">      'n_estimators': [100, 200, 300, 500],\n",
    ">      'max_depth': [None, 10, 20, 30],\n",
    ">      'min_samples_split': [2, 5, 10, 20],\n",
    ">      'min_samples_leaf': [1, 2, 4, 8],\n",
    ">      'max_features': ['sqrt', 'log2', None],\n",
    ">  }\n",
    "> \n",
    "\n",
    "> Best Parameters: {'max_depth': 10, 'max_features': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "53f5e429",
   "metadata": {
    "papermill": {
     "duration": 13.466178,
     "end_time": "2024-01-10T11:53:01.262037",
     "exception": false,
     "start_time": "2024-01-10T11:52:47.795859",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-1 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: black;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-1 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-1 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-1 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: block;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-1 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-1 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-1 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-1 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-1 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 1ex;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-1 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-1 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GridSearchCV(cv=5, estimator=RandomForestClassifier(random_state=1), n_jobs=-1,\n",
       "             param_grid={&#x27;max_depth&#x27;: [10], &#x27;max_features&#x27;: [None],\n",
       "                         &#x27;min_samples_leaf&#x27;: [1], &#x27;min_samples_split&#x27;: [10],\n",
       "                         &#x27;n_estimators&#x27;: [100]},\n",
       "             scoring=&#x27;accuracy&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" ><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;&nbsp;GridSearchCV<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.GridSearchCV.html\">?<span>Documentation for GridSearchCV</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></label><div class=\"sk-toggleable__content fitted\"><pre>GridSearchCV(cv=5, estimator=RandomForestClassifier(random_state=1), n_jobs=-1,\n",
       "             param_grid={&#x27;max_depth&#x27;: [10], &#x27;max_features&#x27;: [None],\n",
       "                         &#x27;min_samples_leaf&#x27;: [1], &#x27;min_samples_split&#x27;: [10],\n",
       "                         &#x27;n_estimators&#x27;: [100]},\n",
       "             scoring=&#x27;accuracy&#x27;)</pre></div> </div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" ><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">best_estimator_: RandomForestClassifier</label><div class=\"sk-toggleable__content fitted\"><pre>RandomForestClassifier(max_depth=10, max_features=None, min_samples_split=10,\n",
       "                       random_state=1)</pre></div> </div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" ><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;RandomForestClassifier<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.RandomForestClassifier.html\">?<span>Documentation for RandomForestClassifier</span></a></label><div class=\"sk-toggleable__content fitted\"><pre>RandomForestClassifier(max_depth=10, max_features=None, min_samples_split=10,\n",
       "                       random_state=1)</pre></div> </div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "GridSearchCV(cv=5, estimator=RandomForestClassifier(random_state=1), n_jobs=-1,\n",
       "             param_grid={'max_depth': [10], 'max_features': [None],\n",
       "                         'min_samples_leaf': [1], 'min_samples_split': [10],\n",
       "                         'n_estimators': [100]},\n",
       "             scoring='accuracy')"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "param_grid = {\n",
    "    'n_estimators': [100, 200, 300, 500],\n",
    "    'max_depth': [None, 10, 20, 30],\n",
    "    'min_samples_split': [2, 5, 10, 20],\n",
    "    'min_samples_leaf': [1, 2, 4, 8],\n",
    "    'max_features': ['sqrt', 'log2', None],\n",
    "}\n",
    "\n",
    "#  Best parameters for RF\n",
    "rf_best_params = {\n",
    "    'n_estimators': [100],\n",
    "    'max_depth': [10],\n",
    "    'min_samples_split': [10],\n",
    "    'min_samples_leaf': [1],\n",
    "    'max_features': [None],\n",
    "}\n",
    "\n",
    "# Create grid search\n",
    "rf_gridsearch = GridSearchCV(estimator=rfModel,param_grid=rf_best_params, cv=5, scoring='accuracy',n_jobs=-1)\n",
    "\n",
    "# Fit grid search\n",
    "rf_gridsearch.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3fbb551",
   "metadata": {
    "papermill": {
     "duration": 0.03864,
     "end_time": "2024-01-10T11:53:01.336526",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.297886",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Get Best parameters and best estimator for RF from GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "f289227a",
   "metadata": {
    "papermill": {
     "duration": 0.048016,
     "end_time": "2024-01-10T11:53:01.426022",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.378006",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters : {'max_depth': 10, 'max_features': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}\n",
      "Best Estimator  : RandomForestClassifier(max_depth=10, max_features=None, min_samples_split=10,\n",
      "                       random_state=1)\n"
     ]
    }
   ],
   "source": [
    "best_params = rf_gridsearch.best_params_\n",
    "best_estimator = rf_gridsearch.best_estimator_\n",
    "\n",
    "print(f\"Best Parameters : {best_params}\")\n",
    "print(f\"Best Estimator  : {best_estimator}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d06c33d4",
   "metadata": {
    "papermill": {
     "duration": 0.041847,
     "end_time": "2024-01-10T11:53:01.506156",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.464309",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Make prediction using best estimator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "171caddc",
   "metadata": {
    "papermill": {
     "duration": 0.222345,
     "end_time": "2024-01-10T11:53:01.772472",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.550127",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "rf_pred_CV = best_estimator.predict(x_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2fa203c2",
   "metadata": {
    "papermill": {
     "duration": 0.033951,
     "end_time": "2024-01-10T11:53:01.839630",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.805679",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "4b6ad2e5",
   "metadata": {
    "papermill": {
     "duration": 0.048485,
     "end_time": "2024-01-10T11:53:01.932028",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.883543",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Accuracy: 87.82\n"
     ]
    }
   ],
   "source": [
    "rf_accuracy_cv = metrics.accuracy_score(y_test, rf_pred_CV)*100\n",
    "print(f\"Best Accuracy: {rf_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d604d41",
   "metadata": {
    "papermill": {
     "duration": 0.042187,
     "end_time": "2024-01-10T11:53:02.011046",
     "exception": false,
     "start_time": "2024-01-10T11:53:01.968859",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Random Forest** Accuracy Scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "0a676142",
   "metadata": {
    "papermill": {
     "duration": 0.046792,
     "end_time": "2024-01-10T11:53:02.093474",
     "exception": false,
     "start_time": "2024-01-10T11:53:02.046682",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Forest accuracy without CV : 87.49\n",
      "Random Forest accuracy with CV    : 87.82\n"
     ]
    }
   ],
   "source": [
    "print(f\"Random Forest accuracy without CV : {rf_accuracy:.2f}\")\n",
    "print(f\"Random Forest accuracy with CV    : {rf_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a556185b",
   "metadata": {
    "papermill": {
     "duration": 0.034777,
     "end_time": "2024-01-10T11:53:02.165391",
     "exception": false,
     "start_time": "2024-01-10T11:53:02.130614",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Classification Report**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "e2ad83d4",
   "metadata": {
    "papermill": {
     "duration": 0.084059,
     "end_time": "2024-01-10T11:53:02.282533",
     "exception": false,
     "start_time": "2024-01-10T11:53:02.198474",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report for RF with CV:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0     0.8837    0.8804    0.8820      6220\n",
      "           1     0.8724    0.8759    0.8742      5809\n",
      "\n",
      "    accuracy                         0.8782     12029\n",
      "   macro avg     0.8780    0.8781    0.8781     12029\n",
      "weighted avg     0.8782    0.8782    0.8782     12029\n",
      "\n"
     ]
    }
   ],
   "source": [
    "classification_report_str = classification_report(y_test, rf_pred_CV, digits=4)\n",
    "\n",
    "print(\"Classification Report for RF with CV:\\n\", classification_report_str)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d372e20e",
   "metadata": {
    "papermill": {
     "duration": 0.035422,
     "end_time": "2024-01-10T11:53:02.361012",
     "exception": false,
     "start_time": "2024-01-10T11:53:02.325590",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **MLP**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2967b3d3",
   "metadata": {
    "papermill": {
     "duration": 0.034178,
     "end_time": "2024-01-10T11:53:02.429908",
     "exception": false,
     "start_time": "2024-01-10T11:53:02.395730",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Without CV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "159ef28d",
   "metadata": {
    "papermill": {
     "duration": 112.343055,
     "end_time": "2024-01-10T11:54:54.813020",
     "exception": false,
     "start_time": "2024-01-10T11:53:02.469965",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy without CV: 87.28\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rohil\\miniforge3\\lib\\site-packages\\sklearn\\neural_network\\_multilayer_perceptron.py:690: ConvergenceWarning: Stochastic Optimizer: Maximum iterations (200) reached and the optimization hasn't converged yet.\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "# build MLP model\n",
    "mlpModel = MLPClassifier(random_state=1)\n",
    "\n",
    "# Fit the model\n",
    "mlpModel.fit(x_train, y_train)\n",
    "\n",
    "# Make predictions\n",
    "mlp_pred = mlpModel.predict(x_test)\n",
    "\n",
    "# accuracy\n",
    "mlp_accuracy = metrics.accuracy_score(y_test, mlp_pred)*100\n",
    "print(f\"Accuracy without CV: {mlp_accuracy:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f3b6a419",
   "metadata": {
    "papermill": {
     "duration": 361.077456,
     "end_time": "2024-01-10T12:00:55.938465",
     "exception": false,
     "start_time": "2024-01-10T11:54:54.861009",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rohil\\miniforge3\\lib\\site-packages\\sklearn\\neural_network\\_multilayer_perceptron.py:697: UserWarning: Training interrupted by user.\n",
      "  warnings.warn(\"Training interrupted by user.\")\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-2 {\n",
       "  /* Definition of color scheme common for light and dark mode */\n",
       "  --sklearn-color-text: black;\n",
       "  --sklearn-color-line: gray;\n",
       "  /* Definition of color scheme for unfitted estimators */\n",
       "  --sklearn-color-unfitted-level-0: #fff5e6;\n",
       "  --sklearn-color-unfitted-level-1: #f6e4d2;\n",
       "  --sklearn-color-unfitted-level-2: #ffe0b3;\n",
       "  --sklearn-color-unfitted-level-3: chocolate;\n",
       "  /* Definition of color scheme for fitted estimators */\n",
       "  --sklearn-color-fitted-level-0: #f0f8ff;\n",
       "  --sklearn-color-fitted-level-1: #d4ebff;\n",
       "  --sklearn-color-fitted-level-2: #b3dbfd;\n",
       "  --sklearn-color-fitted-level-3: cornflowerblue;\n",
       "\n",
       "  /* Specific color for light theme */\n",
       "  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));\n",
       "  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));\n",
       "  --sklearn-color-icon: #696969;\n",
       "\n",
       "  @media (prefers-color-scheme: dark) {\n",
       "    /* Redefinition of color scheme for dark theme */\n",
       "    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));\n",
       "    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));\n",
       "    --sklearn-color-icon: #878787;\n",
       "  }\n",
       "}\n",
       "\n",
       "#sk-container-id-2 {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 pre {\n",
       "  padding: 0;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 input.sk-hidden--visually {\n",
       "  border: 0;\n",
       "  clip: rect(1px 1px 1px 1px);\n",
       "  clip: rect(1px, 1px, 1px, 1px);\n",
       "  height: 1px;\n",
       "  margin: -1px;\n",
       "  overflow: hidden;\n",
       "  padding: 0;\n",
       "  position: absolute;\n",
       "  width: 1px;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-dashed-wrapped {\n",
       "  border: 1px dashed var(--sklearn-color-line);\n",
       "  margin: 0 0.4em 0.5em 0.4em;\n",
       "  box-sizing: border-box;\n",
       "  padding-bottom: 0.4em;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-container {\n",
       "  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`\n",
       "     but bootstrap.min.css set `[hidden] { display: none !important; }`\n",
       "     so we also need the `!important` here to be able to override the\n",
       "     default hidden behavior on the sphinx rendered scikit-learn.org.\n",
       "     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */\n",
       "  display: inline-block !important;\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-text-repr-fallback {\n",
       "  display: none;\n",
       "}\n",
       "\n",
       "div.sk-parallel-item,\n",
       "div.sk-serial,\n",
       "div.sk-item {\n",
       "  /* draw centered vertical line to link estimators */\n",
       "  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));\n",
       "  background-size: 2px 100%;\n",
       "  background-repeat: no-repeat;\n",
       "  background-position: center center;\n",
       "}\n",
       "\n",
       "/* Parallel-specific style estimator block */\n",
       "\n",
       "#sk-container-id-2 div.sk-parallel-item::after {\n",
       "  content: \"\";\n",
       "  width: 100%;\n",
       "  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);\n",
       "  flex-grow: 1;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-parallel {\n",
       "  display: flex;\n",
       "  align-items: stretch;\n",
       "  justify-content: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  position: relative;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-parallel-item {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-parallel-item:first-child::after {\n",
       "  align-self: flex-end;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-parallel-item:last-child::after {\n",
       "  align-self: flex-start;\n",
       "  width: 50%;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-parallel-item:only-child::after {\n",
       "  width: 0;\n",
       "}\n",
       "\n",
       "/* Serial-specific style estimator block */\n",
       "\n",
       "#sk-container-id-2 div.sk-serial {\n",
       "  display: flex;\n",
       "  flex-direction: column;\n",
       "  align-items: center;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  padding-right: 1em;\n",
       "  padding-left: 1em;\n",
       "}\n",
       "\n",
       "\n",
       "/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is\n",
       "clickable and can be expanded/collapsed.\n",
       "- Pipeline and ColumnTransformer use this feature and define the default style\n",
       "- Estimators will overwrite some part of the style using the `sk-estimator` class\n",
       "*/\n",
       "\n",
       "/* Pipeline and ColumnTransformer style (default) */\n",
       "\n",
       "#sk-container-id-2 div.sk-toggleable {\n",
       "  /* Default theme specific background. It is overwritten whether we have a\n",
       "  specific estimator or a Pipeline/ColumnTransformer */\n",
       "  background-color: var(--sklearn-color-background);\n",
       "}\n",
       "\n",
       "/* Toggleable label */\n",
       "#sk-container-id-2 label.sk-toggleable__label {\n",
       "  cursor: pointer;\n",
       "  display: block;\n",
       "  width: 100%;\n",
       "  margin-bottom: 0;\n",
       "  padding: 0.5em;\n",
       "  box-sizing: border-box;\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 label.sk-toggleable__label-arrow:before {\n",
       "  /* Arrow on the left of the label */\n",
       "  content: \"▸\";\n",
       "  float: left;\n",
       "  margin-right: 0.25em;\n",
       "  color: var(--sklearn-color-icon);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {\n",
       "  color: var(--sklearn-color-text);\n",
       "}\n",
       "\n",
       "/* Toggleable content - dropdown */\n",
       "\n",
       "#sk-container-id-2 div.sk-toggleable__content {\n",
       "  max-height: 0;\n",
       "  max-width: 0;\n",
       "  overflow: hidden;\n",
       "  text-align: left;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-toggleable__content.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-toggleable__content pre {\n",
       "  margin: 0.2em;\n",
       "  border-radius: 0.25em;\n",
       "  color: var(--sklearn-color-text);\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-toggleable__content.fitted pre {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {\n",
       "  /* Expand drop-down */\n",
       "  max-height: 200px;\n",
       "  max-width: 100%;\n",
       "  overflow: auto;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {\n",
       "  content: \"▾\";\n",
       "}\n",
       "\n",
       "/* Pipeline/ColumnTransformer-specific style */\n",
       "\n",
       "#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator-specific style */\n",
       "\n",
       "/* Colorize estimator box */\n",
       "#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-label label.sk-toggleable__label,\n",
       "#sk-container-id-2 div.sk-label label {\n",
       "  /* The background is the default theme color */\n",
       "  color: var(--sklearn-color-text-on-default-background);\n",
       "}\n",
       "\n",
       "/* On hover, darken the color of the background */\n",
       "#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "/* Label box, darken color on hover, fitted */\n",
       "#sk-container-id-2 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {\n",
       "  color: var(--sklearn-color-text);\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Estimator label */\n",
       "\n",
       "#sk-container-id-2 div.sk-label label {\n",
       "  font-family: monospace;\n",
       "  font-weight: bold;\n",
       "  display: inline-block;\n",
       "  line-height: 1.2em;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-label-container {\n",
       "  text-align: center;\n",
       "}\n",
       "\n",
       "/* Estimator-specific */\n",
       "#sk-container-id-2 div.sk-estimator {\n",
       "  font-family: monospace;\n",
       "  border: 1px dotted var(--sklearn-color-border-box);\n",
       "  border-radius: 0.25em;\n",
       "  box-sizing: border-box;\n",
       "  margin-bottom: 0.5em;\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-0);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-estimator.fitted {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-0);\n",
       "}\n",
       "\n",
       "/* on hover */\n",
       "#sk-container-id-2 div.sk-estimator:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-2);\n",
       "}\n",
       "\n",
       "#sk-container-id-2 div.sk-estimator.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-2);\n",
       "}\n",
       "\n",
       "/* Specification for estimator info (e.g. \"i\" and \"?\") */\n",
       "\n",
       "/* Common style for \"i\" and \"?\" */\n",
       "\n",
       ".sk-estimator-doc-link,\n",
       "a:link.sk-estimator-doc-link,\n",
       "a:visited.sk-estimator-doc-link {\n",
       "  float: right;\n",
       "  font-size: smaller;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1em;\n",
       "  height: 1em;\n",
       "  width: 1em;\n",
       "  text-decoration: none !important;\n",
       "  margin-left: 1ex;\n",
       "  /* unfitted */\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted,\n",
       "a:link.sk-estimator-doc-link.fitted,\n",
       "a:visited.sk-estimator-doc-link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "div.sk-estimator:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link:hover,\n",
       ".sk-estimator-doc-link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover,\n",
       "div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,\n",
       ".sk-estimator-doc-link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "/* Span, style for the box shown on hovering the info icon */\n",
       ".sk-estimator-doc-link span {\n",
       "  display: none;\n",
       "  z-index: 9999;\n",
       "  position: relative;\n",
       "  font-weight: normal;\n",
       "  right: .2ex;\n",
       "  padding: .5ex;\n",
       "  margin: .5ex;\n",
       "  width: min-content;\n",
       "  min-width: 20ex;\n",
       "  max-width: 50ex;\n",
       "  color: var(--sklearn-color-text);\n",
       "  box-shadow: 2pt 2pt 4pt #999;\n",
       "  /* unfitted */\n",
       "  background: var(--sklearn-color-unfitted-level-0);\n",
       "  border: .5pt solid var(--sklearn-color-unfitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link.fitted span {\n",
       "  /* fitted */\n",
       "  background: var(--sklearn-color-fitted-level-0);\n",
       "  border: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "\n",
       ".sk-estimator-doc-link:hover span {\n",
       "  display: block;\n",
       "}\n",
       "\n",
       "/* \"?\"-specific style due to the `<a>` HTML tag */\n",
       "\n",
       "#sk-container-id-2 a.estimator_doc_link {\n",
       "  float: right;\n",
       "  font-size: 1rem;\n",
       "  line-height: 1em;\n",
       "  font-family: monospace;\n",
       "  background-color: var(--sklearn-color-background);\n",
       "  border-radius: 1rem;\n",
       "  height: 1rem;\n",
       "  width: 1rem;\n",
       "  text-decoration: none;\n",
       "  /* unfitted */\n",
       "  color: var(--sklearn-color-unfitted-level-1);\n",
       "  border: var(--sklearn-color-unfitted-level-1) 1pt solid;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 a.estimator_doc_link.fitted {\n",
       "  /* fitted */\n",
       "  border: var(--sklearn-color-fitted-level-1) 1pt solid;\n",
       "  color: var(--sklearn-color-fitted-level-1);\n",
       "}\n",
       "\n",
       "/* On hover */\n",
       "#sk-container-id-2 a.estimator_doc_link:hover {\n",
       "  /* unfitted */\n",
       "  background-color: var(--sklearn-color-unfitted-level-3);\n",
       "  color: var(--sklearn-color-background);\n",
       "  text-decoration: none;\n",
       "}\n",
       "\n",
       "#sk-container-id-2 a.estimator_doc_link.fitted:hover {\n",
       "  /* fitted */\n",
       "  background-color: var(--sklearn-color-fitted-level-3);\n",
       "}\n",
       "</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>GridSearchCV(cv=5, estimator=MLPClassifier(random_state=1), n_jobs=-1,\n",
       "             param_grid={&#x27;activation&#x27;: [&#x27;tanh&#x27;], &#x27;alpha&#x27;: [0.01],\n",
       "                         &#x27;hidden_layer_sizes&#x27;: [(50, 50)], &#x27;max_iter&#x27;: [300],\n",
       "                         &#x27;solver&#x27;: [&#x27;adam&#x27;]},\n",
       "             scoring=&#x27;accuracy&#x27;)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item sk-dashed-wrapped\"><div class=\"sk-label-container\"><div class=\"sk-label fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-4\" type=\"checkbox\" ><label for=\"sk-estimator-id-4\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;&nbsp;GridSearchCV<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.5/modules/generated/sklearn.model_selection.GridSearchCV.html\">?<span>Documentation for GridSearchCV</span></a><span class=\"sk-estimator-doc-link fitted\">i<span>Fitted</span></span></label><div class=\"sk-toggleable__content fitted\"><pre>GridSearchCV(cv=5, estimator=MLPClassifier(random_state=1), n_jobs=-1,\n",
       "             param_grid={&#x27;activation&#x27;: [&#x27;tanh&#x27;], &#x27;alpha&#x27;: [0.01],\n",
       "                         &#x27;hidden_layer_sizes&#x27;: [(50, 50)], &#x27;max_iter&#x27;: [300],\n",
       "                         &#x27;solver&#x27;: [&#x27;adam&#x27;]},\n",
       "             scoring=&#x27;accuracy&#x27;)</pre></div> </div></div><div class=\"sk-parallel\"><div class=\"sk-parallel-item\"><div class=\"sk-item\"><div class=\"sk-label-container\"><div class=\"sk-label fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-5\" type=\"checkbox\" ><label for=\"sk-estimator-id-5\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">best_estimator_: MLPClassifier</label><div class=\"sk-toggleable__content fitted\"><pre>MLPClassifier(activation=&#x27;tanh&#x27;, alpha=0.01, hidden_layer_sizes=(50, 50),\n",
       "              max_iter=300, random_state=1)</pre></div> </div></div><div class=\"sk-serial\"><div class=\"sk-item\"><div class=\"sk-estimator fitted sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-6\" type=\"checkbox\" ><label for=\"sk-estimator-id-6\" class=\"sk-toggleable__label fitted sk-toggleable__label-arrow fitted\">&nbsp;MLPClassifier<a class=\"sk-estimator-doc-link fitted\" rel=\"noreferrer\" target=\"_blank\" href=\"https://scikit-learn.org/1.5/modules/generated/sklearn.neural_network.MLPClassifier.html\">?<span>Documentation for MLPClassifier</span></a></label><div class=\"sk-toggleable__content fitted\"><pre>MLPClassifier(activation=&#x27;tanh&#x27;, alpha=0.01, hidden_layer_sizes=(50, 50),\n",
       "              max_iter=300, random_state=1)</pre></div> </div></div></div></div></div></div></div></div></div>"
      ],
      "text/plain": [
       "GridSearchCV(cv=5, estimator=MLPClassifier(random_state=1), n_jobs=-1,\n",
       "             param_grid={'activation': ['tanh'], 'alpha': [0.01],\n",
       "                         'hidden_layer_sizes': [(50, 50)], 'max_iter': [300],\n",
       "                         'solver': ['adam']},\n",
       "             scoring='accuracy')"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# mlp_params = {\n",
    "#     'hidden_layer_sizes': [(100,), (50, 50), (100, 50, 25)],\n",
    "#     'activation': ['relu', 'tanh'],\n",
    "#     'solver': ['adam'],\n",
    "#     'max_iter': [100, 200, 300],\n",
    "#     'alpha': [0.0001, 0.001, 0.01],\n",
    "# }\n",
    "\n",
    "# Best parameters for MLP\n",
    "mlp_best_params = {\n",
    "    'activation': ['tanh'],\n",
    "    'alpha': [0.01],\n",
    "    'hidden_layer_sizes': [(50, 50)],\n",
    "    'max_iter': [300],\n",
    "    'solver': ['adam'],\n",
    "}\n",
    "\n",
    "# Create grid search\n",
    "mlp_gridsearch = GridSearchCV(estimator=mlpModel, param_grid=mlp_best_params, cv=5, scoring='accuracy', n_jobs=-1)\n",
    "\n",
    "# Fit grid search\n",
    "mlp_gridsearch.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cff5b015",
   "metadata": {
    "papermill": {
     "duration": 0.04396,
     "end_time": "2024-01-10T12:00:56.044930",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.000970",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Get Best parameters and best estimator for MLP from GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9ab7aad2",
   "metadata": {
    "papermill": {
     "duration": 0.048894,
     "end_time": "2024-01-10T12:00:56.129319",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.080425",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Parameters : {'activation': ['tanh'], 'alpha': [0.01], 'hidden_layer_sizes': [(50, 50)], 'max_iter': [300], 'solver': ['adam']}\n",
      "Best Estimator  : MLPClassifier(activation='tanh', alpha=0.01, hidden_layer_sizes=(50, 50),\n",
      "              max_iter=300, random_state=1)\n"
     ]
    }
   ],
   "source": [
    "# mlp_best_params = mlp_gridsearch.best_params_\n",
    "mlp_best_estimator = mlp_gridsearch.best_estimator_\n",
    "\n",
    "print(f\"Best Parameters : {mlp_best_params}\")\n",
    "print(f\"Best Estimator  : {mlp_best_estimator}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "df4e9a85",
   "metadata": {
    "papermill": {
     "duration": 0.033181,
     "end_time": "2024-01-10T12:00:56.196476",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.163295",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Make prediction using best estimator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "834c2a5c",
   "metadata": {
    "papermill": {
     "duration": 0.17572,
     "end_time": "2024-01-10T12:00:56.405284",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.229564",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "mlp_pred_CV = mlp_best_estimator.predict(x_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1cb9440",
   "metadata": {
    "papermill": {
     "duration": 0.055399,
     "end_time": "2024-01-10T12:00:56.533630",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.478231",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3aade7dd",
   "metadata": {
    "papermill": {
     "duration": 0.051315,
     "end_time": "2024-01-10T12:00:56.618459",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.567144",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Accuracy: 87.57\n"
     ]
    }
   ],
   "source": [
    "mlp_accuracy_cv = metrics.accuracy_score(y_test, mlp_pred_CV)*100\n",
    "print(f\"Best Accuracy: {mlp_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a7fdacff",
   "metadata": {
    "papermill": {
     "duration": 0.034027,
     "end_time": "2024-01-10T12:00:56.686674",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.652647",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**MLP** Accuracy Scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "4d7fe865",
   "metadata": {
    "papermill": {
     "duration": 0.047247,
     "end_time": "2024-01-10T12:00:56.771478",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.724231",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MLP accuracy without CV : 87.28\n",
      "MLP accuracy with CV    : 87.57\n"
     ]
    }
   ],
   "source": [
    "print(f\"MLP accuracy without CV : {mlp_accuracy:.2f}\")\n",
    "print(f\"MLP accuracy with CV    : {mlp_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8b402c40",
   "metadata": {
    "papermill": {
     "duration": 0.034264,
     "end_time": "2024-01-10T12:00:56.840651",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.806387",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Classification Report**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "9408717d",
   "metadata": {
    "papermill": {
     "duration": 0.07859,
     "end_time": "2024-01-10T12:00:56.952864",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.874274",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification Report for MLP with CV:\n",
      "               precision    recall  f1-score   support\n",
      "\n",
      "           0     0.8851    0.8730    0.8790      6220\n",
      "           1     0.8660    0.8786    0.8723      5809\n",
      "\n",
      "    accuracy                         0.8757     12029\n",
      "   macro avg     0.8755    0.8758    0.8756     12029\n",
      "weighted avg     0.8759    0.8757    0.8757     12029\n",
      "\n"
     ]
    }
   ],
   "source": [
    "classification_report_str = classification_report(y_test, mlp_pred_CV, digits=4)\n",
    "\n",
    "print(\"Classification Report for MLP with CV:\\n\", classification_report_str)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e39eaa66",
   "metadata": {
    "papermill": {
     "duration": 0.034434,
     "end_time": "2024-01-10T12:00:57.021026",
     "exception": false,
     "start_time": "2024-01-10T12:00:56.986592",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# **SVM**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "968b069a",
   "metadata": {
    "papermill": {
     "duration": 0.033247,
     "end_time": "2024-01-10T12:00:57.089846",
     "exception": false,
     "start_time": "2024-01-10T12:00:57.056599",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Without CV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "49bbecc0",
   "metadata": {
    "papermill": {
     "duration": 53.375229,
     "end_time": "2024-01-10T12:01:50.502673",
     "exception": false,
     "start_time": "2024-01-10T12:00:57.127444",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# build SVM model\n",
    "svmModel = SVC(random_state=1)\n",
    "\n",
    "# Fit the model\n",
    "svmModel.fit(x_train, y_train)\n",
    "\n",
    "# Make predictions\n",
    "svm_pred = mlpModel.predict(x_test)\n",
    "\n",
    "# accuracy\n",
    "svm_accuracy = metrics.accuracy_score(y_test, svm_pred)*100\n",
    "print(f\"Accuracy without CV: {svm_accuracy:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0fcfd9f",
   "metadata": {
    "papermill": {
     "duration": 224.884141,
     "end_time": "2024-01-10T12:05:35.439931",
     "exception": false,
     "start_time": "2024-01-10T12:01:50.555790",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "svm_param_grid = {\n",
    "    'C': [0.1, 1, 10],\n",
    "    'kernel': ['linear', 'rbf', 'poly'],\n",
    "    'gamma': ['scale', 'auto'],\n",
    "}\n",
    "\n",
    "svm_best_params = {\n",
    "    'C': [10],\n",
    "    'kernel': ['rbf'],\n",
    "    'gamma': ['auto'],\n",
    "}\n",
    "\n",
    "# Create grid search\n",
    "svm_gridsearch = GridSearchCV(estimator=svmModel, param_grid=svm_best_params, cv=5, scoring='accuracy', n_jobs=-1)\n",
    "\n",
    "# Fit grid search\n",
    "svm_gridsearch.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "273e47c4",
   "metadata": {
    "papermill": {
     "duration": 0.034208,
     "end_time": "2024-01-10T12:05:35.507888",
     "exception": false,
     "start_time": "2024-01-10T12:05:35.473680",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Get Best parameters and best estimator for SVM from GridSearchCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb1ff10e",
   "metadata": {
    "papermill": {
     "duration": 0.047116,
     "end_time": "2024-01-10T12:05:35.590583",
     "exception": false,
     "start_time": "2024-01-10T12:05:35.543467",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "svm_best_params = svm_gridsearch.best_params_\n",
    "svm_best_estimator = svm_gridsearch.best_estimator_\n",
    "\n",
    "print(f\"Best Parameters : {svm_best_params}\")\n",
    "print(f\"Best Estimator  : {svm_best_estimator}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4163632",
   "metadata": {
    "papermill": {
     "duration": 0.033566,
     "end_time": "2024-01-10T12:05:35.658483",
     "exception": false,
     "start_time": "2024-01-10T12:05:35.624917",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Make prediction using best estimator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8519dcda",
   "metadata": {
    "papermill": {
     "duration": 9.349944,
     "end_time": "2024-01-10T12:05:45.042110",
     "exception": false,
     "start_time": "2024-01-10T12:05:35.692166",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "    svm_pred_CV = svm_best_estimator.predict(x_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5fd8ef0",
   "metadata": {
    "papermill": {
     "duration": 0.034475,
     "end_time": "2024-01-10T12:05:45.111101",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.076626",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "Accuracy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1ab09e3",
   "metadata": {
    "papermill": {
     "duration": 0.049999,
     "end_time": "2024-01-10T12:05:45.196542",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.146543",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "svm_accuracy_cv = metrics.accuracy_score(y_test, svm_pred_CV)*100\n",
    "print(f\"Best Accuracy: {svm_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5dfea265",
   "metadata": {
    "papermill": {
     "duration": 0.034151,
     "end_time": "2024-01-10T12:05:45.269252",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.235101",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**SVM** Accuracy Scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f9159de",
   "metadata": {
    "papermill": {
     "duration": 0.048307,
     "end_time": "2024-01-10T12:05:45.352880",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.304573",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "print(f\"SVM accuracy without CV : {svm_accuracy:.2f}\")\n",
    "print(f\"SVM accuracy with CV    : {svm_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8061bda8",
   "metadata": {
    "papermill": {
     "duration": 0.036739,
     "end_time": "2024-01-10T12:05:45.423912",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.387173",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Classification Report**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b26f93e",
   "metadata": {
    "papermill": {
     "duration": 0.081339,
     "end_time": "2024-01-10T12:05:45.539909",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.458570",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "classification_report_str = classification_report(y_test, svm_pred_CV, digits=4)\n",
    "\n",
    "print(\"Classification Report for SVM with CV:\\n\", classification_report_str)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3aef6882",
   "metadata": {
    "papermill": {
     "duration": 0.036328,
     "end_time": "2024-01-10T12:05:45.611826",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.575498",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Accuracy of all three models**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3e339c5",
   "metadata": {
    "papermill": {
     "duration": 0.045777,
     "end_time": "2024-01-10T12:05:45.694699",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.648922",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "print(f\"RF accuracy with CV    : {rf_accuracy_cv:.2f}\")\n",
    "print(f\"MLP accuracy with CV   : {mlp_accuracy_cv:.2f}\")\n",
    "print(f\"SVM accuracy with CV   : {svm_accuracy_cv:.2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "135d1fa1",
   "metadata": {
    "papermill": {
     "duration": 0.035202,
     "end_time": "2024-01-10T12:05:45.769008",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.733806",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "**Visualization**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "686c132e",
   "metadata": {
    "papermill": {
     "duration": 0.531505,
     "end_time": "2024-01-10T12:05:46.336230",
     "exception": false,
     "start_time": "2024-01-10T12:05:45.804725",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "cnf_matrix = metrics.confusion_matrix(y_test, rf_pred_CV)\n",
    "cnf_matrix\n",
    "\n",
    "class_names=[0,1] # name  of classes\n",
    "fig, ax = plt.subplots()\n",
    "tick_marks = np.arange(len(class_names))\n",
    "plt.xticks(tick_marks, class_names)\n",
    "plt.yticks(tick_marks, class_names)\n",
    "# create heatmap\n",
    "sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap=\"YlGnBu\" ,fmt='g')\n",
    "ax.xaxis.set_label_position(\"top\")\n",
    "plt.tight_layout()\n",
    "plt.title('Confusion matrix: RF', y=1.1)\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb6ce2bf",
   "metadata": {
    "papermill": {
     "duration": 0.61531,
     "end_time": "2024-01-10T12:05:46.988279",
     "exception": false,
     "start_time": "2024-01-10T12:05:46.372969",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "cnf_matrix = metrics.confusion_matrix(y_test, mlp_pred_CV)\n",
    "cnf_matrix\n",
    "\n",
    "class_names=[0,1] # name  of classes\n",
    "fig, ax = plt.subplots()\n",
    "tick_marks = np.arange(len(class_names))\n",
    "plt.xticks(tick_marks, class_names)\n",
    "plt.yticks(tick_marks, class_names)\n",
    "# create heatmap\n",
    "sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap=\"YlGnBu\" ,fmt='g')\n",
    "ax.xaxis.set_label_position(\"top\")\n",
    "plt.tight_layout()\n",
    "plt.title('Confusion matrix: MLP', y=1.1)\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcd28237",
   "metadata": {
    "papermill": {
     "duration": 0.475927,
     "end_time": "2024-01-10T12:05:47.501272",
     "exception": false,
     "start_time": "2024-01-10T12:05:47.025345",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "cnf_matrix = metrics.confusion_matrix(y_test, svm_pred_CV)\n",
    "cnf_matrix\n",
    "\n",
    "class_names=[0,1] # name  of classes\n",
    "fig, ax = plt.subplots()\n",
    "tick_marks = np.arange(len(class_names))\n",
    "plt.xticks(tick_marks, class_names)\n",
    "plt.yticks(tick_marks, class_names)\n",
    "# create heatmap\n",
    "sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap=\"YlGnBu\" ,fmt='g')\n",
    "ax.xaxis.set_label_position(\"top\")\n",
    "plt.tight_layout()\n",
    "plt.title('Confusion matrix: SVM', y=1.1)\n",
    "plt.ylabel('Actual label')\n",
    "plt.xlabel('Predicted label')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8056a37-beaf-4473-8523-6c70ee786c61",
   "metadata": {},
   "outputs": [],
   "source": [
    "import nbformat\n",
    "\n",
    "# Path to your notebook\n",
    "notebook_filename = 'your_notebook.ipynb'\n",
    "\n",
    "# Load the notebook\n",
    "with open(notebook_filename, 'r', encoding='utf-8') as f:\n",
    "    notebook = nbformat.read(f, as_version=4)\n",
    "\n",
    "# Extract all code cells\n",
    "code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code']\n",
    "\n",
    "# Combine all code cells into one big string\n",
    "combined_code = \"\\n\\n\".join([cell['source'] for cell in code_cells])\n",
    "\n",
    "# Print or save the combined code\n",
    "print(combined_code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "82ffcf22-3d20-4809-bc0f-fdeae61b0664",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d930ce5-ca25-4cc1-9da8-e3958160a90e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 107706,
     "sourceId": 256873,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30626,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
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
   "version": "3.10.14"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 1852.70764,
   "end_time": "2024-01-10T12:05:50.169716",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-01-10T11:34:57.462076",
   "version": "2.4.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
