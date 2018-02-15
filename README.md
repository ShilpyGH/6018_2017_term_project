<h1>Chronic Kidney Disease (CKD) patients in MIMIC II</h1>
<h3>Shilpy Sharma</h3>
<h4>BMI 6018 Fall 2017 Term Project</h4>

<h3>Source of data - MIMIC II database</h3>

<p>
The MIMIC II (Multiparameter Intelligent Monitoring in Intensive Care) Database contains
comprehensive clinical data obtained from hospital medical information systems, 
for tens of thousands of Intensive Care Unit (ICU) patients. 
Data were collected between 2001 and 2008 from a variety of ICUs in a single tertiary teaching hospital.
The MIMIC II Clinical Database contains clinical data from bedside workstations as well as hospital archives. 

<h3>Chronic Kidney Disease (CKD)</h3>

CKD is a type of kidney disease where patient gradually lose their kidney function over a period of time.
CKD is measured by the patient’s serum creatinine levels and an estimated Glomerular Filtration Rate (eGFR) is calculated using various formulas.  This project uses the MDRD equation to calculate the eGFR.

      GFR=175×(Scr)^-1.154×(Age)^-0.203×(0.742 if female)×(1.212 if African American)
      
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

<h3>Project Goals: </h3>
<p>
       <ul>
             <li>Extract all the patient with ICD 9 code for CKD</li>
             <li>Extract the patient's age, gender, ethnicity who has CKD</li>
             <li>Shows statistics of patient's ethnicity, age, gender and different kinds of CKDs.</li>
             <li>Calculates the mean age of all the CKD patients.</li>
             <li>Widget to calculate the eGFR, by manually inputing the data.</li>
             <li>Cleans the excel file extracted from MIMIC II by dropping the missing values.</li>
             <li>Calculates the eGFR, automatically for all the patients based on their age, gender, ethnicity and serum creatinine value</li>
</p>
<h4>Files Used: gfr_calc_info.xlsx</h4>
<h3>Requirements:</h3>
<p>
<ul><li>Python</li><li>Jupyter Notebook</li><li>Excel</li><li>MySql</li></ul>
</p>

<h3>Version: v1.0 released on 2017-12-21</h3>

<h3>Authors: </h3>
<p>Shilpy Sharma (lead), Parveen Ghani, Anjali Nandwani</p>

<h3>Licence: </h3>
<p>
The project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.
See the LICENSE.md file for details</p>

