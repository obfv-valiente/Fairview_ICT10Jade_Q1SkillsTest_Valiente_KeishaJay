from pyscript import document, display


def create_order(e):
       document.getElementById("output1").innerHTML="" #clears previous result

num1 = float(document.getElementById("input1").value) #get input value 
num2 = float(document.getElementById("input2").value) #get input value
num3 = float(document.getElementById("input3").value) #get input value
num4 = float(document.getElementById("input4").value) #get input value
num5 = float(document.getElementById("input5").value) #get input value

result = num1 + num2 + num3 + num4 + num5 #use's the input value from the above to calculate

display(f"Subtotal: {result}", target="output1")

subtotal = (float(prod1))
