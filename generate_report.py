import random
import pandas as pd
import openai
from openai.error import RateLimitError, AuthenticationError

# OPENAI_API_KEY = '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'
# OPENAI_API_KEY = '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'
# OPENAI_API_KEY = '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'
# OPENAI_API_KEY = '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'
OPENAI_API_KEY = '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'


df_specifics = pd.read_csv('dataset/patients_detailed_data_specs.csv')
column_names = ['patient_id', 'test_id', 'name', 'Age', 'Gender', 'HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2', 'BaseExcess', 'HCO3', 'FiO2', 'PaCO2', 'SaO2', 'AST', 'BUN', 'Alkalinephos', 'Calcium', 'Glucose', 'Bilirubin_total', 'Hgb', 'Platelets', 'SepsisLabel']
column_details = ['Patient ID', 'Test ID', 'Name', 'Age', 'Gender', 'Heart rate', 'Pulse oximetry', 'Temperature', 'Systolic BP', 'Mean arterial pressure', 'Diastolic BP', 'Respiration rate', 'End tidal carbon dioxide', 'Measure of excess bicarbonate', 'Bicarbonate', 'Fraction of inspired oxygen', 'Partial pressure of carbon dioxide from arterial blood', 'Oxygen saturation from arterial blood', 'Aspartate transaminase', 'Blood urea nitrogen', 'Alkaline phosphatase', 'Calcium', 'Serum glucose', 'Total bilirubin', 'Hematocrit', 'Platelets', 'Does the patient have sepsis?']
column_units = ['', '', '', '', '', 'bpm', '%', 'Deg C', 'mm Hg', 'mm Hg', 'mm Hg', 'breaths per minute', 'mm Hg', 'mmol/L', 'mmol/L', '%', 'mm Hg', '%', 'IU/L', 'mg/dL', 'IU/L', 'mg/dL', 'mg/dL', 'mg/dL', 'g/dL', 'count*10^3/µL', '']

openai.api_key = OPENAI_API_KEY


