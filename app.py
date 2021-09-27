from flask import Flask, render_template, request
import pickle
import numpy as np
import tensorflow
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow import keras
from tensorflow.keras.models import load_model
import re


model = keras.models.load_model("mortgage_test_13_1_4_final.h5")

app = Flask(__name__)


@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/dashboard', methods=['POST'])
def dashboard():

# state validation
    if request.form['state'] == 'AK':
        data1=0
    elif request.form['state'] == 'AL':
        data1=1
    elif request.form['state'] == 'AR':
        data1=2
    elif request.form['state'] == 'AZ':
        data1=3
    elif request.form['state'] == 'CA':
        data1=4
    elif request.form['state'] == 'CO':
        data1=5
    elif request.form['state'] == 'CT':
        data1=6
    elif request.form['state'] == 'DC':
        data1=7
    elif request.form['state'] == 'DE':
        data1=8
    elif request.form['state'] == 'FL':
        data1=9
    elif request.form['state'] == 'GA':
        data1=10
    elif request.form['state'] == 'GU':
        data1=11
    elif request.form['state'] == 'HI':
        data1=12
    elif request.form['state'] == 'IA':
        data1=13
    elif request.form['state'] == 'ID':
        data1=14
    elif request.form['state'] == 'IL':
        data1=15
    elif request.form['state'] == 'IN':
        data1=16
    elif request.form['state'] == 'KS':
        data1=17
    elif request.form['state'] == 'KY':
        data1=18
    elif request.form['state'] == 'LA':
        data1=19
    elif request.form['state'] == 'MA':
        data1=20
    elif request.form['state'] == 'MD':
        data1=21
    elif request.form['state'] == 'ME':
        data1=22
    elif request.form['state'] == 'MI':
        data1=23
    elif request.form['state'] == 'MN':
        data1=24
    elif request.form['state'] == 'MO':
        data1=25
    elif request.form['state'] == 'MS':
        data1=26
    elif request.form['state'] == 'MT':
        data1=27
    elif request.form['state'] == 'NC':
        data1=28
    elif request.form['state'] == 'ND':
        data1=29
    elif request.form['state'] == 'NE':
        data1=30
    elif request.form['state'] == 'NH':
        data1=31
    elif request.form['state'] == 'NJ':
        data1=32
    elif request.form['state'] == 'NM':
        data1=33
    elif request.form['state'] == 'NV':
        data1=34
    elif request.form['state'] == 'NY':
        data1=35
    elif request.form['state'] == 'OH':
        data1=36
    elif request.form['state'] == 'OK':
        data1=37
    elif request.form['state'] == 'OR':
        data1=38
    elif request.form['state'] == 'PA':
        data1=39
    elif request.form['state'] == 'PR':
        data1=40
    elif request.form['state'] == 'RI':
        data1=41
    elif request.form['state'] == 'SC':
        data1=42
    elif request.form['state'] == 'SD':
        data1=43
    elif request.form['state'] == 'TN':
        data1=44
    elif request.form['state'] == 'TX':
        data1=45
    elif request.form['state'] == 'UT':
        data1=46
    elif request.form['state'] == 'VA':
        data1=47
    elif request.form['state'] == 'VI':
        data1=48
    elif request.form['state'] == 'VT':
        data1=49
    elif request.form['state'] == 'WA':
        data1=50
    elif request.form['state'] == 'WI':
        data1=51
    elif request.form['state'] == 'WV':
        data1=52
    else:
        data1=53
    
#data 2 through 4
    data2 = request.form['loan']
    data3 = request.form['value']
    data4 = request.form['income']

# dwelling validation
    if request.form['dwelling'] == 'Single Family (1-4 Units):Site-Built':
        data5=1
    else:
        data5=0

# occupancy validation
    if request.form['occupancy'] == 'Principal residence':
        data6=1
    elif request.form['occupancy'] == 'Second residence':
        data6=2
    else:
        data6=3
    
# preapproval validation
    if request.form['preapproval'] == 'Preapproval not requested':
        data7=2
    else:
        data7=1
    
# loan-type validation
    if request.form['laon-type'] == 'Conventional (not insured or guaranteed by FHA, VA, RHS, or FSA)':
        data8=1
    elif request.form['laon-type'] == 'Federal Housing Administration insured (FHA)':
        data8=2
    elif request.form['laon-type'] == 'Veterans Affairs guaranteed (VA)':
        data8=3
    else:
        data8=4

