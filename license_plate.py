
from tkinter import messagebox
from tkinter import *
from car_api_response import additional_apis


"""create tabs based on the API response"""


def append_tab(cd, url, tab):
    # Create a temporary dictionary from the info returned from the API and set up the text variables
    temp_dict = additional_apis(url)
    output_dict = {}
    if temp_dict:
        question_text = ''
        response_text = ''

        # Ask for every question and variable within that response and save it in a variable
        for response in temp_dict:
            for item in response:
                question = item
                var = response[question]
                # Look if the response is a link or not, if so, append additional urls
                if 'api_' in question:
                    cd.additional_urls.append(var)
                    cd.additional_urls_titles.append(question)
                    continue
                # Append the text based on the question and responses
                question_text = question_text + question + '\n'
                response_text = response_text + var + '\n'
                # Save the text to use when exporting details to a Word file
                output_dict[question] = var

        # Create the labels and put them next to each other
        question_label = Label(tab, text=question_text, width=50)
        question_label.grid(column=0, row=1)
        response_label = Label(tab, text=response_text)
        response_label.grid(column=1, row=1)
        cd.dict_output[url] = output_dict

    elif len(cd.additional_urls) == 0:
        messagebox.showinfo('error', 'license-plate does not exist')
