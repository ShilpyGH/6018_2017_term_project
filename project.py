import pandas as pd
from matplotlib_venn import venn3


def calc_gfr(scr, age, gender, ethnicity):
    """Calculates the estimated Glomerular Filteration Rate(eGFR)
    
    Based on MDRD equation.
    GFR=175×(Scr)^-1.154×(Age)^-0.203×(0.742 if female)×(1.212 if AA)
    
    Arguments: 
        scr: Patient's serum creatinine level in mg/dL as float
        age: Patient's age in years as integer
        gender: Patient's gender "male" or "female" as string
        ethnicity: Patient's ethicity   
        
    Returns: 
        gfr: Patient's eGFR in mL/min rounded to decimal places.
        
    """
    if scr==0.0 or age==0.0:
        return 0
  
    if gender=='F' and ethnicity=='African American':
        egfr = round(175*(scr)**(-1.154) * age**(-0.203) * (0.742) * 1.212, 2)
    elif gender == 'F' and ethnicity != 'African American':
        egfr = round(175*(scr)**(-1.154) * age**(-0.203) * (0.742), 2)
    elif gender == 'M' and ethnicity == 'African American':
        egfr = round(175*(scr)**(-1.154) * age**(-0.203) * 1.212, 2)
    else:
        egfr = round(175*(scr)**(-1.154) * age**(-0.203), 2)    
    return egfr