# purpose validation
    if request.form['loan-purpose'] == 'Home purchase':
        data9=1
    else:
        data9=31
    
# lien validation
    if request.form['lien'] == 'Secured by a first lien':
        data10=1
    else:
        data10=2
    
# credit type validation
    if request.form['credit-type'] == 'Not an open-end line of credit':
        data11=2
    else:
        data11=1

# amortization validation
    if request.form['amort'] == 'No negative amortization':
        data12=2
    else:
        data12=1

# other amortization features validation
    if request.form['amort-features'] == 'No other non-fully amortizing features':
        data13=2
    else:
        data13=1
    
# interest payment validation
    if request.form['interest'] == 'No interest-only payments':
        data14=2
    else:
        data14=1
    
# balloon validation
    if request.form['balloon'] == 'No balloon payment':
        data15=2
    else:
        data15=1
    
# construction validation
    if request.form['construction'] == 'Site-built':
        data16=1
    else:
        data16=2
    
# manufacturing validation
    if request.form['manufacturing'] == 'Not applicable':
        data17=3
    elif request.form['manufacturing'] == 'Manufactured home and land':
        data17=1
    else:
        data17=2

# credit score type validation
    if request.form['credit-score-type'] == 'Equifax Beacon 5.0':
        data18=1
    elif request.form['credit-score-type'] == 'Experian Fair Isaac':
        data18=2
    elif request.form['credit-score-type'] == 'FICO Risk Score Classic 04':
        data18=3
    elif request.form['credit-score-type'] == 'Not applicable':
        data18=9
    elif request.form['credit-score-type'] == 'VantageScore 3.0':
        data18=6
    elif request.form['credit-score-type'] == 'Other credit scoring model':
        data18=8
    elif request.form['credit-score-type'] == 'More than one credit scoring model':
        data18=7
    elif request.form['credit-score-type'] == 'FICO Risk Score Classic 98':
        data18=4
    else:
        data18=5
    
# cocredit score type validation
    if request.form['co-credit-score-type'] == 'Equifax Beacon 5.0':
        data19=1
    elif request.form['co-credit-score-type'] == 'Experian Fair Isaac':
        data19=2
    elif request.form['co-credit-score-type'] == 'FICO Risk Score Classic 04':
        data19=3
    elif request.form['co-credit-score-type'] == 'Not applicable':
        data19=9
    elif request.form['co-credit-score-type'] == 'VantageScore 3.0':
        data19=6
    elif request.form['co-credit-score-type'] == 'Other credit scoring model':
        data19=8
    elif request.form['co-credit-score-type'] == 'More than one credit scoring model':
        data19=7
    elif request.form['co-credit-score-type'] == 'FICO Risk Score Classic 98':
        data19=4
    elif request.form['co-credit-score-type'] == 'No co-applicant':
        data19=10
    else:
        data19=5
    
# debt-to-income validation
    if request.form['input-debtratio'] == '36%-49%':
        data20=2
    elif request.form['input-debtratio'] == '30%-35%':
        data20=1
    elif request.form['input-debtratio'] == '20%-29%':
        data20=0
    elif request.form['input-debtratio'] == '50%-60%':
        data20=3
    elif request.form['input-debtratio'] == '<20%':
        data20=4
    else:
        data20=5

# age validation
    if request.form['age'] == '45-54':
        data21=2
    elif request.form['age'] == '25-34':
        data21=0
    elif request.form['age'] == '35-44':
        data21=1
    elif request.form['age'] == '65-74':
        data21=4
    elif request.form['age'] == '55-64':
        data21=3
    elif request.form['age'] == '>74':
        data21=6
    else:
        data21=5
    
 # coage validation
    if request.form['coage'] == '45-54':
        data22=2
    elif request.form['coage'] == '25-34':
        data22=0
    elif request.form['coage'] == '35-44':
        data22=1
    elif request.form['coage'] == '65-74':
        data22=4
    elif request.form['coage'] == '55-64':
        data22=3
    elif request.form['coage'] == '>74':
        data22=6
    else:
        data22=5
    
