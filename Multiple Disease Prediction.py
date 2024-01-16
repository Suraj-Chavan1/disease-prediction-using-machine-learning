


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_login_auth_ui.widgets import __login__


if 'login' not in st.session_state:
    st.session_state.login = False

__login__obj = __login__(auth_token="dk_test_RN34A0A2EC4QQ2GWV9WVG0Y1K7G9",

                    company_name="Shims",
                    width=200, height=250,
                    logout_button_name='Logout', hide_menu_bool=False,
                    hide_footer_bool=False,
                    lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

st.session_state.login = __login__obj.build_login_ui()

if st.session_state.login:
    st.markdown("Welcome to Main page!")

    # Get the user name.
    fetched_cookies = __login__obj.cookies
    if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
        username = fetched_cookies['__streamlit_login_signup_ui_username__']
        st.write(username) 
    
    
      
        
        diabetes_model = pickle.load(open('D:\ML\Multiplediseaseprediction/diabetes_model.sav', 'rb'))
    
        heart_disease_model = pickle.load(open('D:\ML\Multiplediseaseprediction/heart_disease_model.sav','rb'))
    
        parkinsons_model = pickle.load(open('D:\ML\Multiplediseaseprediction/parkinsons_model.sav', 'rb'))
        
        
    
        with open("D:\ML\Multiplediseaseprediction\liver_model.sav", 'rb') as f:
            liver_model = pickle.load(f, encoding='utf-8')
            
        with open("D:\ML\Multiplediseaseprediction\kidneymodel.sav", 'rb') as f:
            kidney_model = pickle.load(f, encoding='utf-8')

    
    
    
    
    
    
    
    
    
    
    
        with st.sidebar:
            st.set_option('deprecation.showfileUploaderEncoding', False)
            
            st.image('https://www2.deloitte.com/content/dam/insights/us/articles/6872_AI-in-healthcare/images/6872_banner.png/jcr:content/renditions/cq5dam.web.1440.660.jpeg', width=200)
            st.markdown('## Multiple Disease Prediction System')
            
            selected = option_menu('', ['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Liver Prediction' , 'Kidney Disease Predictionid'])
    
    

        # Home Page
        if selected == 'Home':
            st.title('Welcome to Multiple Disease Prediction System')
            st.image('https://www2.deloitte.com/content/dam/insights/us/articles/6872_AI-in-healthcare/images/6872_banner.png/jcr:content/renditions/cq5dam.web.1440.660.jpeg', use_column_width=True)
            st.write('This system can predict multiple diseases such as diabetes, heart disease, Parkinson’s disease and liver disease.')
            st.write('Please select the disease prediction option from the sidebar to continue.')
            
            # add a section for health tips
            st.markdown('## Health Tips')
            st.write('Here are some tips to help you stay healthy:')
            st.write('- Eat a balanced and nutritious diet')
            st.write('- Exercise regularly')
            st.write('- Get enough sleep')
            st.write('- Manage your stress levels')
            
            # add a section for interesting health facts
            st.markdown('## Health Facts')
            st.write('Did you know that:')
            st.write('- Drinking coffee may reduce your risk of liver cancer')
            st.write('- Eating blueberries may help improve memory function')
            st.write('- Laughing can help lower blood pressure and reduce stress hormones')
            
         
    
    
    
    
            
        # Diabetes Prediction Page
        if (selected == 'Diabetes Prediction'):
            
            # page title
            st.title('Diabetes Prediction using ML')
            
            
            # getting the input data from the user
            col1, col2, col3 = st.columns(3)
            
            with col1:
                Pregnancies = st.text_input('Number of Pregnancies')
                
            with col2:
                Glucose = st.text_input('Glucose Level')
            
            with col3:
                BloodPressure = st.text_input('Blood Pressure value')
            
            with col1:
                SkinThickness = st.text_input('Skin Thickness value')
            
            with col2:
                Insulin = st.text_input('Insulin Level')
            
            with col3:
                BMI = st.text_input('BMI value')
            
            with col1:
                DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
            
            with col2:
                Age = st.text_input('Age of the Person')
            
            
            # code for Prediction
            diab_diagnosis = ''
            
            # creating a button for Prediction
            
            if st.button('Diabetes Test Result'):
                diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                
                if (diab_prediction[0] == 1):
                  diab_diagnosis = 'The person is diabetic you can consult  Dhope Clinic , Dr Kale in Pune'
                else:
                  diab_diagnosis = 'The person is not diabetic '
                
            st.success(diab_diagnosis)
    
    
    
    
        # Heart Disease Prediction Page
        if (selected == 'Heart Disease Prediction'):
            
            # page title
            st.title('Heart Disease Prediction using ML')
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                age = st.text_input('Age')
                
            with col2:
                sex = st.text_input('Sex')
                
            with col3:
                cp = st.text_input('Chest Pain types')
                
            with col1:
                trestbps = st.text_input('Resting Blood Pressure')
                
            with col2:
                chol = st.text_input('Serum Cholestoral in mg/dl')
                
            with col3:
                fbs = st.text_input('Fasting Blood Sugar')
                
            with col1:
                restecg = st.text_input('Resting Electrocardiographic results')
                
            with col2:
                thalach = st.text_input('Maximum Heart Rate achieved')
                
            with col3:
                exang = st.text_input('Exercise Induced Angina')
                
            with col1:
                oldpeak = st.text_input('ST depression induced by exercise')
                
            with col2:
                slope = st.text_input('Slope of the peak exercise ST segment')
                
            with col3:
                ca = st.text_input('Major vessels colored by flourosopy')
                
            with col1:
                thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
                
                
             
             
            # code for Prediction
            heart_diagnosis = ''
            
            # creating a button for Prediction
            
            if st.button('Heart Disease Test Result'):
                heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
                
                if (heart_prediction[0] == 1):
                  heart_diagnosis = 'The person is having heart disease'
                else:
                  heart_diagnosis = 'The person does not have any heart disease'
                
            st.success(heart_diagnosis)
                
            
            
    
        # Parkinson's Prediction Page
        if (selected == "Parkinsons Prediction"):
            
            # page title
            st.title("Parkinson's Disease Prediction using ML")
            
            col1, col2, col3, col4, col5 = st.columns(5)  
            
            with col1:
                fo = st.text_input('MDVP:Fo(Hz)')
                
            with col2:
                fhi = st.text_input('MDVP:Fhi(Hz)')
                
            with col3:
                flo = st.text_input('MDVP:Flo(Hz)')
                
            with col4:
                Jitter_percent = st.text_input('MDVP:Jitter(%)')
                
            with col5:
                Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
                
            with col1:
                rap = st.text_input('MDVP:RAP')
                
            with col2:
                ppq = st.text_input('MDVP:PPQ')
                
            with col3:
                DD = st.text_input('Jitter:DDP')
                
            with col4:
                MDVP = st.text_input('MDVP:Shimmer')
                
            with col5:
                MDVPB = st.text_input('MDVP:Shimmer(dB)')
                
            with col1:
                APQ3 = st.text_input('Shimmer:APQ3')
                
            with col2:
                APQ5 = st.text_input('Shimmer:APQ5')
                
            with col3:
                APQ = st.text_input('MDVP:APQ')
                
            with col4:
                NHR = st.text_input('NHR ')
                
            with col5:
                DDA= st.text_input('shimmer:DDA ')
                
            with col1:
                HNR = st.text_input('HNR')
                
            
                
            with col3:
                RPDE = st.text_input('RPDE')
                
            with col4:
                DFA = st.text_input('DFA')
                
            with col5:
                spread1 = st.text_input('spread1 ')
                
            with col1:
                spread2 = st.text_input('spread2')
                
            with col2:
                D2 = st.text_input('D2')
                
            with col3:
                PPE = st.text_input('PPE')
            # code for Prediction
            parkinsons_diagnosis = ''
            
            # creating a button for Prediction
            
            if st.button('Parkinsons Disease Test Result'):
                parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, rap, ppq, DD,MDVP,MDVPB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
                
                if (parkinsons_prediction[0] == 1):
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"
                
            st.success(parkinsons_diagnosis)
    
    
    
    
    
    
    
    
    
    
    
        if (selected == "Liver Prediction"):
            
            # page title
            st.title("liver Disease Prediction using ML")
    
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                Age = st.text_input('Age')
                
            with col2:
                Sex = st.text_input('Sex')
                
            with col3:
                Total_Bilirubin = st.text_input('Total Bilirubin')
                
            with col1:
                Direct_Bilirubin = st.text_input('Direct Bilirubin')
                
            with col2:
                Alkphos_Alkaline_Phosphotase = st.text_input(' Alkphos Alkaline Phosphotase')
                
            with col3:
                Sgpt_Alamine_Aminotransferase = st.text_input(' Sgpt Alamine Aminotransferase')
                
            with col1:
                Sgot_Aspartate_Aminotransferase = st.text_input('Sgot Aspartate Aminotransferase')
                
            with col2:
                Total_Protiens = st.text_input('Total Protiens')
                
            with col3:
                ALB_Albumin = st.text_input(' ALB Albumin')
                
            with col1:
                agratio = st.text_input('A/G Ratio Albumin and Globulin Ratio')
                
                
                
                
             
             
            # code for Prediction
            liver_diagnosis = ''
            
            # creating a button for Prediction
            
            if st.button('liver Disease Test Result'):
                liver_prediction = liver_model.predict([[Age,Sex,Total_Bilirubin,Direct_Bilirubin,Alkphos_Alkaline_Phosphotase,Sgpt_Alamine_Aminotransferase,Sgot_Aspartate_Aminotransferase,Total_Protiens, ALB_Albumin,agratio]])    
                              
                
                if (liver_prediction[0] == 1):
                  liver_diagnosis = 'The person is having liver disease'
                else:
                  liver_diagnosis = 'The person does not have any liver disease'
                
            st.success(liver_diagnosis)
            
            
        if selected == 'Kidney Disease Predictionid':

    # Page title
            st.title('Kidney Disease Prediction using ML')
        
            # Getting the input data from the user
            col1, col2, col3 = st.columns(3)
        
            
            
            with col1:
                age = st.text_input('Age')
                
            with col2:
                bp = st.text_input('blood pressure')
                
            with col3:
                sg = st.text_input('sg')
                
            with col1:
                al = st.text_input('al')
                
            with col2:
                su = st.text_input('su')
                
            with col3:
                rbc = st.text_input('rbc (yes==1 or no==0)')
                
            with col1:
                pc = st.text_input('pc (yes==1 or no==0)')
                
            with col2:
                pcc = st.text_input('pcc (yes==1 or no==0)')
                
            with col3:
                ba = st.text_input('ba (yes==1 or no==0)')
                
            with col1:
                bgr = st.text_input('bgr  ')
                
            with col2:
                bu = st.text_input('bu')
                
            with col3:
                sc = st.text_input('sc')
                
            with col1:
                sod = st.text_input('sod')
                
            with col2:
                pot = st.text_input('pod')
                
            with col3:
                hemo = st.text_input('hemo')
                
            with col1:
                pcv = st.text_input('pcv')
                
            with col2:
                wc = st.text_input('wc')
                
            with col3:
                rc = st.text_input('rc')
                
            with col1:
                htn = st.text_input('htn (yes==1 or no==0)')
                
            with col2:
                dm = st.text_input('dm  (yes==1 or no==0)')
                
            with col3:
                cad = st.text_input('cad  (yes==1 or no==0)')
                
                
            with col1:
                appet = st.text_input('appet (yes==1 or no==0)')
                
            with col2:
                pe = st.text_input('pe  (yes==1 or no==0)')
                
            with col3:
                ane = st.text_input('ane  (yes==1 or no==0)')
            # Code for Prediction
            kidney_diagnosis = ''
        
            # Creating a button for Prediction
            if st.button('Kidney Disease Test Result'):

                kidney_prediction = kidney_model.predict([[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe ,ane]])
        
                if (kidney_prediction[0] == 1):
                    kidney_diagnosis = 'The person may have kidney disease'
                else:
                    kidney_diagnosis = 'The person is not likely to have kidney disease'
        
            st.success(kidney_diagnosis)

    