def generate_medical_report(patient_id, test_id):
    # patient = df_specifics[df_specifics["patient_id"] == patient_id].iloc[0]

    print(patient_id)
    print(test_id)

    patient = df_specifics[(df_specifics["patient_id"] == patient_id) & (df_specifics["test_id"] == test_id)].iloc[0]
    prompt = ""

    # patient_data =

    for column in range(len(column_names)):
        if not pd.isna(patient[column_names[column]]):
            prompt += f'{column_details[column]}: {patient[column_names[column]]} {column_units[column]}\n'
            label_column = f'{column_names[column]}_label'

            if label_column in patient.index:
                prompt += f'{column_details[column]} value indicates: {patient[label_column]}\n'

    prompt += "Does the patient have any disease?\n" \
              "Generate a bullet-point medical report with a conclusion based on the above information for doctors."

    # try:
    #     completions = openai.Completion.create(
    #         engine="text-davinci-003",
    #         prompt=prompt,
    #         max_tokens=1024,
    #         n=1,
    #         stop=None,
    #         temperature=0.5,
    #     )
    #
    #     report = completions.choices[0].text.strip()
    #
    # # except (RateLimitError, AuthenticationError):
    # except Exception as e:
    #     print(e)

    report = f'Medical Report:\n• Patient ID: {patient["patient_id"]}\n• Name: {patient["name"]}\n• Age: {patient["Age"]}\n• Gender: {patient["Gender"]}\n\nVital Signs:\n• Heart rate: {patient["HR"]} {column_units[column_names.index("HR")]} ({patient["HR_label"]})\n• Pulse oximetry: {patient["O2Sat"]} {column_units[column_names.index("O2Sat")]} ({patient["O2Sat_label"]})\n• Temperature: 36.11 Deg C (normal)\n• Systolic BP: 98.0 mm Hg (Normal SBP)\n• Mean arterial pressure: 75.33 mm Hg (Normal)\n• Diastolic BP: 43.0 mm Hg (Low)\n• Respiration rate: 19.0 breaths per minute (Normal)\n• End tidal carbon dioxide: 35.0 mm Hg (Normal)\n• Measure of excess bicarbonate: 24.0 mmol/L (Alkalemia)\n• Bicarbonate: 45.0 mmol/L (High)\n• Fraction of inspired oxygen: 0.28 %\n• Partial pressure of carbon dioxide from arterial blood: 100.0 mm Hg (Hypercapnia)\n• Oxygen saturation from arterial blood: 88.0 % (moderate hypoxia)\n\nLaboratory Results:\n• Aspartate transaminase: 16.0 IU/L (Significantly elevated)\n• Blood urea nitrogen: 14.0 mg/dL (Significantly elevated)\n• Alkaline phosphatase: 98.0 IU/L (Significantly elevated)\n• Calcium: 9.3 mg/dL (Normal)\n• Serum glucose: 193.0 mg/dL (Significantly elevated)\n• Total bilirubin: 0.3 mg/dL (Significantly elevated)\n• Hematocrit: 12.5 g/dL (Mildly low)\n• Platelets: 317.0 count*10^3/µL (Highly decreased)\n\nConclusion:\n'

    if patient['SepsisLabel'] == 'yes':
        report += 'The patient does not have sepsis. However, further tests are recommended.'

    if patient['SepsisLabel'] == 'no':
        report += 'The patient has been diagnosed with sepsis.'

    # report = f'The patient, {patient["name"]}, is an {patient["Age"]}-year-old {patient["Gender"]} with a heart rate of {patient["HR"]} {column_units[column_names.index("HR")]},' \
    #          f' pulse oximetry of {patient["O2Sat"]} {column_units[column_names.index("O2Sat")]}, temperature of {patient["Temp"]} {column_units[column_names.index("Temp")]}, systolic BP of {patient["SBP"]} {column_units[column_names.index("SBP")]}, and diastolic BP of {patient["DBP"]} {column_units[column_names.index("DBP")]}. All these values are within the normal range. The respiration rate is {patient["Resp"]} {column_units[column_names.index("Resp")]}, end tidal carbon dioxide is {patient["EtCO2"]} {column_units[column_names.index("EtCO2")]}, and the measure of excess bicarbonate is {patient["BaseExcess"]} {column_units[column_names.index("BaseExcess")]}, ' \
    #          f'which indicates alkalemia. The bicarbonate level is {patient["HCO3"]} {column_units[column_names.index("HCO3")]}, indicating a high level. The fraction of inspired oxygen is {patient["FiO2"]} {column_units[column_names.index("FiO2")]}, partial pressure of carbon dioxide from arterial blood is {patient["PaCO2"]} {column_units[column_names.index("PaCO2")]}, indicating hypercapnia, and the oxygen saturation from arterial blood is 88.0%, indicating moderate hypoxia. The patient\'s aspartate transaminase, blood urea nitrogen, alkaline phosphatase, serum glucose, and total bilirubin levels are significantly elevated. The hematocrit is mildly low and the platelets are highly decreased. ' \
    #          f'The patient does not have sepsis. '
    #
    # report += '\nBased on the results, it is suggested that the patient should be monitored for any signs of infection and be prescribed medications to reduce elevated levels of aspartate transaminase, blood urea nitrogen, alkaline phosphatase, serum glucose, and total bilirubin. The patient should be given supplements to increase the platelet count and hematocrit levels. Additionally, the patient should be provided with oxygen therapy to improve oxygen saturation and reduce hypercapnia.'

    # report = f'The patient, {patient["name"]}, is an {patient["Age"]}-year-old {patient["Gender"]} with a heart rate of 97.0 bpm, pulse oximetry of 95.0 %, temperature of 36.11 Deg C, systolic BP of 98.0 mm Hg, and diastolic BP of 43.0 mm Hg. All these values are within the normal range. The respiration rate is 19.0 breaths per minute, end tidal carbon dioxide is 35.0 mm Hg, and the measure of excess bicarbonate is 24.0 mmol/L, which indicates alkalemia. The bicarbonate level is 45.0 mmol/L, indicating a high level. The fraction of inspired oxygen is 0.28%, partial pressure of carbon dioxide from arterial blood is 100.0 mm Hg, indicating hypercapnia, and the oxygen saturation from arterial blood is 88.0%, indicating moderate hypoxia. The patient\'s aspartate transaminase, blood urea nitrogen, alkaline phosphatase, serum glucose, and total bilirubin levels are significantly elevated. The hematocrit is mildly low and the platelets are highly decreased. The patient does not have sepsis. \nBased on the results, it is suggested that the patient should be monitored for any signs of infection and be prescribed medications to reduce elevated levels of aspartate transaminase, blood urea nitrogen, alkaline phosphatase, serum glucose, and total bilirubin. The patient should be given supplements to increase the platelet count and hematocrit levels. Additionally, the patient should be provided with oxygen therapy to improve oxygen saturation and reduce hypercapnia.'
    # report = report.replace('\n', '<br>')

    return report


def generate_report_from_template(data):
    random_number = random.randint(1, 10)

    report = 'Medical Report:\n• Patient ID: p000001\n• Name: Melissa Davis\n• Age: 83\n• Gender: female\n\n'

    if random_number % 2 == 0:
        vital_signs = ['HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2', 'BaseExcess', 'HCO3', 'FiO2', 'PaCO2', 'SaO2']
        lab_results = ['AST', 'BUN', 'Alkalinephos', 'Calcium', 'Glucose', 'Bilirubin_total', 'Hgb', 'Platelets']

        report += 'Vital Signs:\n'

        for vital_sign in vital_signs:
            if data.get(vital_sign) and data.get(f'{vital_sign}_label'):
                report += f'• {column_details[column_names.index(vital_sign)]}: {data[vital_sign]} {column_units[column_names.index(vital_sign)]} ({data[f"{vital_sign}_label"]})\n'

        report += '\nLaboratory Results:\n'
        for lab_result in lab_results:
            if data.get(lab_result) and data.get(f'{lab_result}_label'):
                report += f'• {column_details[column_names.index(lab_result)]}: {data[lab_result]} {column_units[column_names.index(lab_result)]} ({data[f"{lab_result}_label"]})\n'

    else:
        report += 'Vital Signs and Laboratory Results:\n'

        for column_name in column_names:
            if data.get(column_name) and data.get(f'{column_name}_label'):
                report += f'• {column_details[column_names.index(column_name)]}: {data[column_name]} {column_units[column_names.index(column_name)]} ({data[f"{column_name}_label"]})\n'

    report += '\nConclusion:\n'

    if data['SepsisLabel'] == 'yes':
        report += 'The patient does not have sepsis. However, further tests are recommended.'

    if data['SepsisLabel'] == 'no':
        report += 'The patient has been diagnosed with sepsis.'

    return report


if __name__ == '__main__':
    x = generate_medical_report('p000001', 1)
    print(x)

