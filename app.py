import streamlit as st
from fewshots import FewShotsPost
from post_generator import generate_post

# options for length, language,tone and structure of post dropdowns. This can be extended in future 
length_options=["Short","Medium","Long"]
language_options=["English","Hinglish"]
tone_options = ["Professional", "Casual", "Motivational", "Educational", "Story-telling"]
structure_options = ["Regular", "Bullet Points", "Numbered List"]

# main program
def main():
    st.title("Linked In Post Generator")

    #create 3 columns for the dropdowns- title,length,language
    col1,col2,col3=st.columns(3)
    
    fs=FewShotsPost()
    tags=fs.get_tags()
    
    with col1:
        #dropdown for Tags or tile
        selected_tag=st.selectbox("Topic",options=tags)
        #dropdown for tone
        selected_tone = st.selectbox("Tone", options=tone_options,index=0)
    
    with col2:
        #dropdown for length
        selected_length=st.selectbox("Length",options=length_options)
        #dropdown for structure
        selected_structure = st.selectbox("Structure", options=structure_options,index=0)
    
    with col3:
        #dropdown for language
        selected_language=st.selectbox("Language",options=language_options)
    
    #checkboxes for including Emoji, engage Viewers
    Emojis_Check = st.checkbox("Add Emojis in the post?")
    Engage_viewer= st.checkbox("Engage viewers to this post?")

    #Genrate button 
    if st.button("Generate"):
        final_post=generate_post(selected_length,selected_language,selected_tag,selected_tone,selected_structure,Emojis_Check,Engage_viewer)
        st.write(final_post)

# Run the aplication
if __name__=='__main__':
    main()