# race validation
    if request.form['race'] == 'White':
        data23=5
    elif request.form['race'] == 'American Indian or Alaska Native':
        data23=1
    elif request.form['race'] == 'Black or African American':
        data23=3
    elif request.form['race'] == 'Asian':
        data23=2
    elif request.form['race'] == 'Information not provided by applicant in mail, internet, or telephone application':
        data23=6
    elif request.form['race'] == 'Vietnamese':
        data23=26
    elif request.form['race'] == 'Native Hawaiian or Other Pacific Islander':
        data23=4
    elif request.form['race'] == 'Other Asian':
        data23=27
    elif request.form['race'] == 'Filipino':
        data23=23
    elif request.form['race'] == 'Asian Indian':
        data23=21
    elif request.form['race'] == 'Other Pacific Islander':
        data23=44
    elif request.form['race'] == 'Native Hawaiian':
        data23=41
    elif request.form['race'] == 'Korean':
        data23=25
    elif request.form['race'] == 'Samoan':
        data23=43
    elif request.form['race'] == 'Chinese':
        data23=22
    elif request.form['race'] == 'Japanese':
        data23=24
    elif request.form['race'] == 'Not applicable':
        data23=7
    else:
        data23=42

# corace validation
    if request.form['corace'] == 'White':
        data24=5
    elif request.form['corace'] == 'American Indian or Alaska Native':
        data24=1
    elif request.form['corace'] == 'Black or African American':
        data24=3
    elif request.form['corace'] == 'Asian':
        data24=2
    elif request.form['corace'] == 'Information not provided by applicant in mail, internet, or telephone application':
        data24=6
    elif request.form['corace'] == 'Vietnamese':
        data24=26
    elif request.form['corace'] == 'Native Hawaiian or Other Pacific Islander':
        data24=4
    elif request.form['corace'] == 'Other Asian':
        data24=27
    elif request.form['corace'] == 'Filipino':
        data24=23
    elif request.form['corace'] == 'Asian Indian':
        data24=21
    elif request.form['corace'] == 'Other Pacific Islander':
        data24=44
    elif request.form['corace'] == 'Native Hawaiian':
        data24=41
    elif request.form['corace'] == 'Korean':
        data24=25
    elif request.form['corace'] == 'Samoan':
        data24=43
    elif request.form['corace'] == 'Chinese':
        data24=22
    elif request.form['corace'] == 'Japanese':
        data24=24
    elif request.form['corace'] == 'Not applicable':
        data24=7
    else:
        data24=42

# race observed validation
    if request.form['race-observed'] == 'Not collected on the basis of visual observation or surname':
        data25=2
    elif request.form['race-observed'] == 'Collected on the basis of visual observation or surname':
        data25=1
    else:
        data25=3
    
# corace observed validation
    if request.form['corace-observed'] == 'Not collected on the basis of visual observation or surname':
        data26=2
    elif request.form['corace-observed'] == 'Collected on the basis of visual observation or surname':
        data26=1
    elif request.form['corace-observed'] == 'No co-applicant':
        data26=4
    else:
        data26=3

# ethnicity validation
    if request.form['ethnicity'] == 'Not Hispanic or Latino':
        data27=2
    elif request.form['ethnicity'] == 'Hispanic or Latino':
        data27=1
    elif request.form['ethnicity'] == 'Information not provided by applicant in mail, internet, or telephone application':
        data27=3
    elif request.form['ethnicity'] == 'Mexican':
        data27=11
    elif request.form['ethnicity'] == 'Other Hispanic or Latino':
        data27=14
    elif request.form['ethnicity'] == 'Cuban':
        data27=13
    elif request.form['ethnicity'] == 'Puerto Rican':
        data27=12
    else:
        data27=4

# coethnicity validation
    if request.form['coethnicity'] == 'Not Hispanic or Latino':
        data28=2
    elif request.form['coethnicity'] == 'Hispanic or Latino':
        data28=1
    elif request.form['coethnicity'] == 'Information not provided by applicant in mail, internet, or telephone application':
        data28=3
    elif request.form['coethnicity'] == 'Mexican':
        data28=11
    elif request.form['coethnicity'] == 'Other Hispanic or Latino':
        data28=14
    elif request.form['coethnicity'] == 'Cuban':
        data28=13
    elif request.form['coethnicity'] == 'Puerto Rican':
        data28=12
    elif request.form['coethnicity'] == 'No co-applicant':
        data28=5
    else:
        data28=4

