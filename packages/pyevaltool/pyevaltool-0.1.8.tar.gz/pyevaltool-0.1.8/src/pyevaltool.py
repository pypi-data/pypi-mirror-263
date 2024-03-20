import requests
import pandas as pd
import json


def update_content_to_question(obj, question):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'role' and value == 'user':
                obj['content'] = question
            elif isinstance(value, (dict, list)):
                update_content_to_question(value, question)
    elif isinstance(obj, list):
        for item in obj:
            update_content_to_question(item, question)


def gpt_test(frontend_url,token,chat_completion_format,answer_loc, input_data,output_file = 'answered_prompt.csv' ):
#UAT
    url = frontend_url
    token =   token
    try :
        try:
            df  =  pd.read_excel(input_data)
        except:
            df  =  pd.read_csv(input_data)
    except:
        print("Input data file format is not correct. Please make sure that data is in excel or csv format.")

    try:
        questions = df['Prompt'].to_list()
    except:
        print("Please make sure that questions/user input attribute/collumn name is Prompt")

    output_df = pd.DataFrame()
    Question, Answer = [], []
    n = 1
    try:
        for question in questions:
            url = url
            data = chat_completion_format
            update_content_to_question(data, question)
            print("Question : ", question)
            print(data)
            token = token
            try:
                try:
                    headers = {     
                        "Content-Type": "application/json",     
                        "Ocp-Apim-Subscription-Key": token}
                except:
                    headers = {
                        'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/json'}
            except:
                print("It is appearing you are using other than Apim-Subscription-Key or Bearer token. Please use any of these")
            try:
                response = requests.post(url, json=data, headers=headers)
                print(response)
                print(response.status_code)
                if response.status_code !=200:
                    print("update the token")
                    break
                if response.status_code == 200:
                    Question.append(question)
                    answer = response.json()
                    answer = eval("answer" + answer_loc)
                    print("Answer :", answer)
                    Answer.append(answer)
                    print(f'Done {n}/{len(df)}', end="\r")
                    n += 1
                else:
                    print(f"Response code {response.status_code}")
                    break
            except:
                print("chat_completion_format should have question at chat_completion_format['messages'][0]['content']. Please check documentation for more information.")
        output_df['Question'] = Question
        output_df['Answer']= Answer
        output_df.to_csv(output_file)
        print("Sheet generated")
    except:
        print("Saving file failed")
