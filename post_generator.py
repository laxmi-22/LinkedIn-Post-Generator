from fewshots import FewShotsPost
from llm_helper import llm

fs=FewShotsPost()

# function to convert length value to map number of lines since model may not understand length specifictaion
def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"

# function to prepare prompt based on selection of emoji and user engage checkboxes
def get_structure_template(structure):
    prompt=""
    if structure == "Bullet Points":
       prompt += "\nFormat the content using bullet points (•) for main ideas.Each bullet point should starts with new line character."
       # prompt += "\nFormat the content as a bullet points list (•) for main ideas."

    elif structure == "Numbered List":
        prompt+= "\nFormat the content as a numbered list for main points."
    return prompt



# function to prepare prompt based on selection of emoji and user engage checkboxes
def get_emoji_engage_prompt(Emojis_Check,Engage_viewer):   
    prompt=""
    if Emojis_Check:
        prompt+= "\n Use Emojis in relevant places wherever necessary. You can use maximum 5 to 6 Emojis"

    if Engage_viewer:
        prompt+=  "\n At the end ask Viewers to engage in the post. Make it separate paragraph."
    return prompt


#Generate prompt based on user selected values- length,language,tag,Emojis_Check,Engage_viewer
def generate_prompt(length,language,tag,selected_tone, selected_structure,Emojis_Check,Engage_viewer):
    length_str = get_length_str(length)
    structure_template = get_structure_template(selected_structure)
    emoji_engage=get_emoji_engage_prompt(Emojis_Check,Engage_viewer)

    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {tag}
    2) Length: {length_str}
    3) Language: {language}
    4) Tone: {selected_tone} - maintain this tone throughout the post
    {structure_template}
    {emoji_engage}
    
    
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    
    #get filtered posts to provide example for llm 
    examples=fs.get_filtered_post(length,language,tag)

    if len(examples)>0:
        prompt+="5) Use the writing style as per the following examples."
        
    for i,post in enumerate(examples):
        post_text=post['text']
        prompt+=f'\n\n Example {i+1}: \n\n {post_text}'
        if i==1:
            break
    
    return prompt


#generate post
def generate_post(length,language,tag,selected_tone, selected_structure,Emojis_Check,Engage_viewer):
    #first create a final prompt
    prompt=generate_prompt(length,language,tag,selected_tone, selected_structure,Emojis_Check,Engage_viewer)

    #invoke llm by passing the final prompt
    response= llm.invoke(prompt)

    return response.content

    
# #main program
# if __name__=='__main__':
#     respone=generate_prompt("Short","English","LinkedIn")
#     print(respone)