class DiseaseFrame(dict):
    """Makes the disease dataframe into a dictionary for the venn diagram.
    
    DiseaseFrame class inherits from the python's builtin class dictionary.
    It makes the connection to the MIMIC II database and pulls different
    comorbidities the CKD patients has in a pandas dataframe.
    These comorbidities dataframe is later converted in a list and then to a set 
    to make a venn diagram for three chosen the comorbidities from the widget.
    
    """
    
    def __init__(self, conn, *args, **kwargs):
        """Makes the intial connection to MIMIC II database"""
        
        self.conn = conn
        super(DiseaseFrame, self).__init__(*args, **kwargs)
        
    def get_dfs(self):
        """Pulls the subject_id from the MIMIC database, table comorbidity_scores.
        
        Pulls the subject_id, who has CKD and the comorbidities like 
        Heart Failure, Diabetes, Hypertension, Obesity, Drug Abuse, 
        Alcohol Abuse, Liver disease.
        
        """
        
        self['Heart Failure'] = pd.read_sql('SELECT DISTINCT(subject_id)\
                                FROM comorbidity_scores WHERE subject_id \
                                IN (SELECT DISTINCT(subject_id) FROM icd9\
                                WHERE code IN \
                                ("585.9", "585.1", "585.2", "585.3", \
                                "585.4", "585.5", "585.6")\
                                AND congestive_heart_failure=1.0)',\
                                            self.conn)
        
        self['Diabetes'] = pd.read_sql('SELECT DISTINCT(subject_id) \
                            FROM comorbidity_scores WHERE subject_id\
                            IN (SELECT DISTINCT(subject_id) FROM icd9\
                            WHERE code IN \
                            ("585.9", "585.1", "585.2", "585.3", "585.4",\
                            "585.5", "585.6") AND \
                            (diabetes_uncomplicated=1.0\
                            OR diabetes_complicated=1.0))', self.conn)
        
        self['Hypertension'] = pd.read_sql('SELECT DISTINCT(subject_id)\
                                FROM comorbidity_scores WHERE subject_id \
                            IN (SELECT DISTINCT(subject_id) FROM icd9 \
                            WHERE code IN \
                            ("585.9", "585.1", "585.2", "585.3", "585.4", \
                            "585.5", "585.6") AND hypertension=1.0)',\
                             self.conn)
                                                   
        
        self['Obesity'] = pd.read_sql('SELECT DISTINCT(subject_id) \
                            FROM comorbidity_scores WHERE subject_id \
                            IN (SELECT DISTINCT(subject_id) FROM icd9 \
                            WHERE code IN \
                            ("585.9", "585.1", "585.2", "585.3", "585.4",\
                            "585.5", "585.6") AND obesity=1.0)', self.conn)
        
        self['Drug Abuse'] = pd.read_sql('SELECT DISTINCT(subject_id) \
                            FROM comorbidity_scores WHERE subject_id \
                            IN (SELECT DISTINCT(subject_id) FROM icd9 \
                            WHERE code IN \
                            ("585.9", "585.1", "585.2", "585.3", "585.4", \
                            "585.5", "585.6") AND drug_abuse=1.0)', self.conn)
        
        self['Alcohol Abuse'] = pd.read_sql('SELECT DISTINCT(subject_id)\
                            FROM comorbidity_scores WHERE subject_id \
                            IN (SELECT DISTINCT(subject_id) FROM icd9\
                            WHERE code IN \
                            ("585.9", "585.1", "585.2", "585.3", "585.4","585.5", \
                            "585.6") AND alcohol_abuse=1.0)', self.conn)
        
        self['Liver disease'] = pd.read_sql('SELECT DISTINCT(subject_id)\
                            FROM comorbidity_scores WHERE subject_id \
                            IN (SELECT DISTINCT(subject_id) FROM icd9\
                            WHERE code IN \
                            ("585.9", "585.1", "585.2", "585.3", "585.4", "585.5", \
                            "585.6") AND liver_disease=1.0)', self.conn)
        
    def create_venn(self, disease1, disease2, disease3):
        """Creates the venn diagram for the chosen diseases"""
        
        d_list1 = set(self[disease1]['subject_id'].tolist())    
        d_list2 = set(self[disease2]['subject_id'].tolist())
        d_list3 = set(self[disease3]['subject_id'].tolist())
       
        return venn3(subsets = (d_list1, d_list2,d_list3), \
                     set_labels = (disease1, disease2, disease3))
    
    def count_total_pt(self):
        """Counts the total number of patients in MIMIC II database"""
        
        return (pd.read_sql('SELECT COUNT(*) FROM d_patients', self.conn))
    
    def count_icd9(self):
        """Counts the various CKD patients based on ICD9 codes"""
        
        return (pd.read_sql('SELECT DISTINCT(subject_id), code, description \
                FROM icd9 WHERE code IN \
                ("585.9", "585.1", "585.2", "585.3", "585.4", "585.5",\
                "585.6")', self.conn))
    
    def get_patient_info(self):
        """Returns the patient information from MIMIC II"""
        
        return (pd.read_sql("SELECT subject_id, sex, \
                FLOOR(DATEDIFF(dod, dob)/365) age_years FROM d_patients \
                WHERE subject_id IN \
                (SELECT subject_id FROM icd9 WHERE code IN ('585.9', \
                '585.1', '585.2', '585.3','585.4', '585.5', '585.6')) ", self.conn))
    
    def get_creatinine_count(self):
        """Returns the count for the various itemids for creatinine in MIMIC"""
        
        return (pd.read_sql('SELECT itemid, COUNT(itemid) \
                FROM chartevents WHERE itemid IN \
                (17, 791, 1129, 1525, 2975, 3750, 5525, 5811) \
                GROUP BY itemid', self.conn))
                
    def get_all_creatinine_ckd_patient_cleaned(self):
        """Returns all the recorded creatinine values for the CKD patients"""
                
        all_creat_ckd = (pd.read_sql('SELECT subject_id, itemid, charttime, \
                value1num \
                FROM chartevents WHERE itemid IN \
                (17, 791, 1129, 1525, 2975, 3750, 5525, 5811)\
                AND subject_id IN (SELECT subject_id FROM icd9 \
                WHERE code IN ("585.9", "585.1", "585.2", "585.3", \
                "585.4", "585.5", "585.6"))', self.conn))
                         
        all_creat_ckd_cleaned = all_creat_ckd.dropna()   
                         
        return all_creat_ckd_cleaned    
                
    def get_mean_age(self):
        """Returns the mean age of the CKD patients """
        df_age = pd.read_sql('''SELECT FLOOR(DATEDIFF(dod, dob)/365) age_years,\
                sex, subject_id \
                FROM d_patients \
                WHERE subject_id \
                IN (SELECT DISTINCT(subject_id) FROM icd9 WHERE code\
                IN ("585.9", "585.1", "585.2", "585.3", "585.4", "585.5", "585.6" ))
                ''',self.conn)
                         
        return df_age["age_years"].mean()   
                         
    def get_ckd_age(self):
        """Returns the age distribution of the CKD patients from MIMIC II"""  
                         
        df_age = pd.read_sql('''SELECT FLOOR(DATEDIFF(dod, dob)/365) age_years
                FROM d_patients \
                WHERE subject_id \
                IN (SELECT DISTINCT(subject_id) FROM icd9 WHERE code\
                IN ("585.9", "585.1", "585.2", "585.3", "585.4", "585.5", "585.6"))
                ''',self.conn)
                         
        df_age = df_age.dropna()
        return df_age                   
                            
    def get_ckd_ethnictiy(self):
        """Returns the ethnicity distribution of CKD patients from MIMIC II"""
        return (pd.read_sql("SELECT DISTINCT(subject_id), ethnicity_descr FROM demographic_detail  \
                WHERE ethnicity_descr IN ('WHITE', 'BLACK/AFRICAN AMERICAN', 'ASIAN', 'OTHER')  \
                AND subject_id \
                            IN (SELECT DISTINCT(subject_id) FROM icd9\
                            WHERE code IN \
                            ('585.9', '585.1', '585.2', '585.3', '585.4', '585.5' \
                            '585.6'))", self.conn))
                
