{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "<h1>MIMIC II Project </h1>\n",
    "\n",
    "<h3>Shilpy Sharma, Parveen Ghani, Anjali Nandwani </h3>\n",
    "\n",
    "<h4> BMI 6018 Fall 2017 Term Project</h4>\n",
    "<h3>Background:</h3>\n",
    "<p>This project explores the cohort of patient who has Chronic Kidney Disease (CKD) based  <br> \n",
    "    on the ICD 9 code associated with the patient and tracks their Serum Creatinine value.<br>\n",
    "    Project shows the visualization of the change in Serum Creatinine value over time<br>        \n",
    "</p>\n",
    "<h3>Project Goals:</h3>\n",
    "1.\tExtract all the patient with ICD 9 code for CKD:\n",
    "    <ul>\n",
    "        <li>unspecified - 585.9</li>\n",
    "        <li>Stage I - 585.1</li>\n",
    "        <li>Stage II (mild) - 585.2</li>\n",
    "        <li>Stage III (moderate) - 585.3</li>\n",
    "        <li>Stage IV (severe) - 585.4</li>\n",
    "        <li>Stage V - 585.5</li>\n",
    "        <li>End-Stage Renal Disease(ESRD) - 585.6</li>\n",
    "    </ul>\n",
    "\n",
    "2.\tExtract the patient's age, gender, ethnicity who has CKD and shows statistics.\n",
    "3.\tUses class for the lab values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pymysql\n",
    "import pandas as pd\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from ipywidgets import interact, interactive, fixed\n",
    "from IPython.display import clear_output\n",
    "import ipywidgets as widgets\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = pymysql.connect(host=\"mysql\",\n",
    "                       port=3306,user=\"jovyan\",\n",
    "                       passwd=\"jovyan\",db='mimic2')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from project import DiseaseFrame\n",
    "\n",
    "test = DiseaseFrame(conn)\n",
    "\n",
    "test.get_dfs()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display, clear_output, HTML\n",
    "\n",
    "from ipywidgets import interact, interactive, fixed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3cc95a45c77549a5b77a5759b2e0215f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "539f2fd1eae24535bb83029b2b5e5c1b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "29d113aa27bb414ea5456c71acc13cd4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9fd306aba3434dc0abf3477e71734a87",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "disease1 = widgets.Dropdown(options=['Heart Failure', 'Diabetes', 'Hypertension', 'Obesity', 'Drug Abuse', 'Alcohol Abuse', 'Liver Disease'], value = 'Diabetes', description = 'disease:', disabled = False)\n",
    "disease2 = widgets.Dropdown(options=['Heart Failure', 'Diabetes', 'Hypertension', 'Obesity', 'Drug Abuse', 'Alcohol Abuse', 'Liver Disease'], value = 'Heart Failure', description = 'disease:', disabled = False)\n",
    "disease3 = widgets.Dropdown(options=['Heart Failure', 'Diabetes', 'Hypertension', 'Obesity', 'Drug Abuse', 'Alcohol Abuse', 'Liver Disease'], value = 'Hypertension', description = 'disease:', disabled = False)\n",
    "button = widgets.Button(description=\"Create Venn\")\n",
    "\n",
    "display(disease1, disease2, disease3, button)\n",
    "\n",
    "def on_button_clicked(b):\n",
    "    clear_output()\n",
    "    display(disease1, disease2, disease3, button)\n",
    "    tmp = test.get_venn(disease1.value, disease2.value, disease3.value)\n",
    "        \n",
    "\n",
    "button.on_click(on_button_clicked)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ee6ff865e8f24d4db19751a9f5d2014a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "70bd291adb5d44eabf1dc8136c6c0e53",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "681ab36bdb2040beb11a431b9f5cbcc0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "742dc4cb4913416a9f625e5c6c137e9a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "46c05094a79749489f5ff0aa417bf166",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9a5cf322b94c43fa9b0409a98f03be83",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "A Jupyter Widget"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from project import calc_gfr\n",
    "\n",
    "caption = widgets.Label(value='Input followings to calculate Glomerular Filteration Rate (GFR)')\n",
    "\n",
    "scr = widgets.BoundedFloatText(value = 2.0, min = 0, max = 5, step = 0.1, description = 'Creatinine:', disabled = False)\n",
    "\n",
    "age = widgets.BoundedFloatText(value = 50, min = 1, max = 90, step = 1, description = 'Age:', disabled = False)\n",
    "\n",
    "gender = widgets.Dropdown(options=[' ', 'F', 'M'], value = ' ', description = 'Gender:', disabled = False)\n",
    "\n",
    "ethnicity = widgets.Dropdown(options = [' ', 'Caucasian', 'African American', 'Asian', 'Others'], value = ' ',\\\n",
    "                                description = 'Ethnicity:', disabled = False)\n",
    "\n",
    "button = widgets.Button(description=\"Calculate GFR\")\n",
    "\n",
    "\n",
    "display(caption, scr, age, gender, ethnicity, button)\n",
    "\n",
    "def on_button_clicked(b):\n",
    "    clear_output()   \n",
    "    display(caption, scr, age, gender, ethnicity, button)\n",
    "    print(calc_gfr(scr.value, age.value, gender.value, ethnicity.value))\n",
    "        \n",
    "\n",
    "button.on_click(on_button_clicked)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Query: Identifying CKD Patients by ICD9 Codes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>COUNT(*)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   COUNT(*)\n",
       "0      4000"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from project import DiseaseFrame\n",
    "DiseaseFrame(conn).count_total_pt()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'DiseaseFrame' object has no attribute 'count_icd9'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-12-760acf572550>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mDiseaseFrame\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mconn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcount_icd9\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m: 'DiseaseFrame' object has no attribute 'count_icd9'"
     ]
    }
   ],
   "source": [
    "DiseaseFrame(conn).count_icd9()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h4>There are 4000 total patients in MIMIC II database.  Out of 4000 patients, 328 patients have a diagnosis of CKD based on ICD9 codes.</h4>\n",
    "<p>The description for the ICD9 codes are not available for all the CKD stages in MIMIC II database <br>\n",
    "   They have a description of \"None\".<br>\n",
    "</p>\n",
    "<h4> Below is the list of frequency of each diagnosis by the ICD9 codes.</h4>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Add code to add description for the ICD9 code\n",
    "icd9_codes[\"code\"].value_counts(normalize=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h4> Since it is the ICU data, most diagnosis is either \"unspecified CKD\" or \"ESRD\".</h4>\n",
    "<p>Below is a bar graph showing the distribution each ICD9 codes for CKD</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "icd9_counts = icd9_codes[\"code\"].value_counts().to_frame(name=\"ICD9 Counts\")\n",
    "icd9_counts.sort_values(by=\"ICD9 Counts\")\n",
    "icd9_counts.plot(kind='bar', title ='Occurence of CKD')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "subject_info = pd.read_sql(' SELECT subject_id, sex, dob FROM d_patients', conn)   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "subject_info.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "frequently_used_itemid_creat = \\\n",
    "pd.read_sql('SELECT itemid, COUNT(itemid) FROM chartevents WHERE itemid in (17, 791, 1129, 1525, 2975, 3750, 5525, 5811) \\\n",
    "            GROUP BY itemid', conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "frequently_used_itemid_creat"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p> Only the below itemids are used in the charting for the creatinine values:\n",
    "<ul>\n",
    "    <li>791 - Creatinine (0-1.3) Chemistry </li>\n",
    "    <li>1525 - Creatinine Chemistry</li>\n",
    "    <li>3750 - Creatinine (0-0.7) Chemistry</li>\n",
    "</ul> \n",
    "</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "creat_ckd = \\\n",
    "pd.read_sql('SELECT subject_id, itemid, charttime, value1num FROM chartevents WHERE itemid IN (17, 791, 1129, 1525, 2975, 3750, 5525, 5811)\\\n",
    "            AND subject_id IN (SELECT subject_id FROM icd9 \\\n",
    "            WHERE code IN (\"585.9\", \"585.1\", \"585.2\", \"585.3\", \"585.4\", \"585.5\", \"585.6\" ))', conn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "creat_ckd.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Look for the missing values of creatinine and drop the missing data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Look for the missing values of creatinine and drop the missing data\n",
    "creat_cleaned = creat_ckd.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "creat_cleaned.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "#### We had total of 10361 rows for creatinine values, after dropping the missing values we have 10357 rows, (only 4 missing values for creatinine.)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Making a venn diagram of all the comorbidities for all the patients with a diagnosis of CKD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "##### deleted the code for the venn diagram and made it into a module."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "gfr_calc_info = pd.read_excel('gfr_calc_info.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "gfr_calc_info.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "gfr_calc_info.dropna()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Use regular expression to separate ethnicity if it is \"BLACK/AFRICAN AMERICAN\" to \"AFRICAN AMERICAN\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def replace_black(excel_file):\n",
    "    \"\"\"\n",
    "    This function replaces all the ethnicity that is maked \"BLACK/AFRICAN AMERICAN\" to \"AFRICAN AMERICAN\"\n",
    "    Argument:  excel_file - to extract the column\n",
    "    Returns: excel_file - with ethnicity replaced.\n",
    "    \"\"\"\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from project import calc_gfr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst_egfr = []\n",
    "for index, row in gfr_calc_info.iterrows():\n",
    "    lst_egfr.append(calc_gfr(row['VALUENUM'], row['AGE'], row['GENDER'], row['ETHNICITY']) )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lst_egfr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "gfr_calc_info['GFR'] = pd.Series(lst_egfr, index=gfr_calc_info.index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "gfr_calc_info.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Finding mean age of CKD patients"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_age = pd.read_sql('''\n",
    "    SELECT FLOOR(DATEDIFF(dod, dob)/365) age_years, sex, subject_id\n",
    "    from d_patients WHERE subject_id IN (SELECT DISTINCT(subject_id) FROM icd9 WHERE code IN \\\n",
    "                        (\"585.9\", \"585.1\", \"585.2\", \"585.3\", \"585.4\", \"585.5\", \"585.6\" ))\n",
    "    ''',conn)\n",
    "\n",
    "df_age.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def mean_age():\n",
    "    avgAge = []\n",
    "    for i in df_age:\n",
    "        avgAge.append(df_age['age_years'])\n",
    "    np.mean(avgAge)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_age[\"age_years\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(mean_age())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "\"\"\"ASK\"\"\"\n",
    "\n",
    "\"\"\"all_age = gfr_calc_info.drop('SUBJECT_ID', axis=1).drop('GENDER', axis=1).\\\n",
    "drop('ETHNICITY', axis=1).drop('VALUENUM', axis=1).drop('VALUEUOM', axis=1)\n",
    "all_age \"\"\"\n",
    "\n",
    "\n",
    "def mean_age():\n",
    "    \"\"\"\n",
    "    This function calculates the mean age of all the patients with \n",
    "    Chronic Kidney Disease from the \"gfr_calc_info.xlsx\" file.\n",
    "    Arguments:\n",
    "        data_file: source of data\n",
    "    Returns: \n",
    "        Calculated mean of age        \n",
    "    \"\"\"\n",
    "    gfr_calc_info2 = pd.read_excel('gfr_calc_info.xlsx')\n",
    "\n",
    "    all_age = gfr_calc_info2['AGE']\n",
    "    \n",
    "    avgAge = []\n",
    "    for i in all_age:\n",
    "        avgAge.append(float(i))\n",
    "    np.mean(avgAge)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "print(mean_age())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "avgLen = []\n",
    "for word in report1.split():\n",
    "    avgLen.append(len(word))\n",
    "np.mean(avgLen)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Widget"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import ipywidgets as widgets\n",
    "from IPython.display import display, clear_output, HTML\n",
    "\n",
    "from ipywidgets import interact, interactive, fixed\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
