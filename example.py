from email.headerregistry import ContentTypeHeader

import PySimpleGUIQt as s

form= s.FlexForm("My Identification")

layout = [[s.Text("Enter your name:", size=(15, 1))],
          [s.InputText()],
          [s.Text("What your age:", size=(15, 1))],
          [s.InputText()],
          [s.Text("Enter your Country:", size=(15, 1))],
          [s.InputText()],
          [s.Text("Enter your City:", size= (15, 1))],
          [s.InputText()],
          [s.Button("Submit"), s.Button("Cancel")]]
button, values = form.Layout(layout).Read()
name= values[0]
age= values[1]
country= values[2]
city= values[3]
print(f"name {name}, age {age}, country {country}, city {city} ")