<h1>Chronic Kidney Disease (CKD) patients in MIMIC II</h1>
<h3>Shilpy Sharma, Parveen Ghani, Anjali Nandwani</h3>
<h4>BMI 6018 Fall 2017 Term Project</h4>

<h3>Source of data - MIMIC II database</h3>

<p>
The MIMIC II (Multiparameter Intelligent Monitoring in Intensive Care) Database contains
comprehensive clinical data obtained from hospital medical information systems, 
for tens of thousands of Intensive Care Unit (ICU) patients. 
Data were collected between 2001 and 2008 from a variety of ICUs in a single tertiary teaching hospital.
The MIMIC II Clinical Database contains clinical data from bedside workstations as well as hospital archives. 

Chronic Kidney Disease (CKD)

CKD is a type of kidney disease where patient gradually lose their kidney function over a period of time.
CKD is measured by the patient’s serum creatinine levels and an estimated Glomerular Filtration Rate (eGFR) is calculated using various formulas.  This project uses the MDRD equation to calculate the eGFR.
There are six stages of CKD, mentioned below with the associated ICD9 codes.
      unspecified - 585.9
      Stage I - 585.1
      Stage II (mild) - 585.2
      Stage III (moderate) - 585.3
      Stage IV (severe) - 585.4
      Stage V - 585.5
      End-Stage Renal Disease(ESRD) - 585.6
(ICD9 code are the diagnosis code used to record the diagnosis of a patient.)

CKD is accompanied by various comorbidities.  This project explores how different comorbidities are associated with the CKD.  Project shows the visualization (venn diagram) of all the comorbidities associated with CKD patients in MIMIC II.
It has widgets to calculate the estimated Glomerular Filteration Rate (eGFR) based on MDRD equation.

Project Goals:
1.	Extract all the patient with ICD 9 code for CKD
2.	Extract the patient's age, gender, ethnicity who has CKD
3.	Shows statistics of patient's ethnicity, age, gender and different kinds of CKDs.
4.	Calculates the mean age of all the CKD patients.
5.	Widget to calculate the eGFR, by manually inputing the data.
6.	Cleans the excel file extracted from MIMIC II by dropping the missing values.
7.	Calculates the eGFR, automatically for all the patients based on their age, gender, ethnicity and serum creatinine value