# ethnicity observed validation
    if request.form['ethnicity-observed'] == 'Not collected on the basis of visual observation or surname':
        data29=2
    elif request.form['ethnicity-observed'] == 'Collected on the basis of visual observation or surname':
        data29=1
    else:
        data29=3

# coethnicity observed validation
    if request.form['coethnicity-observed'] == 'Not collected on the basis of visual observation or surname':
        data30=2
    elif request.form['coethnicity-observed'] == 'Collected on the basis of visual observation or surname':
        data30=1
    elif request.form['coethnicity-observed'] == 'No co-applicant':
        data30=4
    else:
        data30=3

# sex validation
    if request.form['sex'] == 'Male':
        data31=1
    elif request.form['sex'] == 'Female':
        data31=2
    elif request.form['sex'] == 'Information not provided by applicant in mail, internet, or telephone application':
        data31=3
    elif request.form['sex'] == 'Applicant selected both male and female':
        data31=6
    else:
        data31=4

# cosex validation
    if request.form['cosex'] == 'Male':
        data32=1
    elif request.form['cosex'] == 'Female':
        data32=2
    elif request.form['cosex'] == 'Information not provided by applicant in mail, internet, or telephone application':
        data32=3
    elif request.form['cosex'] == 'Applicant selected both male and female':
        data32=6
    elif request.form['cosex'] == 'No co-applicant':
        data32=5
    else:
        data32=4

# sex-observed observed validation
    if request.form['sex-observed'] == 'Not collected on the basis of visual observation or surname':
        data33=2
    elif request.form['sex-observed'] == 'Collected on the basis of visual observation or surname':
        data33=1
    else:
        data33=3

# cosex-observed observed validation
    if request.form['cosex-observed'] == 'Not collected on the basis of visual observation or surname':
        data34=2
    elif request.form['cosex-observed'] == 'Collected on the basis of visual observation or surname':
        data34=1
    elif request.form['cosex-observed'] == 'No co-applicant':
        data34=4
    else:
        data34=3

# aus observed validation
    if request.form['aus'] == 'Not applicable':
        data35=6
    elif request.form['aus'] == 'Desktop Underwriter (DU)':
        data35=1
    elif request.form['cosex-observed'] == 'Loan Prospector (LP) or Loan Product Advisor':
        data35=2
    elif request.form['aus'] == 'Guaranteed Underwriting System (GUS)':
        data35=4
    elif request.form['cosex-observed'] == 'Technology Open to Approved Lenders (TOTAL) Scorecard':
        data35=3
    else:
        data35=5
    
# conforming observed validation
    if request.form['conforming'] == 'C':
        data36=0
    else:
        data36=1

#data 37 thru 44
    data37 = request.form['county']
    data38 = request.form['census']
    data39 = request.form['tract_minority']
    data40 = request.form['median_fam_income']
    data41 = request.form['msa_income']
    data42 = request.form['one_to_four']
    data43 = request.form['age_housing']
    data44 = request.form['term']

# manufacturing interest
    if request.form['manufacturing-interest'] == 'Direct ownership':
        data45=1
    elif request.form['manufacturing-interest'] == 'Indirect ownership':
        data45=2
    elif request.form['manufacturing-interest'] == 'Paid leasehold':
        data45=3
    elif request.form['manufacturing-interest'] == 'Unpaid leasehold':
        data45=4
    else:
        data45=5

#modeling
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10,data11, data12, data13, data14, data15, data16, data17, data18, data19, data20,data21, data22, data23, data24, data25, data26, data27, data28, data29, data30, data31, data32, data33, data34, data35, data36, data37, data38, data39, data40,data41, data42, data43, data44, data45]], dtype=np.float32)
    pred = model.predict(arr)
#predictions prints out the numpy array
    classes_x = np.argmax(pred,axis=1)
    
#outputs array([1]) which matches the action_taken for that row

    return render_template('dashboard.html', data=classes_x)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home Page')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/process")
def process():
    return render_template('process.html', title='Our Model')


if __name__ == "__main__":
    app.run(debug=True)














