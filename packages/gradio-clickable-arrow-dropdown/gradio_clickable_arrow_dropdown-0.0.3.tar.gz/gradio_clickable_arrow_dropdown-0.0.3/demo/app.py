import gradio as gr
from gradio_clickable_arrow_dropdown import ClickableArrowDropdown

def handle_inputs(reg_dropdown_val, custom_dropdown_val):
    res = f"""
    Regular dropdown value: {reg_dropdown_val}
    Custom dropdown value: {custom_dropdown_val}
    """

    return res

choices = ["Option 1", "Option 2", "Option 3"]

demo = gr.Interface(
    handle_inputs,
    [
        gr.Dropdown(choices=choices, value=choices[0], filterable=False), 
        ClickableArrowDropdown(choices=choices, value=choices[0], filterable=False)
    ],
    gr.Textbox(),
)

if __name__ == "__main__":
    demo.launch()
